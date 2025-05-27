"""
TESTS DE SCÉNARIOS - CHATBOT PÉDAGOGIQUE
Tests automatisés basés sur des scénarios réels d'utilisation

Tests couverts :
- Scénarios éducatifs par niveau
- Gestion des conversations contextuelles
- Qualité des réponses pédagogiques
- Adaptation au niveau utilisateur
- Gestion d'erreurs et cas limites
"""

import unittest
import requests
import json
import time
import sys
import os
from typing import Dict, Any, List

# Ajout du répertoire backend au path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

class TestScenarios(unittest.TestCase):
    """Tests basés sur des scénarios réels d'utilisation"""
    
    @classmethod
    def setUpClass(cls):
        """Configuration initiale des tests de scénarios"""
        cls.base_url = "http://localhost:5000"
        cls.timeout = 15  # Timeout plus long pour les scénarios complexes
        
        # Chargement des scénarios de test
        cls.scenarios = cls._load_test_scenarios()
        
        # Vérification du serveur
        cls.server_running = cls._check_server()
        
        print("\n🎭 Initialisation des tests de scénarios...")
        print(f"   Scénarios chargés: {len(cls.scenarios)}")
        print(f"   Serveur: {'✅ Actif' if cls.server_running else '❌ Inactif'}")
    
    @classmethod
    def _load_test_scenarios(cls) -> List[Dict[str, Any]]:
        """Charge les scénarios de test depuis le fichier JSON"""
        try:
            with open('data/test_scenarios.json', 'r', encoding='utf-8') as f:
                data = json.load(f)
            return data.get('test_scenarios', [])
        except FileNotFoundError:
            print("⚠️ Fichier test_scenarios.json non trouvé")
            return cls._get_default_scenarios()
        except Exception as e:
            print(f"⚠️ Erreur chargement scénarios: {e}")
            return cls._get_default_scenarios()
    
    @classmethod
    def _check_server(cls):
        """Vérifie si le serveur Flask est démarré"""
        try:
            response = requests.get(f"{cls.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    @classmethod
    def _get_default_scenarios(cls) -> List[Dict[str, Any]]:
        """Scénarios par défaut si le fichier n'est pas trouvé"""
        return [
            {
                "id": "basic_greeting",
                "name": "Test de salutation basique",
                "input": "Bonjour",
                "expected_behavior": {
                    "contains": ["bonjour", "aide", "deep learning"],
                    "min_length": 50,
                    "max_length": 200
                }
            },
            {
                "id": "concept_explanation_beginner", 
                "name": "Explication concept niveau débutant",
                "input": "Qu'est-ce qu'un réseau de neurones ?",
                "user_level": "beginner",
                "expected_behavior": {
                    "contains": ["réseau", "neurones", "exemple"],
                    "min_length": 100,
                    "max_length": 400
                }
            }
        ]
    
    def test_basic_greeting_scenario(self):
        """Test du scénario de salutation basique"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        scenario = self._get_scenario("basic_greeting")
        if not scenario:
            self.skipTest("Scénario 'basic_greeting' non trouvé")
        
        print(f"\n🎭 Test: {scenario['name']}")
        
        response = self._send_chat_message(scenario['input'])
        self.assertIsNotNone(response, "Réponse ne doit pas être None")
        
        self._validate_response_behavior(response, scenario['expected_behavior'])
        print("   ✅ Scénario de salutation réussi")
    
    def test_concept_explanation_beginner(self):
        """Test d'explication de concept niveau débutant"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        scenario = self._get_scenario("concept_explanation_beginner")
        if not scenario:
            self.skipTest("Scénario 'concept_explanation_beginner' non trouvé")
        
        print(f"\n🎭 Test: {scenario['name']}")
        
        response = self._send_chat_message(
            scenario['input'],
            level=scenario.get('user_level', 'beginner')
        )
        
        self.assertIsNotNone(response)
        self._validate_response_behavior(response, scenario['expected_behavior'])
        
        # Vérifications spécifiques niveau débutant
        response_lower = response.lower()
        self.assertTrue(
            any(word in response_lower for word in ['simple', 'exemple', 'comme']),
            "Réponse débutant doit contenir des éléments de simplification"
        )
        
        print("   ✅ Explication niveau débutant réussie")
    
    def test_concept_explanation_advanced(self):
        """Test d'explication de concept niveau avancé"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        scenario = self._get_scenario("concept_explanation_advanced")
        if not scenario:
            # Création d'un scénario avancé par défaut
            scenario = {
                "input": "Explique-moi la rétropropagation avec les détails mathématiques",
                "user_level": "advanced",
                "expected_behavior": {
                    "contains": ["rétropropagation", "gradient", "mathématique"],
                    "min_length": 200,
                    "max_length": 600
                }
            }
        
        print(f"\n🎭 Test: Explication concept niveau avancé")
        
        response = self._send_chat_message(
            scenario['input'],
            level=scenario.get('user_level', 'advanced')
        )
        
        self.assertIsNotNone(response)
        self._validate_response_behavior(response, scenario['expected_behavior'])
        
        # Vérifications spécifiques niveau avancé
        response_lower = response.lower()
        advanced_indicators = ['technique', 'algorithme', 'formule', 'calcul', 'mathématique']
        self.assertTrue(
            any(word in response_lower for word in advanced_indicators),
            "Réponse avancée doit contenir des termes techniques"
        )
        
        print("   ✅ Explication niveau avancé réussie")
    
    def test_comparison_scenario(self):
        """Test de scénario de comparaison"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        scenario = self._get_scenario("comparison_cnn_rnn")
        if not scenario:
            scenario = {
                "input": "Quelle est la différence entre CNN et RNN ?",
                "user_level": "intermediate",
                "expected_behavior": {
                    "contains": ["CNN", "RNN", "différence"],
                    "min_length": 150,
                    "max_length": 500
                }
            }
        
        print(f"\n🎭 Test: Comparaison CNN vs RNN")
        
        response = self._send_chat_message(
            scenario['input'],
            level=scenario.get('user_level', 'intermediate')
        )
        
        self.assertIsNotNone(response)
        self._validate_response_behavior(response, scenario['expected_behavior'])
        
        # Vérifications spécifiques comparaison
        response_upper = response.upper()
        self.assertIn("CNN", response_upper, "Doit mentionner CNN")
        self.assertIn("RNN", response_upper, "Doit mentionner RNN")
        
        comparison_words = ['différence', 'contrairement', 'tandis que', 'versus', 'vs']
        self.assertTrue(
            any(word in response.lower() for word in comparison_words),
            "Doit contenir des mots de comparaison"
        )
        
        print("   ✅ Scénario de comparaison réussi")
    
    def test_example_request_scenario(self):
        """Test de demande d'exemple concret"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        print(f"\n🎭 Test: Demande d'exemple concret")
        
        response = self._send_chat_message(
            "Donne-moi un exemple concret d'utilisation de CNN",
            level="intermediate"
        )
        
        self.assertIsNotNone(response)
        
        # Vérifications spécifiques aux exemples
        response_lower = response.lower()
        example_indicators = ['exemple', 'par exemple', 'comme', 'application', 'utilisation']
        self.assertTrue(
            any(word in response_lower for word in example_indicators),
            "Doit contenir des indicateurs d'exemple"
        )
        
        practical_examples = ['image', 'photo', 'reconnaissance', 'détection', 'classification']
        self.assertTrue(
            any(word in response_lower for word in practical_examples),
            "Doit donner des exemples pratiques"
        )
        
        print("   ✅ Exemple concret fourni")
    
    def test_out_of_scope_scenario(self):
        """Test de gestion des questions hors sujet"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        print(f"\n🎭 Test: Question hors sujet")
        
        response = self._send_chat_message(
            "Quelle est la recette de la pizza margherita ?",
            level="beginner"
        )
        
        self.assertIsNotNone(response)
        
        response_lower = response.lower()
        
        # Doit poliment rediriger
        polite_indicators = ['désolé', 'malheureusement', 'pas', 'plutôt', 'aide']
        self.assertTrue(
            any(word in response_lower for word in polite_indicators),
            "Doit poliment indiquer qu'il ne peut pas répondre"
        )
        
        # Doit rester dans le domaine
        domain_indicators = ['deep learning', 'intelligence artificielle', 'informatique', 'réseaux']
        self.assertTrue(
            any(phrase in response_lower for phrase in domain_indicators),
            "Doit rediriger vers le domaine approprié"
        )
        
        print("   ✅ Redirection hors sujet réussie")
    
    def test_ambiguous_question_scenario(self):
        """Test de gestion des questions ambiguës"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        print(f"\n🎭 Test: Question ambiguë")
        
        response = self._send_chat_message(
            "Comment ça marche ?",
            level="intermediate"
        )
        
        self.assertIsNotNone(response)
        
        response_lower = response.lower()
        
        # Doit demander des clarifications
        clarification_indicators = ['préciser', 'quel', 'quoi', 'spécifique', 'clarifier']
        self.assertTrue(
            any(word in response_lower for word in clarification_indicators),
            "Doit demander des clarifications"
        )
        
        print("   ✅ Gestion question ambiguë réussie")
    
    def test_level_adaptation_consistency(self):
        """Test de cohérence de l'adaptation au niveau"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        print(f"\n🎭 Test: Cohérence adaptation niveaux")
        
        question = "Qu'est-ce que la descente de gradient ?"
        levels = ["beginner", "intermediate", "advanced"]
        responses = {}
        
        for level in levels:
            responses[level] = self._send_chat_message(question, level=level)
            time.sleep(0.5)  # Éviter le rate limiting
        
        # Vérifications de cohérence
        for level in levels:
            self.assertIsNotNone(responses[level], f"Réponse {level} ne doit pas être None")
        
        # Réponse débutant doit être plus simple (moins de termes techniques)
        beginner_technical_words = self._count_technical_words(responses["beginner"])
        advanced_technical_words = self._count_technical_words(responses["advanced"])
        
        self.assertLessEqual(
            beginner_technical_words, 
            advanced_technical_words,
            "Réponse débutant ne doit pas avoir plus de termes techniques que avancé"
        )
        
        print(f"   Termes techniques - Débutant: {beginner_technical_words}, Avancé: {advanced_technical_words}")
        print("   ✅ Adaptation cohérente entre niveaux")
    
    def test_response_time_performance(self):
        """Test des performances de temps de réponse"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        print(f"\n🎭 Test: Performance temps de réponse")
        
        test_messages = [
            "Qu'est-ce que le Deep Learning ?",
            "Explique-moi les CNN",
            "Différence entre apprentissage supervisé et non supervisé"
        ]
        
        response_times = []
        
        for message in test_messages:
            start_time = time.time()
            response = self._send_chat_message(message)
            end_time = time.time()
            
            response_time = (end_time - start_time) * 1000  # en ms
            response_times.append(response_time)
            
            self.assertIsNotNone(response)
            self.assertLess(response_time, 15000, f"Réponse doit arriver en moins de 15s")
            
            time.sleep(0.5)  # Éviter le rate limiting
        
        avg_response_time = sum(response_times) / len(response_times)
        print(f"   Temps moyen: {avg_response_time:.0f}ms")
        print(f"   Temps min: {min(response_times):.0f}ms")
        print(f"   Temps max: {max(response_times):.0f}ms")
        
        self.assertLess(avg_response_time, 10000, "Temps moyen doit être < 10s")
        print("   ✅ Performance acceptable")
    
    def test_educational_quality(self):
        """Test de la qualité éducative des réponses"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        print(f"\n🎭 Test: Qualité éducative")
        
        response = self._send_chat_message(
            "Explique-moi pourquoi on utilise des fonctions d'activation",
            level="intermediate"
        )
        
        self.assertIsNotNone(response)
        
        # Critères de qualité éducative
        quality_score = 0
        response_lower = response.lower()
        
        # 1. Structure (numérotation, listes, sections)
        if any(marker in response for marker in ['1.', '2.', '-', '•']):
            quality_score += 1
        
        # 2. Exemples concrets
        if any(word in response_lower for word in ['exemple', 'par exemple', 'comme']):
            quality_score += 1
        
        # 3. Explications claires
        if any(word in response_lower for word in ['parce que', 'car', 'permet', 'grâce']):
            quality_score += 1
        
        # 4. Vocabulaire adapté
        if 100 <= len(response) <= 500:  # Longueur appropriée
            quality_score += 1
        
        # 5. Liens avec d'autres concepts
        if any(phrase in response_lower for phrase in ['lié à', 'connexion', 'relation', 'influence']):
            quality_score += 1
        
        print(f"   Score qualité éducative: {quality_score}/5")
        self.assertGreaterEqual(quality_score, 3, "Qualité éducative doit être >= 3/5")
        print("   ✅ Qualité éducative acceptable")
    
    # Méthodes utilitaires
    
    def _get_scenario(self, scenario_id: str) -> Dict[str, Any]:
        """Récupère un scénario par son ID"""
        for scenario in self.scenarios:
            if scenario.get('id') == scenario_id:
                return scenario
        return None
    
    def _send_chat_message(self, message: str, level: str = "intermediate") -> str:
        """Envoie un message au chatbot et retourne la réponse"""
        try:
            response = requests.post(
                f"{self.base_url}/api/chat",
                json={
                    "message": message,
                    "level": level,
                    "history": []
                },
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    return data.get('response', '')
            
            return None
            
        except Exception as e:
            print(f"   ❌ Erreur envoi message: {e}")
            return None
    
    def _validate_response_behavior(self, response: str, expected: Dict[str, Any]):
        """Valide le comportement de la réponse selon les critères attendus"""
        if not response:
            self.fail("Réponse vide")
        
        response_lower = response.lower()
        
        # Vérification des mots-clés requis
        if 'contains' in expected:
            for keyword in expected['contains']:
                self.assertIn(
                    keyword.lower(), 
                    response_lower,
                    f"Réponse doit contenir '{keyword}'"
                )
        
        # Vérification de la longueur
        if 'min_length' in expected:
            self.assertGreaterEqual(
                len(response),
                expected['min_length'],
                f"Réponse trop courte (min: {expected['min_length']})"
            )
        
        if 'max_length' in expected:
            self.assertLessEqual(
                len(response),
                expected['max_length'],
                f"Réponse trop longue (max: {expected['max_length']})"
            )
    
    def _count_technical_words(self, text: str) -> int:
        """Compte le nombre de mots techniques dans un texte"""
        if not text:
            return 0
        
        technical_words = [
            'algorithme', 'gradient', 'dérivée', 'matrice', 'vecteur',
            'fonction', 'optimisation', 'hyperparamètre', 'epoch',
            'batch', 'tensor', 'backpropagation', 'convolution'
        ]
        
        text_lower = text.lower()
        return sum(1 for word in technical_words if word in text_lower)


class TestConversationalContext(unittest.TestCase):
    """Tests de contexte conversationnel"""
    
    def setUp(self):
        self.base_url = "http://localhost:5000"
        self.timeout = 10
        self.server_running = self._check_server()
    
    def _check_server(self):
        try:
            response = requests.get(f"{self.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def test_conversation_continuity(self):
        """Test de continuité conversationnelle"""
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        print(f"\n🎭 Test: Continuité conversationnelle")
        
        # Premier échange
        response1 = self._send_chat_message("Qu'est-ce qu'un CNN ?")
        self.assertIsNotNone(response1)
        
        # Deuxième échange avec contexte
        history = [
            {"type": "user", "content": "Qu'est-ce qu'un CNN ?"},
            {"type": "assistant", "content": response1}
        ]
        
        response2 = self._send_chat_message("Comment ça marche exactement ?", history=history)
        self.assertIsNotNone(response2)
        
        # La deuxième réponse doit faire référence au contexte
        response2_lower = response2.lower()
        context_indicators = ['cnn', 'convolution', 'comme mentionné', 'comme dit']
        
        self.assertTrue(
            any(indicator in response2_lower for indicator in context_indicators),
            "Deuxième réponse doit faire référence au contexte"
        )
        
        print("   ✅ Continuité conversationnelle maintenue")
    
    def _send_chat_message(self, message: str, level: str = "intermediate", history: List = None) -> str:
        """Envoie un message avec contexte optionnel"""
        try:
            response = requests.post(
                f"{self.base_url}/api/chat",
                json={
                    "message": message,
                    "level": level,
                    "history": history or []
                },
                timeout=self.timeout
            )
            
            if response.status_code == 200:
                data = response.json()
                if data.get('success'):
                    return data.get('response', '')
            
            return None
            
        except Exception as e:
            print(f"   ❌ Erreur: {e}")
            return None


def run_scenario_tests():
    """Fonction principale pour exécuter les tests de scénarios"""
    print("🎭 TESTS DE SCÉNARIOS - CHATBOT PÉDAGOGIQUE")
    print("=" * 60)
    
    # Configuration du test runner
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Ajout des classes de test
    test_classes = [TestScenarios, TestConversationalContext]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Exécution des tests
    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    result = runner.run(suite)
    
    # Analyse des résultats
    print("\n" + "=" * 60)
    print("📊 RÉSUMÉ DES TESTS DE SCÉNARIOS")
    print(f"Tests exécutés: {result.testsRun}")
    print(f"Succès: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Échecs: {len(result.failures)}")
    print(f"Erreurs: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ ÉCHECS DÉTAILLÉS:")
        for test, traceback in result.failures:
            error_lines = traceback.split('\n')
            error_msg = next((line for line in error_lines if 'AssertionError:' in line), 'Erreur non spécifiée')
            print(f"   {test}: {error_msg.replace('AssertionError: ', '')}")
    
    if result.errors:
        print("\n🚨 ERREURS DÉTAILLÉES:")
        for test, traceback in result.errors:
            error_lines = traceback.split('\n')
            error_msg = error_lines[-2] if len(error_lines) > 1 else traceback
            print(f"   {test}: {error_msg}")
    
    # Calcul du score et recommandations
    success_rate = (result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100
    
    print(f"\n📈 SCORE GLOBAL: {success_rate:.1f}%")
    
    if success_rate >= 90:
        print("🏆 EXCELLENT ! Votre chatbot fonctionne parfaitement.")
    elif success_rate >= 75:
        print("✅ TRÈS BIEN ! Quelques améliorations mineures possibles.")
    elif success_rate >= 60:
        print("⚠️ CORRECT - Des améliorations sont nécessaires.")
    else:
        print("❌ ATTENTION - Problèmes importants à résoudre.")
    
    print("\n💡 RECOMMANDATIONS:")
    if not TestScenarios._check_server():
        print("   - Démarrez le serveur: python backend/app.py")
    
    if success_rate < 75:
        print("   - Vérifiez la configuration de votre clé API Mistral")
        print("   - Complétez votre base de connaissances")
        print("   - Testez manuellement les scénarios qui échouent")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_scenario_tests()
    sys.exit(0 if success else 1)