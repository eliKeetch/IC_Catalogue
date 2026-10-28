from __future__ import annotations

import json
import mimetypes
import re
import sqlite3
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, unquote, urlparse

from seed_components import COMPONENTS


ROOT = Path(__file__).resolve().parent
STATIC_DIR = ROOT / "static"
DATA_DIR = ROOT / "data"
DB_PATH = DATA_DIR / "components.sqlite3"
HOST = "0.0.0.0"
PORT = 8080


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def slugify(value: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", value.strip().lower()).strip("-")
    return slug or "component"


def db() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def encode_json(value) -> str:
    if isinstance(value, str):
        try:
            json.loads(value)
            return value
        except json.JSONDecodeError:
            return json.dumps([line.strip() for line in value.splitlines() if line.strip()])
    return json.dumps(value or [])


def row_to_component(row: sqlite3.Row) -> dict:
    item = dict(row)
    for key in ("uses", "project_ideas", "pins", "documents"):
        try:
            item[key] = json.loads(item.get(key) or "[]")
        except json.JSONDecodeError:
            item[key] = []
    return item


def init_db() -> None:
    DATA_DIR.mkdir(exist_ok=True)
    (DATA_DIR / "docs").mkdir(exist_ok=True)
    with db() as conn:
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS components (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                slug TEXT NOT NULL UNIQUE,
                name TEXT NOT NULL,
                category TEXT NOT NULL DEFAULT 'Uncategorized',
                package TEXT NOT NULL DEFAULT '',
                quantity INTEGER NOT NULL DEFAULT 0,
                location TEXT NOT NULL DEFAULT '',
                summary TEXT NOT NULL DEFAULT '',
                uses TEXT NOT NULL DEFAULT '[]',
                project_ideas TEXT NOT NULL DEFAULT '[]',
                pins TEXT NOT NULL DEFAULT '[]',
                documents TEXT NOT NULL DEFAULT '[]',
                model_type TEXT NOT NULL DEFAULT '',
                datasheet_url TEXT NOT NULL DEFAULT '',
                notes TEXT NOT NULL DEFAULT '',
                created_at TEXT NOT NULL,
                updated_at TEXT NOT NULL
            )
            """
        )
        ensure_columns(conn)
        count = conn.execute("SELECT COUNT(*) FROM components").fetchone()[0]
        if count == 0:
            seed_components(conn)


def ensure_columns(conn: sqlite3.Connection) -> None:
    columns = {row["name"] for row in conn.execute("PRAGMA table_info(components)").fetchall()}
    if "model_type" not in columns:
        conn.execute("ALTER TABLE components ADD COLUMN model_type TEXT NOT NULL DEFAULT ''")


def seed_components(conn: sqlite3.Connection) -> None:
    timestamp = now_iso()
    for component in COMPONENTS:
        payload = {
            "slug": unique_slug(conn, component["name"]),
            "name": component["name"],
            "category": component.get("category", "Uncategorized"),
            "package": component.get("package", ""),
            "quantity": component.get("quantity", 1),
            "location": component.get("location", ""),
            "summary": component.get("summary", ""),
            "uses": json.dumps(component.get("uses", [])),
            "project_ideas": json.dumps(component.get("project_ideas", [])),
            "pins": json.dumps(component.get("pins", [])),
            "documents": json.dumps(component.get("documents", [])),
            "model_type": component.get("model_type", ""),
            "datasheet_url": component.get("datasheet_url", ""),
            "notes": component.get("notes", ""),
            "created_at": timestamp,
            "updated_at": timestamp,
        }
        conn.execute(
            """
            INSERT INTO components (
                slug, name, category, package, quantity, location, summary,
                uses, project_ideas, pins, documents, model_type, datasheet_url, notes,
                created_at, updated_at
            ) VALUES (
                :slug, :name, :category, :package, :quantity, :location, :summary,
                :uses, :project_ideas, :pins, :documents, :model_type, :datasheet_url, :notes,
                :created_at, :updated_at
            )
            """,
            payload,
        )


def unique_slug(conn: sqlite3.Connection, name: str, existing_id: int | None = None) -> str:
    base = slugify(name)
    candidate = base
    suffix = 2
    while True:
        row = conn.execute("SELECT id FROM components WHERE slug = ?", (candidate,)).fetchone()
        if row is None or row["id"] == existing_id:
            return candidate
        candidate = f"{base}-{suffix}"
        suffix += 1


def component_payload(data: dict, conn: sqlite3.Connection, existing_id: int | None = None) -> dict:
    name = str(data.get("name") or "").strip()
    if not name:
        raise ValueError("Component name is required.")

    quantity = int(data.get("quantity") or 0)
    if quantity < 0:
        raise ValueError("Quantity cannot be negative.")

    return {
        "slug": unique_slug(conn, name, existing_id),
        "name": name,
        "category": str(data.get("category") or "Uncategorized").strip() or "Uncategorized",
        "package": str(data.get("package") or "").strip(),
        "quantity": quantity,
        "location": str(data.get("location") or "").strip(),
        "summary": str(data.get("summary") or "").strip(),
        "uses": encode_json(data.get("uses")),
        "project_ideas": encode_json(data.get("project_ideas")),
        "pins": encode_json(data.get("pins")),
        "documents": encode_json(data.get("documents")),
        "model_type": str(data.get("model_type") or "").strip(),
        "datasheet_url": str(data.get("datasheet_url") or "").strip(),
        "notes": str(data.get("notes") or "").strip(),
        "updated_at": now_iso(),
    }


class Handler(BaseHTTPRequestHandler):
    server_version = "ComponentCatalogue/0.1"

    def do_GET(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/"):
            self.handle_api_get(parsed.path, parse_qs(parsed.query))
            return
        self.serve_static(parsed.path)

    def do_POST(self) -> None:
        parsed = urlparse(self.path)
        if parsed.path == "/api/components":
            self.create_component()
            return
        self.send_error_json(404, "Endpoint not found.")

    def do_PUT(self) -> None:
        parsed = urlparse(self.path)
        match = re.fullmatch(r"/api/components/(\d+)", parsed.path)
        if match:
            self.update_component(int(match.group(1)))
            return
        self.send_error_json(404, "Endpoint not found.")

    def do_PATCH(self) -> None:
        parsed = urlparse(self.path)
        match = re.fullmatch(r"/api/components/(\d+)/quantity", parsed.path)
        if match:
            self.update_quantity(int(match.group(1)))
            return
        self.send_error_json(404, "Endpoint not found.")

    def handle_api_get(self, path: str, query: dict) -> None:
        if path == "/api/components":
            search = (query.get("q") or [""])[0].strip()
            category = (query.get("category") or [""])[0].strip()
            sql = "SELECT * FROM components"
            filters = []
            params = []
            if search:
                filters.append("(name LIKE ? OR summary LIKE ? OR notes LIKE ?)")
                params.extend([f"%{search}%", f"%{search}%", f"%{search}%"])
            if category:
                filters.append("category = ?")
                params.append(category)
            if filters:
                sql += " WHERE " + " AND ".join(filters)
            sql += " ORDER BY category, name"
            with db() as conn:
                rows = conn.execute(sql, params).fetchall()
            self.send_json([row_to_component(row) for row in rows])
            return

        if path == "/api/categories":
            with db() as conn:
                rows = conn.execute("SELECT DISTINCT category FROM components ORDER BY category").fetchall()
            self.send_json([row["category"] for row in rows])
            return

        match = re.fullmatch(r"/api/components/(\d+)", path)
        if match:
            with db() as conn:
                row = conn.execute("SELECT * FROM components WHERE id = ?", (int(match.group(1)),)).fetchone()
            if not row:
                self.send_error_json(404, "Component not found.")
                return
            self.send_json(row_to_component(row))
            return

        self.send_error_json(404, "Endpoint not found.")

    def create_component(self) -> None:
        try:
            data = self.read_json()
            with db() as conn:
                payload = component_payload(data, conn)
                timestamp = now_iso()
                conn.execute(
                    """
                    INSERT INTO components (
                        slug, name, category, package, quantity, location, summary,
                        uses, project_ideas, pins, documents, model_type, datasheet_url, notes,
                        created_at, updated_at
                    ) VALUES (
                        :slug, :name, :category, :package, :quantity, :location, :summary,
                        :uses, :project_ideas, :pins, :documents, :model_type, :datasheet_url, :notes,
                        :created_at, :updated_at
                    )
                    """,
                    {**payload, "created_at": timestamp},
                )
                row = conn.execute("SELECT * FROM components WHERE id = last_insert_rowid()").fetchone()
            self.send_json(row_to_component(row), 201)
        except (ValueError, sqlite3.Error, json.JSONDecodeError) as exc:
            self.send_error_json(400, str(exc))

    def update_component(self, component_id: int) -> None:
        try:
            data = self.read_json()
            with db() as conn:
                current = conn.execute("SELECT * FROM components WHERE id = ?", (component_id,)).fetchone()
                if not current:
                    self.send_error_json(404, "Component not found.")
                    return
                payload = component_payload({**row_to_component(current), **data}, conn, component_id)
                conn.execute(
                    """
                    UPDATE components SET
                        slug = :slug,
                        name = :name,
                        category = :category,
                        package = :package,
                        quantity = :quantity,
                        location = :location,
                        summary = :summary,
                        uses = :uses,
                        project_ideas = :project_ideas,
                        pins = :pins,
                        documents = :documents,
                        model_type = :model_type,
                        datasheet_url = :datasheet_url,
                        notes = :notes,
                        updated_at = :updated_at
                    WHERE id = :id
                    """,
                    {**payload, "id": component_id},
                )
                row = conn.execute("SELECT * FROM components WHERE id = ?", (component_id,)).fetchone()
            self.send_json(row_to_component(row))
        except (ValueError, sqlite3.Error, json.JSONDecodeError) as exc:
            self.send_error_json(400, str(exc))

    def update_quantity(self, component_id: int) -> None:
        try:
            data = self.read_json()
            delta = int(data.get("delta") or 0)
            with db() as conn:
                row = conn.execute("SELECT quantity FROM components WHERE id = ?", (component_id,)).fetchone()
                if not row:
                    self.send_error_json(404, "Component not found.")
                    return
                quantity = max(0, row["quantity"] + delta)
                conn.execute(
                    "UPDATE components SET quantity = ?, updated_at = ? WHERE id = ?",
                    (quantity, now_iso(), component_id),
                )
                updated = conn.execute("SELECT * FROM components WHERE id = ?", (component_id,)).fetchone()
            self.send_json(row_to_component(updated))
        except (ValueError, sqlite3.Error, json.JSONDecodeError) as exc:
            self.send_error_json(400, str(exc))

    def read_json(self) -> dict:
        length = int(self.headers.get("Content-Length") or 0)
        raw = self.rfile.read(length).decode("utf-8") if length else "{}"
        return json.loads(raw or "{}")

    def serve_static(self, path: str) -> None:
        if path == "/docs" or path.startswith("/docs/"):
            self.serve_file(DATA_DIR / "docs", path.removeprefix("/docs").lstrip("/"))
            return
        if path == "/images" or path.startswith("/images/"):
            self.serve_file(ROOT / "images", path.removeprefix("/images").lstrip("/"))
            return
        clean = unquote(path).lstrip("/")
        if not clean:
            clean = "index.html"
        self.serve_file(STATIC_DIR, clean)

    def serve_file(self, base_dir: Path, relative_path: str) -> None:
        target = (base_dir / unquote(relative_path)).resolve()
        if not str(target).startswith(str(base_dir.resolve())) or not target.exists() or target.is_dir():
            self.send_error(404)
            return
        content_type = mimetypes.guess_type(target.name)[0] or "application/octet-stream"
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(target.stat().st_size))
        self.end_headers()
        self.wfile.write(target.read_bytes())

    def send_json(self, payload, status: int = 200) -> None:
        body = json.dumps(payload, indent=2).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def send_error_json(self, status: int, message: str) -> None:
        self.send_json({"error": message}, status)


if __name__ == "__main__":
    init_db()
    print(f"Component Catalogue running at http://localhost:{PORT}")
    print(f"Database: {DB_PATH}")
    ThreadingHTTPServer((HOST, PORT), Handler).serve_forever()
