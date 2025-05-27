"""
CLIENT API MISTRAL AI
Gestion des appels à l'API Mistral pour le chatbot pédagogique

Fonctionnalités :
- Appels sécurisés à l'API Mistral
- Gestion des erreurs et retry
- Optimisation des paramètres
- Cache des réponses fréquentes
"""

import requests
import json
import time
import logging
from typing import Optional, List, Dict, Any
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class MistralResponse:
    """Structure de réponse de l'API Mistral"""
    content: str
    usage: Dict[str, int]
    model: str
    success: bool = True
    error: Optional[str] = None

class MistralClient:
    """Client pour l'API Mistral AI"""
    
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.mistral.ai/v1"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        })
        
        # Cache simple pour éviter les appels répétés
        self.cache = {}
        self.cache_max_size = 100
        
        # Configuration par défaut
        self.default_model = "mistral-small"
        self.default_temperature = 0.5
        self.default_max_tokens = 500
        
        # Gestion des limites de taux
        self.last_request_time = 0
        self.min_request_interval = 0.1  # 100ms entre les requêtes
        
    def generate_response(
        self, 
        prompt: str, 
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None,
        system_prompt: Optional[str] = None
    ) -> Optional[str]:
        """
        Génère une réponse via l'API Mistral
        
        Args:
            prompt: Le prompt utilisateur
            model: Modèle à utiliser (défaut: mistral-small)
            temperature: Créativité (0.0-1.0)
            max_tokens: Longueur max de la réponse
            system_prompt: Instructions système
            
        Returns:
            La réponse générée ou None en cas d'erreur
        """
        try:
            # Vérification du cache
            cache_key = self._get_cache_key(prompt, model, temperature, max_tokens)
            if cache_key in self.cache:
                logger.info("🎯 Réponse trouvée en cache")
                return self.cache[cache_key]
            
            # Construction des messages
            messages = []
            if system_prompt:
                messages.append({"role": "system", "content": system_prompt})
            messages.append({"role": "user", "content": prompt})
            
            # Paramètres de la requête
            payload = {
                "model": model or self.default_model,
                "messages": messages,
                "temperature": temperature or self.default_temperature,
                "max_tokens": max_tokens or self.default_max_tokens
            }
            
            # Gestion du taux de requêtes
            self._rate_limit()
            
            # Appel à l'API
            response = self._make_request("/chat/completions", payload)
            
            if response and response.success:
                # Mise en cache
                self._cache_response(cache_key, response.content)
                return response.content
            else:
                logger.error(f"❌ Erreur API Mistral: {response.error if response else 'Pas de réponse'}")
                return None
                
        except Exception as e:
            logger.error(f"❌ Exception dans generate_response: {e}")
            return None
    
    def generate_conversation_response(
        self, 
        messages: List[Dict[str, str]], 
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_tokens: Optional[int] = None
    ) -> Optional[str]:
        """
        Génère une réponse dans le contexte d'une conversation
        
        Args:
            messages: Historique de la conversation
            model: Modèle à utiliser
            temperature: Créativité
            max_tokens: Longueur max
            
        Returns:
            La réponse générée
        """
        try:
            payload = {
                "model": model or self.default_model,
                "messages": messages,
                "temperature": temperature or self.default_temperature,
                "max_tokens": max_tokens or self.default_max_tokens
            }
            
            self._rate_limit()
            response = self._make_request("/chat/completions", payload)
            
            return response.content if response and response.success else None
            
        except Exception as e:
            logger.error(f"❌ Erreur génération conversation: {e}")
            return None
    
    def test_connection(self) -> bool:
        """
        Test de connexion à l'API Mistral
        
        Returns:
            True si la connexion fonctionne
        """
        try:
            test_response = self.generate_response(
                prompt="Test de connexion. Réponds juste 'OK'.",
                max_tokens=10,
                temperature=0.1
            )
            
            success = test_response is not None and len(test_response.strip()) > 0
            logger.info(f"🔍 Test connexion Mistral: {'✅ OK' if success else '❌ FAILED'}")
            return success
            
        except Exception as e:
            logger.error(f"❌ Test connexion échoué: {e}")
            return False
    
    def get_available_models(self) -> List[str]:
        """
        Récupère la liste des modèles disponibles
        
        Returns:
            Liste des modèles disponibles
        """
        try:
            response = self._make_request("/models", method="GET")
            if response and response.success:
                # Parse de la réponse pour extraire les noms de modèles
                models_data = json.loads(response.content)
                return [model["id"] for model in models_data.get("data", [])]
            return ["mistral-tiny", "mistral-small", "mistral-medium"]  # Fallback
        except Exception as e:
            logger.error(f"❌ Erreur récupération modèles: {e}")
            return ["mistral-tiny", "mistral-small", "mistral-medium"]
    
    def _make_request(self, endpoint: str, payload: Optional[Dict] = None, method: str = "POST") -> Optional[MistralResponse]:
        """
        Effectue une requête HTTP à l'API Mistral
        
        Args:
            endpoint: Point de terminaison de l'API
            payload: Données à envoyer
            method: Méthode HTTP
            
        Returns:
            Réponse formatée ou None
        """
        url = f"{self.base_url}{endpoint}"
        
        try:
            if method.upper() == "GET":
                response = self.session.get(url, timeout=30)
            else:
                response = self.session.post(url, json=payload, timeout=30)
            
            response.raise_for_status()
            
            data = response.json()
            
            # Extraction du contenu selon le type de réponse
            if "choices" in data and len(data["choices"]) > 0:
                content = data["choices"][0]["message"]["content"]
                usage = data.get("usage", {})
                model = data.get("model", "unknown")
                
                return MistralResponse(
                    content=content,
                    usage=usage,
                    model=model,
                    success=True
                )
            else:
                return MistralResponse(
                    content=json.dumps(data),
                    usage={},
                    model="unknown",
                    success=True
                )
                
        except requests.exceptions.HTTPError as e:
            error_msg = f"Erreur HTTP {e.response.status_code}"
            if e.response.status_code == 401:
                error_msg = "Clé API invalide"
            elif e.response.status_code == 429:
                error_msg = "Limite de taux atteinte"
            elif e.response.status_code == 500:
                error_msg = "Erreur serveur Mistral"
                
            logger.error(f"❌ {error_msg}: {e}")
            return MistralResponse("", {}, "", False, error_msg)
            
        except requests.exceptions.Timeout:
            error_msg = "Timeout de la requête"
            logger.error(f"❌ {error_msg}")
            return MistralResponse("", {}, "", False, error_msg)
            
        except Exception as e:
            error_msg = f"Erreur requête: {str(e)}"
            logger.error(f"❌ {error_msg}")
            return MistralResponse("", {}, "", False, error_msg)
    
    def _rate_limit(self):
        """Gestion du taux de requêtes"""
        now = time.time()
        elapsed = now - self.last_request_time
        
        if elapsed < self.min_request_interval:
            sleep_time = self.min_request_interval - elapsed
            time.sleep(sleep_time)
        
        self.last_request_time = time.time()
    
    def _get_cache_key(self, prompt: str, model: Optional[str], temperature: Optional[float], max_tokens: Optional[int]) -> str:
        """Génère une clé de cache pour la requête"""
        key_data = {
            "prompt": prompt[:100],  # Premiers 100 caractères
            "model": model or self.default_model,
            "temperature": temperature or self.default_temperature,
            "max_tokens": max_tokens or self.default_max_tokens
        }
        return hash(json.dumps(key_data, sort_keys=True))
    
    def _cache_response(self, key: str, response: str):
        """Met en cache une réponse"""
        if len(self.cache) >= self.cache_max_size:
            # Supprime le plus ancien (FIFO simple)
            oldest_key = next(iter(self.cache))
            del self.cache[oldest_key]
        
        self.cache[key] = response
    
    def clear_cache(self):
        """Vide le cache"""
        self.cache.clear()
        logger.info("🗑️ Cache vidé")
    
    def get_cache_stats(self) -> Dict[str, Any]:
        """Statistiques du cache"""
        return {
            "size": len(self.cache),
            "max_size": self.cache_max_size,
            "hit_rate": getattr(self, '_cache_hits', 0) / max(getattr(self, '_cache_requests', 1), 1)
        }


