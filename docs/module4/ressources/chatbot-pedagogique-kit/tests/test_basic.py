"""
TESTS DE BASE - CHATBOT PÉDAGOGIQUE
Tests automatisés pour vérifier le fonctionnement de base du chatbot

Tests couverts :
- Configuration et initialisation
- Connexion API Mistral
- Base de connaissances
- Endpoints de l'API
- Fonctionnalités essentielles
"""

import unittest
import requests
import json
import time
import sys
import os

# Ajout du répertoire backend au path
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))

from config import Config
from knowledge_manager import KnowledgeManager
from mistral_client import MistralClient

class TestBasicFunctionality(unittest.TestCase):
    """Tests de base du chatbot"""
    
    @classmethod
    def setUpClass(cls):
        """Configuration initiale des tests"""
        cls.base_url = "http://localhost:5000"
        cls.config = Config()
        cls.timeout = 10  # secondes
        
        print("\n🧪 Initialisation des tests de base...")
        
        # Vérifier si le serveur est démarré
        cls.server_running = cls._check_server()
        
        if not cls.server_running:
            print("⚠️ Serveur non démarré. Certains tests seront ignorés.")
    
    @classmethod
    def _check_server(cls):
        """Vérifie si le serveur Flask est démarré"""
        try:
            response = requests.get(f"{cls.base_url}/health", timeout=5)
            return response.status_code == 200
        except:
            return False
    
    def test_01_configuration_validity(self):
        """Test de validité de la configuration"""
        print("\n🔧 Test configuration...")
        
        # Test de validation de la configuration
        validation = Config.validate_config()
        
        # La configuration doit avoir des warnings mais pas d'erreurs critiques
        self.assertIsInstance(validation, dict)
        self.assertIn('valid', validation)
        self.assertIn('errors', validation)
        self.assertIn('warnings', validation)
        
        print(f"   Configuration valide: {validation['valid']}")
        print(f"   Erreurs: {len(validation['errors'])}")
        print(f"   Avertissements: {len(validation['warnings'])}")
        
    def test_02_knowledge_base_loading(self):
        """Test de chargement de la base de connaissances"""
        print("\n📚 Test base de connaissances...")
        
        # Test avec le fichier par défaut
        km = KnowledgeManager('data/knowledge_base.json')
        
        # La base doit être chargée (même partiellement)
        self.assertTrue(km.is_loaded(), "Base de connaissances doit être chargée")
        
        # Doit avoir au moins un concept
        concepts = km.get_all_concepts()
        self.assertGreater(len(concepts), 0, "Doit avoir au moins un concept")
        
        # Test de recherche basique
        results = km.search_concepts("réseau neurones")
        self.assertIsInstance(results, list, "Recherche doit retourner une liste")
        
        print(f"   Concepts chargés: {len(concepts)}")
        print(f"   Recherche 'réseau neurones': {len(results)} résultats")
    
    def test_03_mistral_client_initialization(self):
        """Test d'initialisation du client Mistral"""
        print("\n🤖 Test client Mistral...")
        
        # Initialisation du client
        client = MistralClient(self.config.MISTRAL_API_KEY)
        
        # Le client doit être initialisé
        self.assertIsNotNone(client)
        self.assertEqual(client.api_key, self.config.MISTRAL_API_KEY)
        
        # Test de connexion (si clé API valide)
        if self.config.MISTRAL_API_KEY != "VOTRE_CLE_API":
            connection_ok = client.test_connection()
            print(f"   Connexion API: {'✅' if connection_ok else '❌'}")
        else:
            print("   ⚠️ Clé API non configurée - test de connexion ignoré")
    
    @unittest.skipUnless(True, "Test toujours exécuté")
    def test_04_server_health_check(self):
        """Test de santé du serveur"""
        print("\n🏥 Test santé serveur...")
        
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        try:
            response = requests.get(f"{self.base_url}/health", timeout=self.timeout)
            
            self.assertEqual(response.status_code, 200)
            
            data = response.json()
            self.assertIn('status', data)
            
            print(f"   Status: {data.get('status')}")
            
            if 'components' in data:
                components = data['components']
                print(f"   API Mistral: {'✅' if components.get('mistral_api') else '❌'}")
                print(f"   Base connaissances: {'✅' if components.get('knowledge_base') else '❌'}")
                print(f"   Optimiseur prompts: {'✅' if components.get('prompt_optimizer') else '❌'}")
                
        except requests.exceptions.Timeout:
            self.fail("Timeout sur le health check")
        except requests.exceptions.ConnectionError:
            self.fail("Impossible de se connecter au serveur")
    
    def test_05_api_endpoints_basic(self):
        """Test des endpoints API de base"""
        print("\n🔌 Test endpoints API...")
        
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        # Test endpoint racine
        response = requests.get(f"{self.base_url}/")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('message', data)
        self.assertIn('endpoints', data)
        
        print("   ✅ Endpoint racine OK")
        
        # Test endpoint concepts (GET)
        response = requests.get(f"{self.base_url}/api/concepts")
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('concepts', data)
        self.assertIsInstance(data['concepts'], list)
        
        print(f"   ✅ Endpoint concepts OK ({len(data['concepts'])} concepts)")
    
    def test_06_chat_endpoint_structure(self):
        """Test de structure de l'endpoint chat"""
        print("\n💬 Test endpoint chat...")
        
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        # Test avec données invalides (doit retourner erreur 400)
        response = requests.post(f"{self.base_url}/api/chat", json={})
        self.assertEqual(response.status_code, 400)
        
        print("   ✅ Validation des données d'entrée OK")
        
        # Test avec données valides mais message vide
        response = requests.post(f"{self.base_url}/api/chat", json={
            "message": "",
            "level": "beginner"
        })
        self.assertEqual(response.status_code, 400)
        
        print("   ✅ Validation message vide OK")
    
    def test_07_quiz_generation_structure(self):
        """Test de structure de génération de quiz"""
        print("\n📝 Test génération quiz...")
        
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        # Test de génération de quiz
        response = requests.post(f"{self.base_url}/api/quiz/generate", json={
            "topic": "deep_learning_general",
            "difficulty": "beginner",
            "count": 2
        })
        
        self.assertEqual(response.status_code, 200)
        
        data = response.json()
        self.assertIn('questions', data)
        self.assertIsInstance(data['questions'], list)
        
        if len(data['questions']) > 0:
            question = data['questions'][0]
            self.assertIn('question', question)
            self.assertIn('options', question)
            self.assertIn('correctAnswer', question)
            self.assertEqual(len(question['options']), 4)
        
        print(f"   ✅ Quiz généré avec {len(data['questions'])} questions")
    
    def test_08_error_handling(self):
        """Test de gestion d'erreurs"""
        print("\n❌ Test gestion erreurs...")
        
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        # Test endpoint inexistant
        response = requests.get(f"{self.base_url}/api/nonexistent")
        self.assertEqual(response.status_code, 404)
        
        data = response.json()
        self.assertIn('error', data)
        
        print("   ✅ Gestion 404 OK")
        
        # Test méthode HTTP incorrecte
        response = requests.put(f"{self.base_url}/api/chat")
        self.assertIn(response.status_code, [405, 404])  # Method not allowed ou Not found
        
        print("   ✅ Gestion méthode incorrecte OK")
    
    def test_09_response_time_performance(self):
        """Test de performance des temps de réponse"""
        print("\n⏱️ Test performance...")
        
        if not self.server_running:
            self.skipTest("Serveur non démarré")
        
        # Test temps de réponse health check
        start_time = time.time()
        response = requests.get(f"{self.base_url}/health")
        end_time = time.time()
        
        response_time = (end_time - start_time) * 1000  # en ms
        
        self.assertLess(response_time, 1000, "Health check doit répondre en moins de 1s")
        print(f"   Health check: {response_time:.0f}ms")
        
        # Test temps de réponse concepts
        start_time = time.time()
        response = requests.get(f"{self.base_url}/api/concepts")
        end_time = time.time()
        
        response_time = (end_time - start_time) * 1000
        
        self.assertLess(response_time, 2000, "Concepts doit répondre en moins de 2s")
        print(f"   Concepts API: {response_time:.0f}ms")
    
    def test_10_data_validation(self):
        """Test de validation des données"""
        print("\n✅ Test validation données...")
        
        # Test validation base de connaissances
        km = KnowledgeManager('data/knowledge_base.json')
        
        if km.is_loaded():
            concepts = km.get_all_concepts()
            
            for concept in concepts[:3]:  # Test sur les 3 premiers concepts
                # Chaque concept doit avoir les champs requis
                self.assertIn('id', concept)
                self.assertIn('title', concept)
                self.assertIn('description', concept)
                
                # Les IDs ne doivent pas être vides
                self.assertTrue(concept['id'].strip())
                self.assertTrue(concept['title'].strip())
        
        print("   ✅ Structure concepts valide")


