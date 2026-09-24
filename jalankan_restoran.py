"""
jalankan_restoran.py
Menjalankan server lokal untuk halaman restoran.
"""

import os
import webbrowser
import http.server
import socketserver
import threading

NAMA_HTML = "revisi-restoran.html"
PORT = 8000


def jalankan_server():
    if not os.path.exists(NAMA_HTML):
        print(f"❌ File '{NAMA_HTML}' tidak ditemukan di folder ini.")
        print(f"   Folder saat ini: {os.getcwd()}")
        return

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        url = f"http://localhost:{PORT}/{NAMA_HTML.replace(' ', '%20')}"
        print("=" * 55)
        print(f"🌐 Server berjalan di: {url}")
        print("   Tekan Ctrl+C untuk berhenti.")
        print("=" * 55)
        threading.Timer(1, lambda: webbrowser.open(url)).start()
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Server dihentikan.")


if __name__ == "__main__":
    jalankan_server()