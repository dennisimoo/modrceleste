import os
import http.server

class SecureHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add required security headers
        self.send_header("Cross-Origin-Opener-Policy", "same-origin")
        self.send_header("Cross-Origin-Embedder-Policy", "require-corp")
        super().end_headers()

# Get PORT from Render (fallback to 8080 locally)
PORT = int(os.getenv("PORT", 8080))

# Allow external connections (Render requires 0.0.0.0)
server_address = ('0.0.0.0', PORT)

httpd = http.server.HTTPServer(server_address, SecureHTTPRequestHandler)

print(f"Serving on port {PORT}...")
httpd.serve_forever()
