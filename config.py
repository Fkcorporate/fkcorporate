import os
from datetime import timedelta
from dotenv import load_dotenv

# Charger les variables d'environnement depuis .env
load_dotenv()

class Config:
    # ============================================================================
    # CONFIGURATIONS DE BASE
    # ============================================================================
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'votre_cle_secrete_super_securisee_changer_en_production'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///controle_interne.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=1)
    
    # ============================================================================
    # CONFIGURATIONS DES UPLOADS
    # ============================================================================
    UPLOAD_FOLDER = 'uploads'
    UPLOAD_FOLDER_AUDIT = 'uploads/audits'
    UPLOAD_FOLDER_CONSTATATIONS = 'uploads/constatations'
    UPLOAD_FOLDER_RECOMMANDATIONS = 'uploads/recommandations'
    UPLOAD_FOLDER_PLANS = 'uploads/plans_action'
    UPLOAD_FOLDER_VEILLE = 'static/uploads/veille'
    UPLOAD_FOLDER_RISQUES = 'uploads/risques'
    
    # Extensions autorisées
    ALLOWED_EXTENSIONS = {
        'pdf', 'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff',
        'doc', 'docx', 'xls', 'xlsx', 'ppt', 'pptx', 'txt',
        'csv', 'json', 'xml', 'zip', 'rar', '7z'
    }
    
    # Taille maximale des fichiers (16MB)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024
    
    # ============================================================================
    # CONFIGURATION EMAIL (POUR NOTIFICATIONS)
    # ============================================================================
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.gmail.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT', 587))
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', '1', 't']
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', 'False').lower() in ['true', '1', 't']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME', 'contact.fkcorporate@gmail.com')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD', '')
    MAIL_DEFAULT_SENDER = ('FK Corporate Intelligence', 'contact.fkcorporate@gmail.com')
    
    # ============================================================================
    # CONFIGURATIONS AUDIT - STATUTS INTELLIGENTS
    # ============================================================================
    AUDIT_STATUTS = [
        ('planifie', 'Planifié'),
        ('en_preparation', 'En préparation'),
        ('en_collecte', 'En collecte'),
        ('en_analyse', 'En analyse'),
        ('en_redaction', 'En rédaction du rapport'),
        ('en_validation', 'En validation'),
        ('clos', 'Clos'),
        ('archive', 'Archivé')
    ]
    
    # ============================================================================
    # CONFIGURATIONS CONSTATATION - WORKFLOW ET CLASSIFICATION
    # ============================================================================
    CONSTATATION_TYPES = [
        ('non_conformite', 'Non-conformité'),
        ('observation', 'Observation'),
        ('opportunite_amelioration', 'Opportunité d\'amélioration'),
        ('conforme', 'Conforme'),
        ('point_fort', 'Point fort')
    ]
    
    CONSTATATION_GRAVITE = [
        ('mineure', 'Mineure'),
        ('moyenne', 'Moyenne'),
        ('majeure', 'Majeure'),
        ('critique', 'Critique')
    ]
    
    CONSTATATION_CRITICITE = [
        ('mineure', 'Mineure'),
        ('majeure', 'Majeure'),
        ('critique', 'Critique')
    ]
    
    # ============================================================================
    # CONFIGURATIONS RECOMMANDATION - TYPOLOGIE ET PRIORISATION
    # ============================================================================
    RECOMMANDATION_TYPES = [
        ('corrective', 'Corrective'),
        ('preventive', 'Préventive'),
        ('amelioration', 'Amélioration'),
        ('optimisation', 'Optimisation')
    ]
    
    RECOMMANDATION_CATEGORIES = [
        ('conformite_reglementaire', 'Conformité réglementaire'),
        ('amelioration_continue', 'Amélioration continue'),
        ('reduction_risque', 'Réduction de risque'),
        ('optimisation_processus', 'Optimisation de processus'),
        ('securite_controle_interne', 'Sécurité / Contrôle interne')
    ]
    
    # ============================================================================
    # CONFIGURATIONS PLAN D'ACTION
    # ============================================================================
    PLAN_ACTION_STATUTS = [
        ('en_attente', 'En attente'),
        ('en_cours', 'En cours'),
        ('termine', 'Terminé'),
        ('retarde', 'Retardé'),
        ('suspendu', 'Suspendu')
    ]
    
    # ============================================================================
    # CONFIGURATIONS ALERTES AUTOMATIQUES
    # ============================================================================
    ALERTE_7J_AVANT_ECHEANCE = True
    ALERTE_ECHEANCE_ATTEINTE = True
    ALERTE_RETARD = True
    
    # ============================================================================
    # CONFIGURATIONS EXPORTS
    # ============================================================================
    EXPORT_LOGO_PATH = 'static/images/logo_entreprise.png'
    EXPORT_SIGNATURE_ENABLED = True
    
    # ============================================================================
    # MÉTHODES UTILITAIRES
    # ============================================================================
    
    @staticmethod
    def ensure_upload_folders():
        """Crée tous les dossiers d'upload s'ils n'existent pas"""
        folders = [
            Config.UPLOAD_FOLDER,
            Config.UPLOAD_FOLDER_AUDIT,
            Config.UPLOAD_FOLDER_CONSTATATIONS,
            Config.UPLOAD_FOLDER_RECOMMANDATIONS,
            Config.UPLOAD_FOLDER_PLANS,
            Config.UPLOAD_FOLDER_VEILLE,
            Config.UPLOAD_FOLDER_RISQUES
        ]
        
        for folder in folders:
            if not os.path.exists(folder):
                os.makedirs(folder, exist_ok=True)
    
    @staticmethod
    def print_config_summary():
        """Affiche un résumé de la configuration (sans les mots de passe)"""
        print("\n" + "="*60)
        print("📋 RÉSUMÉ DE LA CONFIGURATION")
        print("="*60)
        print(f"SECRET_KEY: {'✅ Définie' if Config.SECRET_KEY else '❌ Non définie'}")
        print(f"DATABASE: {Config.SQLALCHEMY_DATABASE_URI}")
        print(f"MAIL_SERVER: {Config.MAIL_SERVER}")
        print(f"MAIL_PORT: {Config.MAIL_PORT}")
        print(f"MAIL_USERNAME: {Config.MAIL_USERNAME}")
        print(f"MAIL_PASSWORD: {'✅ Définie' if Config.MAIL_PASSWORD else '❌ Non définie'}")
        print(f"MAIL_DEFAULT_SENDER: {Config.MAIL_DEFAULT_SENDER}")
        print("="*60)
