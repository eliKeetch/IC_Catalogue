# Raspberry Pi Local Hosting

Recommended format for this project: a small Python web app with SQLite.

Why this format fits:

- Runs locally on a Raspberry Pi without a cloud account.
- Stores inventory in one file: `data/components.sqlite3`.
- Serves the site and API from one command: `python server.py`.
- Static frontend files are plain HTML, CSS, and JavaScript.
- Easy to back up by copying the project folder.

## Run Locally

```powershell
python server.py
```

Open:

```text
http://localhost:8080
```

## Run On Raspberry Pi

```bash
sudo apt update
sudo apt install python3
python3 server.py
```

From another device on the same network, open:

```text
http://<pi-ip-address>:8080
```

## Component List Format

For future bulk imports, use this plain text style:

```text
LM358, quantity: 4, location: A1
NE555, quantity: 10, location: A2
74HC595, quantity: 6, location: Logic drawer
```

Quantity and location are optional. If omitted, quantity starts at `1` and location is left blank.
