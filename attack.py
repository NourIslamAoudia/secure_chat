import socket
import rsa
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64
import json

# === Clés ===
with open("client_private_fake.pem", "rb") as f:
    client_private = rsa.PrivateKey.load_pkcs1(f.read())

with open("server_public.pem", "rb") as f:
    server_public = rsa.PublicKey.load_pkcs1(f.read())

# === Message à envoyer ===
message = b"Message depuis Kali Linux !"

# === Signature RSA ===
signature = rsa.sign(message, client_private, 'SHA-256')

# === Message complet ===
full_message = message + b'||' + signature

# === Chiffrement AES ===
aes_key = get_random_bytes(16)
cipher = AES.new(aes_key, AES.MODE_EAX)
ciphertext, tag = cipher.encrypt_and_digest(full_message)

# === Chiffrement de la clé AES ===
encrypted_aes_key = rsa.encrypt(aes_key, server_public)

# === Données encodées en Base64 ===
data = {
    'aes_key': base64.b64encode(encrypted_aes_key).decode(),
    'nonce': base64.b64encode(cipher.nonce).decode(),
    'tag': base64.b64encode(tag).decode(),
    'ciphertext': base64.b64encode(ciphertext).decode()
}

# === Envoi JSON ===
json_data = json.dumps(data).encode()

# === Connexion au serveur ===
client = socket.socket()
client.connect(("192.168.100.5", 9999))
client.send(json_data)
client.close()