# Classe utilitaire pour la gestion des prompts éducatifs
class EducationalPromptBuilder:
    """Constructeur de prompts spécialisés pour l'éducation"""
    
    @staticmethod
    def create_explanation_prompt(concept: str, level: str, context: str = "") -> str:
        """Crée un prompt pour expliquer un concept"""
        level_instructions = {
            "beginner": "Utilise des analogies simples et évite le jargon technique.",
            "intermediate": "Donne des détails techniques modérés avec des exemples concrets.",
            "advanced": "Fournis des explications techniques approfondies avec des détails mathématiques si nécessaire."
        }
        
        return f"""Tu es un assistant pédagogique spécialisé en Deep Learning.

Explique le concept de '{concept}' à un étudiant de niveau {level}.

Instructions spécifiques pour ce niveau :
{level_instructions.get(level, level_instructions['intermediate'])}

{f"Contexte de la conversation : {context}" if context else ""}

Structure ta réponse ainsi :
1. Définition claire et concise
2. Exemple pratique ou analogie
3. Application concrète en informatique
4. Lien avec d'autres concepts si pertinent

Réponds de manière engageante et pédagogique."""

    @staticmethod
    def create_quiz_generation_prompt(topic: str, difficulty: str, count: int) -> str:
        """Crée un prompt pour générer un quiz"""
        return f"""Génère un quiz de {count} questions sur le sujet "{topic}" avec un niveau de difficulté {difficulty}.

Format JSON EXACT à respecter :
{{
    "title": "Quiz : {topic}",
    "questions": [
        {{
            "id": 1,
            "question": "Question claire et précise ?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correctAnswer": 0,
            "explanation": "Explication pédagogique de pourquoi cette réponse est correcte",
            "difficulty": "{difficulty}"
        }}
    ]
}}

Critères pour le niveau {difficulty} :
- beginner: Concepts de base, analogies simples
- intermediate: Applications pratiques, exemples concrets  
- advanced: Détails techniques, optimisations, cas complexes

Assure-toi que :
- Chaque question a exactement 4 options
- Une seule option est correcte
- L'explication est pédagogique et utile
- Les questions progressent logiquement"""


# Instance de test pour validation
if __name__ == "__main__":
    # Test basique du client (nécessite une vraie clé API)
    import os
    
    api_key = os.getenv("MISTRAL_API_KEY", "test_key")
    client = MistralClient(api_key)
    
    print("🧪 Test du client Mistral...")
    
    if api_key != "test_key":
        # Test avec vraie clé
        success = client.test_connection()
        print(f"Connexion: {'✅' if success else '❌'}")
        
        if success:
            response = client.generate_response(
                "Explique brièvement ce qu'est un neurone artificiel.",
                temperature=0.3,
                max_tokens=100
            )
            print(f"Réponse test: {response[:100] if response else 'Aucune'}...")
    else:
        print("⚠️ Clé API manquante pour test complet")
    
    print("✅ Tests terminés")