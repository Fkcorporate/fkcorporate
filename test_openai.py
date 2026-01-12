# test_openai.py - Version compatible OpenAI v1.0.0+
import os
import sys
from datetime import datetime
from openai import OpenAI, APIError, AuthenticationError, RateLimitError

def test_openai_connection():
    """Tester la connexion à l'API OpenAI (v1.0.0+)"""
    
    api_key = os.environ.get("OPENAI_API_KEY")
    
    print(f"🔍 Clé API détectée: {'Oui' if api_key else 'Non'}")
    
    if not api_key or api_key == "mode-simulation":
        print("🔧 Mode simulation activé - pas d'appel réel à l'API")
        return {
            "status": "simulation",
            "timestamp": datetime.now().isoformat(),
            "message": "Clé non définie ou mode simulation"
        }
    
    try:
        # Initialiser le client avec la nouvelle API
        client = OpenAI(api_key=api_key)
        
        # Petit test simple et peu coûteux
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Vous êtes un assistant utile."},
                {"role": "user", "content": "Répondez uniquement par 'TEST_OK' si vous recevez ce message."}
            ],
            max_tokens=10,
            temperature=0
        )
        
        message_content = response.choices[0].message.content
        
        print(f"✅ Connexion API réussie")
        print(f"📊 Réponse: {message_content}")
        print(f"📈 Tokens utilisés: {response.usage.total_tokens}")
        print(f"🔢 ID de la requête: {response.id}")
        
        return {
            "status": "success",
            "tokens": response.usage.total_tokens,
            "response": message_content,
            "model": response.model,
            "request_id": response.id
        }
        
    except AuthenticationError:
        print("❌ Erreur d'authentification : clé API invalide ou expirée")
        print("   Vérifiez sur: https://platform.openai.com/api-keys")
        return {"status": "auth_error"}
    
    except RateLimitError:
        print("❌ Limite de taux atteinte. Attendez quelques minutes.")
        return {"status": "rate_limit"}
    
    except APIError as e:
        print(f"❌ Erreur API OpenAI: {e}")
        return {"status": "api_error", "message": str(e)}
    
    except Exception as e:
        print(f"❌ Erreur inattendue: {type(e).__name__}: {e}")
        return {"status": "error", "message": str(e)}

def verifier_version_openai():
    """Vérifier la version installée d'OpenAI"""
    try:
        import openai
        import pkg_resources
        
        version = pkg_resources.get_distribution("openai").version
        print(f"📦 Version OpenAI installée: {version}")
        
        # Vérifier si c'est la nouvelle API
        if version.startswith("0."):
            print("⚠️ Vous utilisez l'ancienne API (<1.0.0)")
            print("   Considérez la mise à jour: pip install --upgrade openai")
            return "old"
        else:
            print("✅ Vous utilisez la nouvelle API (>=1.0.0)")
            return "new"
            
    except Exception as e:
        print(f"❌ Impossible de vérifier la version: {e}")
        return "unknown"

if __name__ == "__main__":
    print("=" * 50)
    print("🧪 TEST DE CONNEXION OPENAI v1.0.0+")
    print("=" * 50)
    
    # Vérifier la version
    version = verifier_version_openai()
    
    print("\n🔑 Test de connexion...")
    result = test_openai_connection()
    
    print("\n" + "=" * 50)
    print("📋 RÉSULTAT DU TEST")
    print("=" * 50)
    
    for key, value in result.items():
        print(f"  {key}: {value}")