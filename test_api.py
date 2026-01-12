# test_api.py
import os

api_key = os.environ.get("OPENAI_API_KEY")
print(f"📏 Longueur de la clé : {len(api_key) if api_key else 0} caractères")

if api_key:
    if api_key.startswith("sk-"):
        print("✅ Format de clé OpenAI détecté")
    else:
        print("⚠️ La clé ne commence pas par 'sk-', vérifiez-la")
else:
    print("❌ OPENAI_API_KEY non définie")
    
# Test supplémentaire : vérifier les permissions
import stat
import os.path

secrets_file = os.path.expanduser("~/.secrets/api_keys.sh")
if os.path.exists(secrets_file):
    permissions = stat.S_IMODE(os.stat(secrets_file).st_mode)
    print(f"🔐 Permissions du fichier : {oct(permissions)}")
    if permissions == 0o600:
        print("✅ Permissions sécurisées (600)")
    else:
        print(f"⚠️ Permissions incorrectes : {oct(permissions)}. Exécutez : chmod 600 {secrets_file}")