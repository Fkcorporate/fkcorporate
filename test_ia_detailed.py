# test_ia_detailed.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app, service_ia
from models import Audit, AnalyseIA
from app import db

def test_ia_complet():
    """Test complet du service IA"""
    
    with app.app_context():
        print("🔍 TEST COMPLET SERVICE IA")
        print("=" * 50)
        
        # 1. Vérifier la configuration
        print("\n1. 📋 CONFIGURATION:")
        print(f"   - Mode simulation: {service_ia.mode_simulation}")
        print(f"   - Client OpenAI: {'✅ Initialisé' if service_ia.client else '❌ Non initialisé'}")
        print(f"   - API Key: {'✅ Présente' if os.environ.get('OPENAI_API_KEY') else '❌ Absente'}")
        
        # 2. Chercher un audit existant
        print("\n2. 🔍 RECHERCHE AUDIT:")
        audit = Audit.query.first()
        if audit:
            print(f"   - Audit trouvé: {audit.reference} - {audit.titre}")
            print(f"   - ID: {audit.id}")
            print(f"   - Constatations: {len(audit.constatations) if hasattr(audit, 'constatations') else 'N/A'}")
        else:
            print("   ❌ Aucun audit trouvé dans la base")
            return
        
        # 3. Tester l'analyse IA
        print("\n3. 🧪 TEST ANALYSE IA:")
        try:
            resultat = service_ia.analyser_audit(
                audit_id=audit.id,
                type_analyse='complet',
                user_id=1
            )
            
            # Convertir en dict
            if hasattr(resultat, 'to_dict'):
                data = resultat.to_dict()
            elif hasattr(resultat, 'resultat'):
                data = resultat.resultat
                if isinstance(data, str):
                    try:
                        import json
                        data = json.loads(data)
                    except:
                        data = {'raw': data}
            else:
                data = resultat
            
            print(f"   ✅ Analyse réussie")
            print(f"   - Type résultat: {type(resultat).__name__}")
            print(f"   - Recommandations: {len(data.get('recommandations_ia', []))}")
            print(f"   - Causes racines: {len(data.get('causes_racines', []))}")
            print(f"   - Score confiance: {data.get('metadata', {}).get('score_confiance', 'N/A')}")
            
            # Afficher un aperçu
            if data.get('recommandations_ia'):
                print(f"\n   📋 APERÇU RECOMMANDATIONS:")
                for i, reco in enumerate(data['recommandations_ia'][:2], 1):
                    print(f"      {i}. {reco.get('titre', 'Sans titre')[:50]}...")
            
        except Exception as e:
            print(f"   ❌ Erreur analyse: {e}")
            import traceback
            traceback.print_exc()
        
        # 4. Vérifier les analyses existantes
        print("\n4. 📊 ANALYSES EXISTANTES:")
        analyses = AnalyseIA.query.filter_by(audit_id=audit.id).all()
        print(f"   - Analyses en base: {len(analyses)}")
        
        for analyse in analyses[:3]:  # Afficher les 3 premières
            print(f"      • ID {analyse.id}: {analyse.type_analyse} - Score: {analyse.score_confiance}%")
        
        print("\n" + "=" * 50)
        print("✅ Test terminé")

if __name__ == "__main__":
    test_ia_complet()