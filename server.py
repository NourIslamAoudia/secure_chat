# server.py
import socket
import rsa
from Crypto.Cipher import AES
import base64
import json

# === Chargement des clés ===
with open("server_private.pem", "rb") as f:
    server_private = rsa.PrivateKey.load_pkcs1(f.read())

with open("client_public.pem", "rb") as f:
    client_public = rsa.PublicKey.load_pkcs1(f.read())

# === Serveur socket ===
server = socket.socket()
server.bind(("0.0.0.0", 9999))
server.listen(1)
print("Serveur en écoute sur le port 9999...")

conn, addr = server.accept()
print(f"Connexion de {addr}")

data = conn.recv(4096)
conn.close()

try:
    # === Décodage JSON ===
    data = json.loads(data.decode())
    encrypted_aes_key = base64.b64decode(data['aes_key'])
    nonce = base64.b64decode(data['nonce'])
    tag = base64.b64decode(data['tag'])
    ciphertext = base64.b64decode(data['ciphertext'])

    # === Déchiffrement de la clé AES avec RSA ===
    aes_key = rsa.decrypt(encrypted_aes_key, server_private)

    # === Déchiffrement du message avec AES ===
    cipher = AES.new(aes_key, AES.MODE_EAX, nonce=nonce)
    full_message = cipher.decrypt_and_verify(ciphertext, tag)

    # === Séparation du message et de la signature ===
    message, signature = full_message.split(b'||')

    # === Vérification de la signature ===
    try:
        rsa.verify(message, signature, client_public)
        print(f"✅ Message vérifié : {message.decode()}")
    except rsa.VerificationError:
        print("❌ Signature invalide ! ATTENTION : MITM ?")

except Exception as e:
    print("❌ Erreur lors du traitement :", e)
