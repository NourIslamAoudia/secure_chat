# generate_keys.py
import rsa

def generate_keys(name):
    public_key, private_key = rsa.newkeys(2048)

    with open(f'{name}_public.pem', 'wb') as f:
        f.write(public_key.save_pkcs1('PEM'))
    with open(f'{name}_private.pem', 'wb') as f:
        f.write(private_key.save_pkcs1('PEM'))

    print(f"Clés pour {name} générées.")

# Génère les clés pour client et serveur
generate_keys('client')
generate_keys('server')
