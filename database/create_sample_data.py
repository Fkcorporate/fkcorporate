from app import app, db
from models import User, Direction, Service

def create_sample_data():
    with app.app_context():
        print("Création des données de démonstration...")
        
        # Vérifier si des données existent déjà
        if Direction.query.first():
            print("⚠️  Des données existent déjà. Arrêt.")
            return
        
        # Créer des directions
        directions = [
            Direction(nom='Direction Générale', description='Direction principale de l\'entreprise'),
            Direction(nom='Direction Financière', description='Direction des finances et de la comptabilité'),
            Direction(nom='Direction des Ressources Humaines', description='Direction RH et développement des talents'),
            Direction(nom='Direction Technique', description='Direction technique et opérationnelle'),
        ]
        
        for direction in directions:
            db.session.add(direction)
        
        db.session.commit()
        print("✅ 4 directions créées")
        
        # Créer des services
        services = [
            Service(nom='Service Comptabilité', direction_id=2, description='Gestion comptable et financière'),
            Service(nom='Service Contrôle de Gestion', direction_id=2, description='Analyse et contrôle budgétaire'),
            Service(nom='Service Recrutement', direction_id=3, description='Recrutement et intégration'),
            Service(nom='Service Formation', direction_id=3, description='Développement des compétences'),
            Service(nom='Service Informatique', direction_id=4, description='Support et développement IT'),
            Service(nom='Service Production', direction_id=4, description='Gestion de la production'),
        ]
        
        for service in services:
            db.session.add(service)
        
        db.session.commit()
        print("✅ 6 services créés")
        
        print("\n🎉 Données de démonstration créées avec succès!")
        print("\n📋 Vous pouvez maintenant :")
        print("1. Créer des cartographies")
        print("2. Créer des processus")
        print("3. Ajouter des risques")
        print("4. Utiliser l'application complètement")

if __name__ == '__main__':
    create_sample_data()
