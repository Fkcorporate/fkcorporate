# init_database.py
import os
import sys
import json
from werkzeug.security import generate_password_hash

# Ajouter le chemin du projet
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(current_dir)

# Importer SQLAlchemy directement sans les modèles complexes
from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy

print("🔄 Initialisation de la base de données...")

# Créer une application minimale
temp_app = Flask(__name__)
temp_app.config.from_object(Config)

# Initialiser la base de données
db = SQLAlchemy(temp_app)

# Définir un modèle User simplifié
class User(db.Model):
    __tablename__ = 'user'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='utilisateur')
    department = db.Column(db.String(100))
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=db.func.now())
    last_login = db.Column(db.DateTime)
    permissions = db.Column(db.Text, default='{}')  # Stocké comme texte JSON

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

with temp_app.app_context():
    try:
        # Créer toutes les tables
        db.create_all()
        print("✅ Tables créées")
        
        # Vérifier si l'admin existe
        if not User.query.first():
            # Permissions admin complètes
            admin_permissions = {
                'can_view_dashboard': True,
                'can_manage_risks': True,
                'can_manage_kri': True,
                'can_manage_audit': True,
                'can_manage_regulatory': True,
                'can_manage_logigram': True,
                'can_manage_users': True,
                'can_manage_settings': True,
                'can_export_data': True,
                'can_view_reports': True,
                'can_delete_data': True,
                'can_manage_permissions': True,
                'can_access_all_departments': True,
                'can_archive_data': True,
                'can_validate_risks': True,
                'can_confirm_evaluations': True
            }
            
            admin = User(
                username='admin',
                email='admin@entreprise.com',
                role='admin',
                department='Direction Générale',
                permissions=json.dumps(admin_permissions)
            )
            admin.set_password('admin123')
            db.session.add(admin)
            db.session.commit()
            print("✅ Admin créé: admin / admin123")
        else:
            print("✅ L'admin existe déjà")
            
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()