#!/usr/bin/env python3
"""Launch the Ruen Bongkot website locally.

Run with:  python3 run.py   (or double-click on most systems)
Serves the site at http://localhost:3000 and opens it in your browser.
Pass a different port as an argument if needed:  python3 run.py 8080
"""
import http.server
import os
import socketserver
import sys
import threading
import webbrowser

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 3000

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def create_server(port, attempts=10):
    """Bind to the requested port, falling forward if it's taken."""
    for candidate in range(port, port + attempts):
        try:
            return candidate, socketserver.TCPServer(
                ("", candidate), http.server.SimpleHTTPRequestHandler
            )
        except OSError:
            print(f"⚠️  Port {candidate} is already in use, trying {candidate + 1}...")
    raise SystemExit(
        f"Could not find a free port between {port} and {port + attempts - 1}. "
        f"Try another one: python3 run.py 8080"
    )


socketserver.TCPServer.allow_reuse_address = True
PORT, server = create_server(PORT)
with server as httpd:
    url = f"http://localhost:{PORT}"
    print(f"🪷 Ruen Bongkot is live at {url}")
    print("Press Ctrl+C to stop.")
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped. Goodbye!")
