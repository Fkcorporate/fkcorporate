# test_service_ia.py
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

print("🧪 TEST DU SERVICE IA")
print("=" * 50)

# Test 1: Vérifier les imports
try:
    from services.analyse_ia import ServiceAnalyseIA
    print("✅ Import ServiceAnalyseIA réussi")
except IndentationError as e:
    print(f"❌ Erreur d'indentation: {e}")
    print("Corrigez l'indentation dans services/analyse_ia.py")
    sys.exit(1)
except Exception as e:
    print(f"❌ Erreur import: {e}")
    sys.exit(1)

# Test 2: Créer une instance
try:
    service = ServiceAnalyseIA()
    statut = service.get_statut()
    
    print(f"\n📊 STATUT SERVICE:")
    print(f"  Mode: {statut['mode']}")
    print(f"  Erreur quota: {statut['quota_error']}")
    print(f"  Clé API: {'✅ Présente' if statut['api_key_presente'] else '❌ Absente'}")
    print(f"  Client: {'✅ Initialisé' if statut['client_initialise'] else '❌ Non initialisé'}")
    
    # Test 3: Simuler une analyse
    print("\n🧪 TEST ANALYSE SIMULATION:")
    resultat = service.analyser_audit(1, 'test', 1)
    
    print(f"  Type résultat: {type(resultat).__name__}")
    print(f"  Recommandations: {len(resultat.get('recommandations_ia', []))}")
    print(f"  Causes racines: {len(resultat.get('causes_racines', []))}")
    print(f"  Score global: {resultat.get('statistiques', {}).get('score_global', 'N/A')}")
    
    # Afficher les recommandations
    if resultat.get('recommandations_ia'):
        print(f"\n  📋 RECOMMANDATIONS:")
        for reco in resultat['recommandations_ia'][:3]:
            print(f"    • {reco.get('titre', 'Sans titre')}")
    
    print("\n✅ Test terminé avec succès!")
    
except Exception as e:
    print(f"\n❌ Erreur: {e}")
    import traceback
    traceback.print_exc()