#!/usr/bin/env python3
"""
Simple HTTP server for Math Hack Terminal game.
Run with: python3 serve.py
Then open browser to: http://your-ip-address:8000
"""

import http.server
import socketserver
import socket

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

def get_local_ip():
    """Get the local IP address"""
    try:
        # Connect to a remote server to determine local IP
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "localhost"

if __name__ == "__main__":
    local_ip = get_local_ip()
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print("=" * 50)
        print("🎮 MATH HACK TERMINAL SERVER")
        print("=" * 50)
        print(f"🌐 Local access: http://localhost:{PORT}")
        print(f"📱 iPad access: http://{local_ip}:{PORT}")
        print("=" * 50)
        print("Press Ctrl+C to stop the server")
        print("=" * 50)
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n🛑 Server stopped")