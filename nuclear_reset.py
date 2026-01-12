# nuclear_reset.py
import os
import sys
import shutil

print("💣 APPROCHE NUCLÉAIRE - RECONSTRUCTION COMPLÈTE")
print("="*60)

# 1. Supprimer toute la base
files_to_nuke = [
    'instance',
    '__pycache__',
    'migrations',
    '*.pyc',
    '*.pyo',
    'fabricekonan.db',
    'fabricekonan.db.backup'
]

for item in files_to_nuke:
    if os.path.exists(item):
        if os.path.isdir(item):
            shutil.rmtree(item)
            print(f"🗑️ Dossier supprimé: {item}")
        else:
            os.remove(item)
            print(f"🗑️ Fichier supprimé: {item}")

# 2. Recréer les dossiers essentiels
os.makedirs('instance', exist_ok=True)

# 3. Créer une base SQLite brute
import sqlite3
conn = sqlite3.connect('instance/fabricekonan.db')
cursor = conn.cursor()

# Table user ultra simple
cursor.execute("""
    CREATE TABLE user (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username VARCHAR(80) UNIQUE NOT NULL,
        email VARCHAR(120) UNIQUE NOT NULL,
        password_hash VARCHAR(128),
        role VARCHAR(20) DEFAULT 'utilisateur',
        department VARCHAR(100),
        is_active BOOLEAN DEFAULT TRUE,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
        last_login DATETIME,
        client_id INTEGER DEFAULT 1,
        is_client_admin BOOLEAN DEFAULT FALSE,
        permissions TEXT DEFAULT '{}',
        preferences_notifications TEXT DEFAULT '{}'
    )
""")

# Insérer admin
from werkzeug.security import generate_password_hash
cursor.execute("""
    INSERT INTO user (username, email, password_hash, role, client_id, is_client_admin)
    VALUES (?, ?, ?, ?, ?, ?)
""", (
    'admin',
    'admin@entreprise.com',
    generate_password_hash('admin123'),
    'super_admin',
    1,
    1
))

conn.commit()
conn.close()

print("✅ Base recréée avec succès")
print("\n🔗 http://localhost:5000")
print("👑 admin / admin123")