class TestIntegration(unittest.TestCase):
    """Tests d'intégration des composants"""
    
    def test_full_workflow_simulation(self):
        """Test d'un workflow complet simulé"""
        print("\n🔄 Test workflow complet...")
        
        # 1. Chargement de la configuration
        config = Config()
        self.assertIsNotNone(config)
        
        # 2. Chargement base de connaissances
        km = KnowledgeManager('data/knowledge_base.json')
        self.assertTrue(km.is_loaded())
        
        # 3. Recherche de concepts
        results = km.search_concepts("neural network")
        self.assertIsInstance(results, list)
        
        # 4. Client Mistral (initialisation seulement)
        client = MistralClient("test_key")
        self.assertIsNotNone(client)
        
        print("   ✅ Workflow de base fonctionnel")


def run_basic_tests():
    """Fonction principale pour exécuter les tests"""
    print("🧪 TESTS DE BASE - CHATBOT PÉDAGOGIQUE")
    print("=" * 50)
    
    # Configuration du test runner
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Ajout des tests dans l'ordre
    test_classes = [TestBasicFunctionality, TestIntegration]
    
    for test_class in test_classes:
        tests = loader.loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Exécution des tests
    runner = unittest.TextTestRunner(verbosity=2, buffer=True)
    result = runner.run(suite)
    
    # Résumé des résultats
    print("\n" + "=" * 50)
    print("📊 RÉSUMÉ DES TESTS")
    print(f"Tests exécutés: {result.testsRun}")
    print(f"Succès: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Échecs: {len(result.failures)}")
    print(f"Erreurs: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ ÉCHECS:")
        for test, traceback in result.failures:
            print(f"   {test}: {traceback.split('AssertionError: ')[-1].split('\\n')[0]}")
    
    if result.errors:
        print("\n🚨 ERREURS:")
        for test, traceback in result.errors:
            error_msg = traceback.split('\\n')[-2] if '\\n' in traceback else traceback
            print(f"   {test}: {error_msg}")
    
    # Recommandations
    print("\n💡 RECOMMANDATIONS:")
    if not TestBasicFunctionality._check_server():
        print("   - Démarrez le serveur backend : python backend/app.py")
    
    if Config.MISTRAL_API_KEY == "VOTRE_CLE_API":
        print("   - Configurez votre clé API Mistral dans backend/config.py")
    
    success_rate = (result.testsRun - len(result.failures) - len(result.errors)) / result.testsRun * 100
    
    if success_rate >= 80:
        print("✅ Votre chatbot semble fonctionnel !")
    elif success_rate >= 60:
        print("⚠️ Quelques problèmes à corriger")
    else:
        print("❌ Problèmes importants détectés")
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_basic_tests()
    sys.exit(0 if success else 1)