#!/usr/bin/env python3
"""Launch the Ruen Bongkot website locally.

Run with:  python3 run.py   (or double-click on most systems)
Serves the site at http://localhost:8000 and opens it in your browser.
"""
import http.server
import os
import socketserver
import threading
import webbrowser

PORT = 8000

os.chdir(os.path.dirname(os.path.abspath(__file__)))

socketserver.TCPServer.allow_reuse_address = True
with socketserver.TCPServer(("", PORT), http.server.SimpleHTTPRequestHandler) as httpd:
    url = f"http://localhost:{PORT}"
    print(f"🪷 Ruen Bongkot is live at {url}")
    print("Press Ctrl+C to stop.")
    threading.Timer(0.5, lambda: webbrowser.open(url)).start()
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped. Goodbye!")
