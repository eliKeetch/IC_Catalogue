from __future__ import annotations

import json
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from seed_components import COMPONENTS  # noqa: E402


DB_PATH = ROOT / "data" / "components.sqlite3"


def now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def main() -> None:
    if not DB_PATH.exists():
        raise SystemExit(f"Database not found: {DB_PATH}")

    conn = sqlite3.connect(DB_PATH)
    try:
        ensure_columns(conn)
        timestamp = now_iso()
        for component in COMPONENTS:
            conn.execute(
                """
                UPDATE components SET
                    category = ?,
                    package = ?,
                    summary = ?,
                    uses = ?,
                    project_ideas = ?,
                    pins = ?,
                    documents = ?,
                    model_type = ?,
                    datasheet_url = ?,
                    notes = ?,
                    updated_at = ?
                WHERE lower(name) = lower(?)
                """,
                (
                    component.get("category", "Uncategorized"),
                    component.get("package", ""),
                    component.get("summary", ""),
                    json.dumps(component.get("uses", [])),
                    json.dumps(component.get("project_ideas", [])),
                    json.dumps(component.get("pins", [])),
                    json.dumps(component.get("documents", [])),
                    component.get("model_type", ""),
                    component.get("datasheet_url", ""),
                    component.get("notes", ""),
                    timestamp,
                    component["name"],
                ),
            )
        conn.commit()
    finally:
        conn.close()


def ensure_columns(conn: sqlite3.Connection) -> None:
    columns = {row[1] for row in conn.execute("PRAGMA table_info(components)").fetchall()}
    if "model_type" not in columns:
        conn.execute("ALTER TABLE components ADD COLUMN model_type TEXT NOT NULL DEFAULT ''")


if __name__ == "__main__":
    main()
