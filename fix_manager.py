from app import app, db
from models import User

with app.app_context():
    # Trouver tous les managers
    managers = User.query.filter_by(role='manager').all()
    
    for manager in managers:
        print(f"🔧 Correction pour {manager.username}")
        
        # Activer le flag
        manager.can_manage_users = True
        
        # Initialiser permissions si nécessaire
        if manager.permissions is None:
            manager.permissions = {}
        
        # Mettre à jour les permissions spécifiques
        manager.permissions.update({
            'can_create_users': True,
            'can_edit_users': True,
            'can_deactivate_users': True,
            'can_delete_users': True,
            'can_manage_users': True,
            'can_manage_permissions': True,
            'can_view_users_list': True
        })
    
    db.session.commit()
    print(f"✅ {len(managers)} gestionnaires corrigés")