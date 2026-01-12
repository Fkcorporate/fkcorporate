import sqlite3
import json

def find_and_fix():
    conn = sqlite3.connect('instance/app.db')
    cursor = conn.cursor()
    
    print("🔍 Recherche des tables...")
    
    # 1. Voir toutes les tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    
    print("📋 Tables disponibles:")
    for table in tables:
        print(f"  - {table[0]}")
    
    # 2. Chercher une table contenant "formule" ou "abonnement"
    formule_tables = []
    for table in tables:
        if 'formule' in table[0].lower() or 'abonnement' in table[0].lower():
            formule_tables.append(table[0])
    
    if formule_tables:
        print(f"\n✅ Table(s) trouvée(s): {formule_tables}")
        
        for table_name in formule_tables:
            print(f"\n📊 Inspection de '{table_name}':")
            
            # Voir la structure
            cursor.execute(f"PRAGMA table_info({table_name})")
            columns = cursor.fetchall()
            print("  Colonnes:")
            for col in columns:
                print(f"    - {col[1]} ({col[2]})")
            
            # Voir le contenu
            cursor.execute(f"SELECT * FROM {table_name}")
            rows = cursor.fetchall()
            print(f"  Lignes: {len(rows)}")
            
            # Chercher la formule enterprise
            for row in rows:
                if len(row) > 2 and ('enterprise' in str(row) or 'Enterprise' in str(row)):
                    print(f"\n  📍 Formule Enterprise trouvée:")
                    for i, col in enumerate(columns):
                        if i < len(row):
                            print(f"    {col[1]}: {row[i]}")
    
    else:
        print("\n❌ Aucune table 'formule_abonnement' trouvée !")
        
        # Chercher dans toutes les tables
        print("\n🔍 Recherche dans toutes les tables...")
        for table in tables:
            print(f"\n  Table: {table[0]}")
            try:
                cursor.execute(f"SELECT * FROM {table[0]} LIMIT 1")
                cols = [description[0] for description in cursor.description]
                print(f"    Colonnes: {', '.join(cols)}")
                
                # Voir quelques lignes
                cursor.execute(f"SELECT * FROM {table[0]} LIMIT 3")
                rows = cursor.fetchall()
                for row in rows:
                    print(f"    Ligne: {row}")
            except:
                continue
    
    conn.close()

if __name__ == "__main__":
    find_and_fix()