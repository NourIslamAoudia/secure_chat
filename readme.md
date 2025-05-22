# Secure Chat (Python)

Un système de chat sécurisé utilisant le chiffrement RSA.

## 🚀 Installation

1. **Clonez le dépôt** :
   ```bash
   git clone https://github.com/NourIslamAoudia/secure_chat.git
   cd secure_chat
   ```

2. **Créez un environnement virtuel** (Python 3.7+) :
   ```bash
   python -m venv venv
   ```

3. **Activez l'environnement** :
   - **Windows (PowerShell)** :
     ```powershell
     .\venv\Scripts\Activate.ps1
     ```
   - **Linux/MacOS** :
     ```bash
     source venv/bin/activate
     ```

4. **Installez les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

## ▶️ Exécution

- **Lancer le serveur** :
  ```bash
  python server.py
  ```

- **Lancer le client** :
  ```bash
  python client.py
  ```

## 📁 Structure des fichiers
```
secure_chat/
├── generate_keys.py           # Génère les paires de clés RSA
├── server.py                  # Serveur de chat
├── client.py                  # Client de chat
├── client_public.pem          # Clé publique du client
├── client_private.pem         # Clé privée du client
├── server_public.pem          # Clé publique du serveur
├── server_private.pem         # Clé privée du serveur
├── requirements.txt           # Dépendances Python
└── README.md                  # Ce fichier
```

## 📜 Licence
MIT