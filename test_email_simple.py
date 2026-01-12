#!/usr/bin/env python3
# test_email_simple.py

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

print("🔍 Test d'envoi d'email Gmail simple...")

# Récupérer le mot de passe d'environnement
password = os.environ.get('GMAIL_APP_PASSWORD')
if not password:
    print("❌ GMAIL_APP_PASSWORD non défini")
    print("Exportez-le avec: export GMAIL_APP_PASSWORD='votre_mot_de_passe'")
    exit(1)

print(f"🔑 Mot de passe récupéré ({len(password)} caractères)")

# Tester avec différentes configurations
configs = [
    {
        'name': 'Port 587 avec TLS',
        'server': 'smtp.gmail.com',
        'port': 587,
        'use_tls': True,
        'use_ssl': False
    },
    {
        'name': 'Port 465 avec SSL',
        'server': 'smtp.gmail.com',
        'port': 465,
        'use_tls': False,
        'use_ssl': True
    }
]

for config in configs:
    print(f"\n🔄 Test: {config['name']}")
    print(f"  Serveur: {config['server']}:{config['port']}")
    print(f"  TLS: {config['use_tls']}, SSL: {config['use_ssl']}")
    
    try:
        if config['use_ssl']:
            server = smtplib.SMTP_SSL(config['server'], config['port'])
        else:
            server = smtplib.SMTP(config['server'], config['port'])
            if config['use_tls']:
                server.starttls()
        
        print("  ✅ Connexion réussie")
        
        # Login
        server.login('contact.fkcorporate@gmail.com', password)
        print("  ✅ Authentification réussie")
        
        # Créer l'email
        msg = MIMEMultipart()
        msg['From'] = 'contact.fkcorporate@gmail.com'
        msg['To'] = 'contact.fkcorporate@gmail.com'
        msg['Subject'] = f"Test SMTP - {config['name']}"
        
        body = f"Ceci est un test de l'envoi d'email avec {config['name']}"
        msg.attach(MIMEText(body, 'plain'))
        
        # Envoyer
        server.send_message(msg)
        print("  📧 Email envoyé avec succès !")
        
        server.quit()
        print(f"  🎉 {config['name']} : TOUT FONCTIONNE !")
        
    except Exception as e:
        print(f"  ❌ Erreur: {type(e).__name__}: {str(e)[:100]}")

print("\n" + "="*50)
print("Si tous les tests échouent :")
print("1. Vérifiez que la validation en 2 étapes est activée")
print("2. Générez un NOUVEAU mot de passe d'application :")
print("   https://myaccount.google.com/apppasswords")
print("3. Utilisez le nouveau mot de passe")