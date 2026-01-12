from app import app, db
from models import User, Direction, Service

def init_database():
    with app.app_context():
        # Créer toutes les tables
        db.create_all()
        
        # Créer des données de test
        if not User.query.first():
            # Créer l'admin
            admin = User(
                username='admin',
                email='admin@entreprise.com',
                role='admin',
                department='Direction Générale'
            )
            admin.set_password('admin123')
            db.session.add(admin)
            
            # Créer des directions de test
            directions = [
                Direction(nom='Direction Générale', description='Direction principale'),
                Direction(nom='Direction Financière', description='Direction des finances'),
                Direction(nom='Direction des Ressources Humaines', description='Direction RH'),
                Direction(nom='Direction Technique', description='Direction technique et opérationnelle')
            ]
            
            for direction in directions:
                db.session.add(direction)
            
            db.session.commit()
            
            print("Base de données initialisée avec succès!")
            print("Compte admin créé: admin / admin123")

if __name__ == '__main__':
    init_database()
