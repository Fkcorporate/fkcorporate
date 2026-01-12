#!/usr/bin/env python3
"""
Script d'initialisation de l'application
Crée les dossiers nécessaires et initialise la base de données
"""

import os
import sys
from config import Config

def init_application():
    """Initialise l'application"""
    print("🔧 Initialisation de l'application...")
    
    try:
        # 1. Créer les dossiers d'upload
        print("📁 Création des dossiers d'upload...")
        Config.ensure_upload_folders()
        
        # 2. Vérifier les variables d'environnement
        print("🔍 Vérification des variables d'environnement...")
        
        required_vars = ['SECRET_KEY']
        missing_vars = []
        
        for var in required_vars:
            if not os.environ.get(var):
                missing_vars.append(var)
        
        if missing_vars:
            print(f"⚠️ Variables manquantes: {', '.join(missing_vars)}")
            print("ℹ️ Création d'un fichier .env avec des valeurs par défaut...")
            
            # Créer un fichier .env s'il n'existe pas
            if not os.path.exists('.env'):
                with open('.env', 'w') as f:
                    f.write(f"# Configuration Application Audit\n")
                    f.write(f"SECRET_KEY={Config.SECRET_KEY}\n")
                    f.write(f"FLASK_ENV=development\n")
                    f.write(f"FLASK_APP=app.py\n")
                    f.write(f"DATABASE_URL={Config.SQLALCHEMY_DATABASE_URI}\n")
                print("✅ Fichier .env créé")
        
        # 3. Vérifier les dépendances
        print("📦 Vérification des dépendances...")
        try:
            import flask
            import flask_sqlalchemy
            import flask_login
            import flask_wtf
            import werkzeug
            print("✅ Toutes les dépendances sont installées")
        except ImportError as e:
            print(f"❌ Dépendance manquante: {e}")
            print("💡 Exécutez: pip install -r requirements.txt")
            return False
        
        # 4. Créer la base de données
        print("🗄️  Initialisation de la base de données...")
        from app import app, db
        with app.app_context():
            db.create_all()
            print("✅ Base de données initialisée")
            
            # 5. Vérifier l'utilisateur admin
            from models import User
            admin = User.query.filter_by(username='admin').first()
            if not admin:
                print("👤 Création de l'utilisateur admin...")
                admin = User(
                    username='admin',
                    email='admin@entreprise.com',
                    role='admin',
                    department='Direction Générale',
                    is_active=True
                )
                admin.set_password('admin123')
                db.session.add(admin)
                db.session.commit()
                print("✅ Admin créé: admin / admin123")
                print("⚠️  CHANGEZ CE MOT DE PASSE IMMÉDIATEMENT !")
            else:
                print("✅ Admin existe déjà")
        
        print("🎉 Initialisation terminée avec succès !")
        print("\n📋 Prochaines étapes:")
        print("1. Modifiez le fichier .env avec vos valeurs réelles")
        print("2. Changez le mot de passe admin")
        print("3. Lancez l'application: python app.py")
        print("4. Accédez à http://localhost:5000")
        
        return True
        
    except Exception as e:
        print(f"❌ Erreur lors de l'initialisation: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = init_application()
    sys.exit(0 if success else 1)