import rsa

# Générer une paire de clés RSA (2048 bits)
(public_key, private_key) = rsa.newkeys(2048)

# Enregistrer la clé privée dans client_private.pem
with open("client_private_fake.pem", "wb") as f:
    f.write(private_key.save_pkcs1("PEM"))



print("✅ Clés RSA générées : client_private.pem et client_public.pem")
