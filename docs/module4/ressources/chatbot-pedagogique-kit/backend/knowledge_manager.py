"""
GESTIONNAIRE DE BASE DE CONNAISSANCES
Gestion de la base de connaissances pour le chatbot pédagogique

Fonctionnalités :
- Chargement et validation de la base de connaissances JSON
- Recherche de concepts par mots-clés
- Génération de quiz à partir des concepts
- Extraction de concepts depuis du texte
- Suggestions de concepts liés
"""

import json
import re
import logging
from typing import List, Dict, Any, Optional, Set
from dataclasses import dataclass
from difflib import SequenceMatcher
import random

logger = logging.getLogger(__name__)

@dataclass
class Concept:
    """Structure d'un concept de la base de connaissances"""
    id: str
    title: str
    description: str
    levels: Dict[str, str]
    examples: List[str]
    analogies: List[str]
    related_concepts: List[str]
    quiz: List[Dict[str, Any]]
    keywords: List[str] = None

class KnowledgeManager:
    """Gestionnaire de la base de connaissances"""
    
    def __init__(self, knowledge_file_path: str):
        self.knowledge_file_path = knowledge_file_path
        self.concepts: Dict[str, Concept] = {}
        self.keyword_index: Dict[str, Set[str]] = {}  # mot-clé -> set(concept_ids)
        self.is_loaded_flag = False
        
        self.load_knowledge_base()
    
    def load_knowledge_base(self) -> bool:
        """
        Charge la base de connaissances depuis le fichier JSON
        
        Returns:
            True si le chargement a réussi
        """
        try:
            with open(self.knowledge_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'concepts' not in data:
                logger.error("❌ Format de base de connaissances invalide : 'concepts' manquant")
                return False
            
            concepts_data = data['concepts']
            logger.info(f"📚 Chargement de {len(concepts_data)} concepts...")
            
            for concept_data in concepts_data:
                # Validation du concept
                if not self._validate_concept(concept_data):
                    logger.warning(f"⚠️ Concept invalide ignoré : {concept_data.get('id', 'unknown')}")
                    continue
                
                # Création de l'objet Concept
                concept = Concept(
                    id=concept_data['id'],
                    title=concept_data['title'],
                    description=concept_data['description'],
                    levels=concept_data.get('levels', {}),
                    examples=concept_data.get('examples', []),
                    analogies=concept_data.get('analogies', []),
                    related_concepts=concept_data.get('related_concepts', []),
                    quiz=concept_data.get('quiz', []),
                    keywords=concept_data.get('keywords', [])
                )
                
                self.concepts[concept.id] = concept
                self._index_concept_keywords(concept)
            
            self.is_loaded_flag = True
            logger.info(f"✅ Base de connaissances chargée : {len(self.concepts)} concepts")
            return True
            
        except FileNotFoundError:
            logger.error(f"❌ Fichier de base de connaissances non trouvé : {self.knowledge_file_path}")
            return False
        except json.JSONDecodeError as e:
            logger.error(f"❌ Erreur JSON dans la base de connaissances : {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Erreur lors du chargement : {e}")
            return False
    
    def search_concepts(self, query: str, max_results: int = 5) -> List[Dict[str, Any]]:
        """
        Recherche de concepts basée sur une requête
        
        Args:
            query: Texte de recherche
            max_results: Nombre max de résultats
            
        Returns:
            Liste des concepts pertinents avec scores
        """
        if not self.is_loaded_flag:
            return []
        
        query_lower = query.lower()
        concept_scores = {}
        
        # Extraction des mots-clés de la requête
        query_words = set(re.findall(r'\b\w+\b', query_lower))
        
        for concept_id, concept in self.concepts.items():
            score = self._calculate_relevance_score(concept, query_lower, query_words)
            if score > 0:
                concept_scores[concept_id] = score
        
        # Tri par score décroissant
        sorted_concepts = sorted(concept_scores.items(), key=lambda x: x[1], reverse=True)
        
        # Formatage des résultats
        results = []
        for concept_id, score in sorted_concepts[:max_results]:
            concept = self.concepts[concept_id]
            results.append({
                'id': concept.id,
                'title': concept.title,
                'description': concept.description,
                'score': score,
                'levels': concept.levels,
                'examples': concept.examples[:2],  # Limiter aux 2 premiers exemples
                'related_concepts': concept.related_concepts
            })
        
        logger.info(f"🔍 Recherche '{query[:50]}': {len(results)} résultats")
        return results
    
    def get_concept(self, concept_id: str) -> Optional[Dict[str, Any]]:
        """
        Récupère un concept par son ID
        
        Args:
            concept_id: Identifiant du concept
            
        Returns:
            Données du concept ou None
        """
        if concept_id not in self.concepts:
            return None
        
        concept = self.concepts[concept_id]
        return {
            'id': concept.id,
            'title': concept.title,
            'description': concept.description,
            'levels': concept.levels,
            'examples': concept.examples,
            'analogies': concept.analogies,
            'related_concepts': concept.related_concepts,
            'quiz': concept.quiz
        }
    
    def get_all_concepts(self) -> List[Dict[str, str]]:
        """
        Récupère la liste de tous les concepts (format simplifié)
        
        Returns:
            Liste des concepts avec id, title, description
        """
        return [
            {
                'id': concept.id,
                'title': concept.title,
                'description': concept.description
            }
            for concept in self.concepts.values()
        ]
    
    def extract_concepts_from_text(self, text: str) -> List[str]:
        """
        Extrait les concepts mentionnés dans un texte
        
        Args:
            text: Texte à analyser
            
        Returns:
            Liste des IDs de concepts trouvés
        """
        text_lower = text.lower()
        found_concepts = []
        
        for concept_id, concept in self.concepts.items():
            # Vérification du titre du concept
            if concept.title.lower() in text_lower:
                found_concepts.append(concept_id)
                continue
            
            # Vérification des mots-clés
            concept_keywords = self._get_concept_keywords(concept)
            for keyword in concept_keywords:
                if keyword.lower() in text_lower:
                    found_concepts.append(concept_id)
                    break
        
        # Suppression des doublons tout en gardant l'ordre
        seen = set()
        unique_concepts = []
        for concept_id in found_concepts:
            if concept_id not in seen:
                seen.add(concept_id)
                unique_concepts.append(concept_id)
        
        return unique_concepts
    
    def get_related_concepts(self, concept_id: str, depth: int = 1) -> List[str]:
        """
        Récupère les concepts liés à un concept donné
        
        Args:
            concept_id: ID du concept source
            depth: Profondeur de recherche
            
        Returns:
            Liste des concepts liés
        """
        if concept_id not in self.concepts:
            return []
        
        related = set()
        to_explore = {concept_id}
        
        for _ in range(depth):
            next_to_explore = set()
            for current_id in to_explore:
                if current_id in self.concepts:
                    concept_related = self.concepts[current_id].related_concepts
                    for rel_id in concept_related:
                        if rel_id != concept_id and rel_id in self.concepts:
                            related.add(rel_id)
                            next_to_explore.add(rel_id)
            to_explore = next_to_explore
        
        return list(related)
    
    def generate_quiz(self, topic: str = None, difficulty: str = 'intermediate', count: int = 5) -> Dict[str, Any]:
        """
        Génère un quiz à partir de la base de connaissances
        
        Args:
            topic: Sujet spécifique (optionnel)
            difficulty: Niveau de difficulté
            count: Nombre de questions
            
        Returns:
            Quiz généré
        """
        all_questions = []
        
        # Collecte des questions de tous les concepts pertinents
        for concept in self.concepts.values():
            if topic and topic.lower() not in concept.title.lower() and topic != concept.id:
                continue
            
            for question in concept.quiz:
                if question.get('difficulty', 'intermediate') == difficulty:
                    # Enrichissement de la question avec le contexte du concept
                    enriched_question = {
                        **question,
                        'concept_id': concept.id,
                        'concept_title': concept.title
                    }
                    all_questions.append(enriched_question)
        
        if not all_questions:
            logger.warning(f"⚠️ Aucune question trouvée pour {topic or 'tous sujets'} / {difficulty}")
            return self._generate_fallback_quiz(topic, difficulty, count)
        
        # Sélection aléatoire des questions
        selected_questions = random.sample(
            all_questions, 
            min(count, len(all_questions))
        )
        
        # Formatage du quiz
        quiz = {
            'title': f"Quiz {topic or 'Deep Learning'} - Niveau {difficulty}",
            'difficulty': difficulty,
            'topic': topic or 'general',
            'questions': []
        }
        
        for i, question in enumerate(selected_questions):
            quiz['questions'].append({
                'id': i + 1,
                'question': question['question'],
                'options': question['options'],
                'correctAnswer': question['correct_answer'],
                'explanation': question['explanation'],
                'difficulty': question.get('difficulty', difficulty),
                'concept': question.get('concept_title', 'Concept général')
            })
        
        logger.info(f"📝 Quiz généré : {len(quiz['questions'])} questions")
        return quiz
    
    def get_concept_by_title(self, title: str) -> Optional[str]:
        """
        Trouve l'ID d'un concept par son titre
        
        Args:
            title: Titre du concept
            
        Returns:
            ID du concept ou None
        """
        title_lower = title.lower()
        
        # Recherche exacte
        for concept in self.concepts.values():
            if concept.title.lower() == title_lower:
                return concept.id
        
        # Recherche approximative
        best_match = None
        best_ratio = 0.8  # Seuil minimum de similarité
        
        for concept in self.concepts.values():
            ratio = SequenceMatcher(None, title_lower, concept.title.lower()).ratio()
            if ratio > best_ratio:
                best_ratio = ratio
                best_match = concept.id
        
        return best_match
    
    def is_loaded(self) -> bool:
        """Vérifie si la base de connaissances est chargée"""
        return self.is_loaded_flag
    
    def get_stats(self) -> Dict[str, Any]:
        """Statistiques de la base de connaissances"""
        if not self.is_loaded_flag:
            return {"error": "Base de connaissances non chargée"}
        
        total_quiz_questions = sum(len(concept.quiz) for concept in self.concepts.values())
        concepts_with_examples = sum(1 for concept in self.concepts.values() if concept.examples)
        concepts_with_analogies = sum(1 for concept in self.concepts.values() if concept.analogies)
        
        return {
            'total_concepts': len(self.concepts),
            'total_quiz_questions': total_quiz_questions,
            'concepts_with_examples': concepts_with_examples,
            'concepts_with_analogies': concepts_with_analogies,
            'keyword_index_size': len(self.keyword_index),
            'file_path': self.knowledge_file_path
        }
    
    # Méthodes privées
    
    def _validate_concept(self, concept_data: Dict[str, Any]) -> bool:
        """Valide la structure d'un concept"""
        required_fields = ['id', 'title', 'description']
        
        for field in required_fields:
            if field not in concept_data:
                logger.error(f"❌ Champ obligatoire manquant : {field}")
                return False
        
        # Validation des quiz si présents
        if 'quiz' in concept_data:
            for i, question in enumerate(concept_data['quiz']):
                if not self._validate_quiz_question(question, i):
                    return False
        
        return True
    
    def _validate_quiz_question(self, question: Dict[str, Any], index: int) -> bool:
        """Valide une question de quiz"""
        required_fields = ['question', 'options', 'correct_answer', 'explanation']
        
        for field in required_fields:
            if field not in question:
                logger.error(f"❌ Question {index}: champ manquant '{field}'")
                return False
        
        if len(question['options']) != 4:
            logger.error(f"❌ Question {index}: doit avoir exactement 4 options")
            return False
        
        correct_answer = question['correct_answer']
        if not isinstance(correct_answer, int) or correct_answer < 0 or correct_answer >= 4:
            logger.error(f"❌ Question {index}: correct_answer doit être entre 0 et 3")
            return False
        
        return True
    
    def _index_concept_keywords(self, concept: Concept):
        """Indexe les mots-clés d'un concept pour la recherche"""
        keywords = self._get_concept_keywords(concept)
        
        for keyword in keywords:
            keyword_lower = keyword.lower()
            if keyword_lower not in self.keyword_index:
                self.keyword_index[keyword_lower] = set()
            self.keyword_index[keyword_lower].add(concept.id)
    
    def _get_concept_keywords(self, concept: Concept) -> List[str]:
        """Récupère tous les mots-clés d'un concept"""
        keywords = []
        
        # Mots-clés explicites
        if concept.keywords:
            keywords.extend(concept.keywords)
        
        # Mots du titre
        title_words = re.findall(r'\b\w+\b', concept.title.lower())
        keywords.extend(title_words)
        
        # Mots de la description (limités)
        desc_words = re.findall(r'\b\w{4,}\b', concept.description.lower())  # Mots de 4+ lettres
        keywords.extend(desc_words[:5])  # Max 5 mots de la description
        
        return list(set(keywords))  # Suppression des doublons
    
    def _calculate_relevance_score(self, concept: Concept, query_lower: str, query_words: Set[str]) -> float:
        """Calcule le score de pertinence d'un concept pour une requête"""
        score = 0.0
        
        # Score pour titre exact ou partiel
        if concept.title.lower() in query_lower:
            score += 10.0
        elif any(word in concept.title.lower() for word in query_words):
            score += 5.0
        
        # Score pour description
        if any(word in concept.description.lower() for word in query_words):
            score += 2.0
        
        # Score pour mots-clés
        concept_keywords = set(keyword.lower() for keyword in self._get_concept_keywords(concept))
        matching_keywords = concept_keywords.intersection(query_words)
        score += len(matching_keywords) * 3.0
        
        # Score pour exemples et analogies
        all_text = ' '.join(concept.examples + concept.analogies).lower()
        if any(word in all_text for word in query_words):
            score += 1.0
        
        return score
    
    def _generate_fallback_quiz(self, topic: str, difficulty: str, count: int) -> Dict[str, Any]:
        """Génère un quiz de fallback quand aucune question n'est trouvée"""
        fallback_questions = [
            {
                'id': 1,
                'question': 'Qu\'est-ce que le Deep Learning ?',
                'options': [
                    'Une technique de programmation',
                    'Un sous-domaine du Machine Learning utilisant des réseaux de neurones profonds',
                    'Un langage de programmation',
                    'Un type de base de données'
                ],
                'correctAnswer': 1,
                'explanation': 'Le Deep Learning est un sous-domaine du Machine Learning qui utilise des réseaux de neurones avec plusieurs couches cachées.',
                'difficulty': difficulty,
                'concept': 'Concepts généraux'
            }
        ]
        
        return {
            'title': f'Quiz de base - {topic or "Deep Learning"}',
            'difficulty': difficulty,
            'topic': topic or 'general',
            'questions': fallback_questions[:count]
        }


# Utilitaires pour la gestion de la base de connaissances
class KnowledgeValidator:
    """Validateur pour la base de connaissances"""
    
    @staticmethod
    def validate_file(file_path: str) -> Dict[str, Any]:
        """
        Valide complètement un fichier de base de connaissances
        
        Returns:
            Rapport de validation
        """
        report = {
            'valid': False,
            'errors': [],
            'warnings': [],
            'stats': {}
        }
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            if 'concepts' not in data:
                report['errors'].append("Structure invalide : 'concepts' manquant")
                return report
            
            concepts = data['concepts']
            report['stats']['total_concepts'] = len(concepts)
            
            valid_concepts = 0
            total_quiz_questions = 0
            
            for i, concept in enumerate(concepts):
                concept_errors = KnowledgeValidator._validate_concept_structure(concept, i)
                if concept_errors:
                    report['errors'].extend(concept_errors)
                else:
                    valid_concepts += 1
                    total_quiz_questions += len(concept.get('quiz', []))
            
            report['stats']['valid_concepts'] = valid_concepts
            report['stats']['total_quiz_questions'] = total_quiz_questions
            report['valid'] = len(report['errors']) == 0
            
        except Exception as e:
            report['errors'].append(f"Erreur de lecture du fichier : {e}")
        
        return report
    
    @staticmethod
    def _validate_concept_structure(concept: Dict[str, Any], index: int) -> List[str]:
        """Valide la structure d'un concept"""
        errors = []
        required_fields = ['id', 'title', 'description']
        
        for field in required_fields:
            if field not in concept:
                errors.append(f"Concept {index}: champ '{field}' manquant")
        
        # Validation des quiz
        if 'quiz' in concept:
            for q_idx, question in enumerate(concept['quiz']):
                if 'question' not in question:
                    errors.append(f"Concept {index}, Question {q_idx}: 'question' manquant")
                if 'options' not in question or len(question.get('options', [])) != 4:
                    errors.append(f"Concept {index}, Question {q_idx}: doit avoir 4 options")
                if 'correct_answer' not in question:
                    errors.append(f"Concept {index}, Question {q_idx}: 'correct_answer' manquant")
        
        return errors


# Test et exemple d'utilisation
if __name__ == "__main__":
    # Test de base du gestionnaire de connaissances
    print("🧪 Test du gestionnaire de connaissances...")
    
    # Simulation avec données de test
    test_data = {
        "concepts": [
            {
                "id": "neural_network",
                "title": "Réseau de neurones",
                "description": "Modèle informatique inspiré du cerveau",
                "levels": {
                    "beginner": "Un réseau qui apprend comme le cerveau"
                },
                "examples": ["Reconnaissance d'images"],
                "analogies": ["Comme un cerveau artificiel"],
                "related_concepts": ["deep_learning"],
                "quiz": [
                    {
                        "question": "Qu'est-ce qu'un réseau de neurones ?",
                        "options": ["A", "B", "C", "D"],  
                        "correct_answer": 0,
                        "explanation": "Test"
                    }
                ]
            }
        ]
    }
    
    # Créer fichier temporaire pour test
    import tempfile
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        json.dump(test_data, f)
        test_file = f.name
    
    # Test du gestionnaire
    km = KnowledgeManager(test_file)
    
    if km.is_loaded():
        print("✅ Chargement réussi")
        print(f"Concepts: {len(km.get_all_concepts())}")
        
        # Test de recherche
        results = km.search_concepts("réseau neurones")
        print(f"Recherche: {len(results)} résultats")
        
        # Test génération quiz
        quiz = km.generate_quiz(count=1)
        print(f"Quiz: {len(quiz['questions'])} questions")
    else:
        print("❌ Échec du chargement")
    
    # Nettoyage
    import os
    os.unlink(test_file)
    
    print("✅ Tests terminés")