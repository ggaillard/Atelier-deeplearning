"""
OPTIMISEUR DE PROMPTS - CHOIX C PERSONNALISATION
Optimisation intelligente des prompts pour le chatbot pédagogique

Fonctionnalités :
- Templates de prompts adaptés au contexte
- Optimisation selon le niveau de l'utilisateur
- Enrichissement contextuel avec la base de connaissances
- Détection d'intention et adaptation
- Système de prompts dynamiques
"""

import json
import re
import logging
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

logger = logging.getLogger(__name__)

class IntentType(Enum):
    """Types d'intentions détectées"""
    EXPLANATION = "explanation"
    EXAMPLE = "example"
    COMPARISON = "comparison"
    DEFINITION = "definition"
    HOW_TO = "how_to"
    QUIZ = "quiz"
    TROUBLESHOOTING = "troubleshooting"
    GENERAL = "general"

class ContextType(Enum):
    """Types de contexte conversationnel"""
    FIRST_INTERACTION = "first"
    FOLLOW_UP = "follow_up"
    DEEP_DIVE = "deep_dive"
    CLARIFICATION = "clarification"
    CHANGE_TOPIC = "change_topic"

@dataclass
class PromptContext:
    """Contexte pour la génération de prompt"""
    user_message: str
    user_level: str
    intent_type: IntentType
    context_type: ContextType
    relevant_concepts: List[Dict[str, Any]]
    conversation_history: List[Dict[str, str]]
    user_preferences: Dict[str, Any] = None

class PromptOptimizer:
    """Optimiseur de prompts pour le chatbot pédagogique"""
    
    def __init__(self, templates_file_path: str):
        self.templates_file_path = templates_file_path
        self.templates: Dict[str, Dict[str, str]] = {}
        self.intent_patterns: Dict[IntentType, List[str]] = {}
        self.level_adaptations: Dict[str, Dict[str, str]] = {}
        self.is_ready_flag = False
        
        self.load_templates()
        self._initialize_intent_patterns()
        self._initialize_level_adaptations()
    
    def load_templates(self) -> bool:
        """
        Charge les templates de prompts depuis le fichier JSON
        
        Returns:
            True si le chargement a réussi
        """
        try:
            with open(self.templates_file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            self.templates = data.get('templates', {})
            logger.info(f"✅ Templates de prompts chargés : {len(self.templates)} catégories")
            self.is_ready_flag = True
            return True
            
        except FileNotFoundError:
            logger.warning(f"⚠️ Fichier templates non trouvé : {self.templates_file_path}")
            self._create_default_templates()
            return True
        except json.JSONDecodeError as e:
            logger.error(f"❌ Erreur JSON dans les templates : {e}")
            return False
        except Exception as e:
            logger.error(f"❌ Erreur chargement templates : {e}")
            return False
    
    def create_educational_prompt(
        self,
        user_message: str,
        user_level: str,
        relevant_concepts: List[Dict[str, Any]] = None,
        conversation_history: List[Dict[str, str]] = None,
        user_preferences: Dict[str, Any] = None
    ) -> str:
        """
        Crée un prompt éducatif optimizé
        
        Args:
            user_message: Message de l'utilisateur
            user_level: Niveau de l'utilisateur (beginner, intermediate, advanced)
            relevant_concepts: Concepts pertinents de la base de connaissances
            conversation_history: Historique de conversation
            user_preferences: Préférences utilisateur
            
        Returns:
            Prompt optimisé
        """
        # Détection d'intention
        intent = self._detect_intent(user_message)
        
        # Analyse du contexte conversationnel
        context_type = self._analyze_conversation_context(conversation_history or [])
        
        # Création du contexte
        prompt_context = PromptContext(
            user_message=user_message,
            user_level=user_level,
            intent_type=intent,
            context_type=context_type,
            relevant_concepts=relevant_concepts or [],
            conversation_history=conversation_history or [],
            user_preferences=user_preferences or {}
        )
        
        # Génération du prompt
        optimized_prompt = self._build_prompt(prompt_context)
        
        logger.info(f"🎯 Prompt optimisé: intent={intent.value}, level={user_level}, context={context_type.value}")
        return optimized_prompt
    
    def create_quiz_prompt(self, topic: str, difficulty: str, question_count: int) -> str:
        """
        Crée un prompt spécialisé pour la génération de quiz
        
        Args:
            topic: Sujet du quiz
            difficulty: Niveau de difficulté
            question_count: Nombre de questions
            
        Returns:
            Prompt pour génération de quiz
        """
        template = self.templates.get('quiz', {}).get('generation', self._get_default_quiz_template())
        
        difficulty_instructions = {
            'beginner': "Questions conceptuelles simples, privilégie les analogies et exemples concrets.",
            'intermediate': "Questions pratiques avec des cas d'usage, équilibre entre théorie et pratique.",
            'advanced': "Questions techniques approfondies, inclus des aspects mathématiques et d'optimisation."
        }
        
        return template.format(
            topic=topic,
            difficulty=difficulty,
            question_count=question_count,
            difficulty_instruction=difficulty_instructions.get(difficulty, difficulty_instructions['intermediate'])
        )
    
    def adapt_response_style(self, base_response: str, user_level: str, intent_type: IntentType) -> str:
        """
        Adapte le style d'une réponse selon le niveau et l'intention
        
        Args:
            base_response: Réponse de base
            user_level: Niveau utilisateur
            intent_type: Type d'intention
            
        Returns:
            Réponse adaptée
        """
        adaptations = self.level_adaptations.get(user_level, {})
        
        # Instructions d'adaptation selon le niveau
        if user_level == 'beginner':
            prefix = "Reformule cette réponse de manière plus simple, avec des analogies :\n\n"
        elif user_level == 'advanced':
            prefix = "Enrichis cette réponse avec plus de détails techniques :\n\n"
        else:
            prefix = "Améliore cette réponse pour la rendre plus pédagogique :\n\n"
        
        return prefix + base_response
    
    def generate_follow_up_suggestions(
        self,
        current_response: str,
        concepts_mentioned: List[str],
        user_level: str
    ) -> List[str]:
        """
        Génère des suggestions de questions de suivi
        
        Args:
            current_response: Réponse actuelle
            concepts_mentioned: Concepts mentionnés
            user_level: Niveau utilisateur
            
        Returns:
            Liste de suggestions
        """
        suggestions = []
        
        # Suggestions basées sur les concepts
        for concept in concepts_mentioned[:2]:  # Max 2 concepts
            if user_level == 'beginner':
                suggestions.append(f"Peux-tu me donner un exemple simple de {concept} ?")
            elif user_level == 'advanced':
                suggestions.append(f"Quelles sont les optimisations possibles pour {concept} ?")
            else:
                suggestions.append(f"Comment {concept} s'applique-t-il en pratique ?")
        
        # Suggestions génériques selon le niveau
        level_suggestions = {
            'beginner': [
                "Peux-tu me donner une analogie ?",
                "Comment cela s'applique-t-il dans la vraie vie ?",
                "Quels sont les exemples les plus simples ?"
            ],
            'intermediate': [
                "Quels sont les cas d'usage pratiques ?",
                "Quelles sont les meilleures pratiques ?",
                "Comment implémenter cela concrètement ?"
            ],
            'advanced': [
                "Quels sont les défis techniques actuels ?",
                "Comment optimiser les performances ?",
                "Quelles sont les recherches récentes sur ce sujet ?"
            ]
        }
        
        suggestions.extend(level_suggestions.get(user_level, [])[:2])
        return suggestions[:3]  # Max 3 suggestions
    
    def is_ready(self) -> bool:
        """Vérifie si l'optimiseur est prêt"""
        return self.is_ready_flag
    
    # Méthodes privées
    
    def _detect_intent(self, user_message: str) -> IntentType:
        """Détecte l'intention dans le message utilisateur"""
        message_lower = user_message.lower()
        
        # Vérification des patterns d'intention
        for intent_type, patterns in self.intent_patterns.items():
            for pattern in patterns:
                if re.search(pattern, message_lower):
                    return intent_type
        
        return IntentType.GENERAL
    
    def _analyze_conversation_context(self, conversation_history: List[Dict[str, str]]) -> ContextType:
        """Analyse le contexte de la conversation"""
        if not conversation_history:
            return ContextType.FIRST_INTERACTION
        
        history_length = len(conversation_history)
        
        if history_length == 1:
            return ContextType.FIRST_INTERACTION
        elif history_length <= 3:
            return ContextType.FOLLOW_UP
        else:
            # Analyser si c'est un approfondissement ou changement de sujet
            recent_messages = conversation_history[-3:]
            last_user_msg = recent_messages[-1].get('content', '').lower()
            
            if any(word in last_user_msg for word in ['détail', 'plus', 'approfondir', 'expliquer']):
                return ContextType.DEEP_DIVE
            elif any(word in last_user_msg for word in ['maintenant', 'autre', 'différent', 'nouveau']):
                return ContextType.CHANGE_TOPIC
            else:
                return ContextType.CLARIFICATION
    
    def _build_prompt(self, context: PromptContext) -> str:
        """Construit le prompt optimisé"""
        # Template de base selon l'intention
        base_template = self._get_template_for_intent(context.intent_type)
        
        # Instructions système personnalisées
        system_instructions = self._build_system_instructions(context)
        
        # Contexte de connaissances
        knowledge_context = self._build_knowledge_context(context.relevant_concepts)
        
        # Historique conversationnel
        conversation_context = self._build_conversation_context(context.conversation_history)
        
        # Assembly du prompt
        prompt_parts = [
            system_instructions,
            knowledge_context,
            conversation_context,
            f"Question de l'utilisateur : {context.user_message}",
            self._get_response_guidelines(context.user_level)
        ]
        
        return "\n\n".join(filter(None, prompt_parts))
    
    def _build_system_instructions(self, context: PromptContext) -> str:
        """Construit les instructions système"""
        base_instruction = """Tu es un assistant pédagogique spécialisé dans l'enseignement du Deep Learning pour des étudiants de BTS SIO."""
        
        level_specific = {
            'beginner': "Privilégie les explications simples, les analogies concrètes et évite le jargon technique.",
            'intermediate': "Équilibre entre concepts théoriques et applications pratiques, avec des exemples concrets.",
            'advanced': "Fournis des explications techniques approfondies avec détails mathématiques si pertinent."
        }
        
        intent_specific = {
            IntentType.EXPLANATION: "Focus sur une explication claire et structurée.",
            IntentType.EXAMPLE: "Fournis des exemples concrets et pratiques.",
            IntentType.COMPARISON: "Structure ta réponse autour d'une comparaison détaillée.",
            IntentType.DEFINITION: "Donne une définition précise puis développe avec des exemples.",
            IntentType.HOW_TO: "Fournis des instructions étape par étape."
        }
        
        instructions = [
            base_instruction,
            level_specific.get(context.user_level, level_specific['intermediate']),
            intent_specific.get(context.intent_type, "")
        ]
        
        return " ".join(filter(None, instructions))
    
    def _build_knowledge_context(self, relevant_concepts: List[Dict[str, Any]]) -> str:
        """Construit le contexte de connaissances"""
        if not relevant_concepts:
            return ""
        
        context_parts = ["Informations pertinentes de la base de connaissances :"]
        
        for concept in relevant_concepts[:3]:  # Max 3 concepts
            concept_info = f"- {concept.get('title', 'Concept')}: {concept.get('description', '')}"
            if concept.get('examples'):
                concept_info += f" Exemples: {', '.join(concept['examples'][:2])}"
            context_parts.append(concept_info)
        
        return "\n".join(context_parts)
    
    def _build_conversation_context(self, conversation_history: List[Dict[str, str]]) -> str:
        """Construit le contexte conversationnel"""
        if not conversation_history:
            return ""
        
        # Ne garde que les derniers échanges pertinents
        recent_history = conversation_history[-4:]  # 4 derniers messages
        
        if len(recent_history) <= 1:
            return ""
        
        context_parts = ["Contexte de la conversation :"]
        for msg in recent_history:
            role = "Utilisateur" if msg.get('type') == 'user' else "Assistant"
            content = msg.get('content', '')[:100]  # Limite à 100 caractères
            context_parts.append(f"- {role}: {content}...")
        
        return "\n".join(context_parts)
    
    def _get_response_guidelines(self, user_level: str) -> str:
        """Retourne les directives de réponse selon le niveau"""
        guidelines = {
            'beginner': """Structure ta réponse ainsi :
1. Explication simple avec analogie
2. Exemple concret facile à comprendre
3. Application pratique en informatique
4. Question pour vérifier la compréhension""",
            
            'intermediate': """Structure ta réponse ainsi :
1. Définition claire du concept
2. Exemple pratique d'application
3. Lien avec d'autres concepts
4. Conseil pour approfondir""",
            
            'advanced': """Structure ta réponse ainsi :
1. Explication technique détaillée
2. Aspects mathématiques si pertinents
3. Optimisations et meilleures pratiques
4. Références pour approfondir"""
        }
        
        return guidelines.get(user_level, guidelines['intermediate'])
    
    def _get_template_for_intent(self, intent: IntentType) -> str:
        """Récupère le template approprié pour une intention"""
        templates = self.templates.get('intents', {})
        return templates.get(intent.value, templates.get('general', ''))
    
    def _initialize_intent_patterns(self):
        """Initialise les patterns de détection d'intention"""
        self.intent_patterns = {
            IntentType.EXPLANATION: [
                r'\b(explique|comment|pourquoi|qu[\'e]st-ce que)\b',
                r'\b(fonctionne|marche)\b',
                r'\b(principe|concept)\b'
            ],
            IntentType.EXAMPLE: [
                r'\b(exemple|illustration|cas)\b',
                r'\b(montre|donne-moi)\b.*\b(exemple)\b',
                r'\b(concret|pratique)\b'
            ],
            IntentType.COMPARISON: [
                r'\b(différence|vs|par rapport)\b',
                r'\b(compare|comparaison)\b',
                r'\b(mieux|plutôt)\b'
            ],
            IntentType.DEFINITION: [
                r'\b(définition|c[\'e]est quoi|signifie)\b',
                r'\b(terme|mot|expression)\b',
                r'^(qu[\'e]st-ce que|define|def)\b'
            ],
            IntentType.HOW_TO: [
                r'\b(comment faire|how to|étapes)\b',
                r'\b(implémenter|créer|développer)\b',
                r'\b(procédure|méthode)\b'
            ],
            IntentType.QUIZ: [
                r'\b(quiz|test|question|évaluer)\b',
                r'\b(vérifier|tester)\b.*\b(connaissance)\b'
            ]
        }
    
    def _initialize_level_adaptations(self):
        """Initialise les adaptations par niveau"""
        self.level_adaptations = {
            'beginner': {
                'vocabulary': 'simple',
                'analogies': 'required',
                'technical_depth': 'minimal',
                'examples': 'concrete'
            },
            'intermediate': {
                'vocabulary': 'balanced',
                'analogies': 'optional',
                'technical_depth': 'moderate',
                'examples': 'practical'
            },
            'advanced': {
                'vocabulary': 'technical',
                'analogies': 'rare',
                'technical_depth': 'detailed',
                'examples': 'sophisticated'
            }
        }
    
    def _create_default_templates(self):
        """Crée des templates par défaut si le fichier n'existe pas"""
        self.templates = {
            'intents': {
                'explanation': "Explique clairement le concept demandé en l'adaptant au niveau {level}.",
                'example': "Fournis des exemples concrets et pratiques du concept.",
                'comparison': "Compare les éléments demandés de manière structurée.",
                'definition': "Donne une définition précise puis développe avec des exemples.",
                'general': "Réponds de manière pédagogique et adaptée au niveau de l'étudiant."
            },
            'quiz': {
                'generation': """Génère un quiz de {question_count} questions sur le sujet "{topic}" 
                avec un niveau de difficulté {difficulty}.
                
                {difficulty_instruction}
                
                Format JSON exact requis."""
            }
        }
        logger.info("📝 Templates par défaut créés")
    
    def _get_default_quiz_template(self) -> str:
        """Retourne le template par défaut pour les quiz"""
        return """Génère un quiz de {question_count} questions sur le sujet "{topic}" avec un niveau {difficulty}.

{difficulty_instruction}

Format JSON exact :
{{
    "title": "Quiz : {topic}",
    "questions": [
        {{
            "id": 1,
            "question": "Question ?",
            "options": ["Option A", "Option B", "Option C", "Option D"],
            "correctAnswer": 0,
            "explanation": "Explication pédagogique",
            "difficulty": "{difficulty}"
        }}
    ]
}}"""


# Analyseur de performance des prompts
class PromptAnalyzer:
    """Analyseur de performance des prompts"""
    
    def __init__(self):
        self.metrics = {
            'response_lengths': [],
            'response_times': [],
            'user_satisfaction': [],
            'intent_accuracy': []
        }
    
    def analyze_prompt_effectiveness(
        self,
        prompt: str,
        response: str,
        user_feedback: Optional[float] = None
    ) -> Dict[str, Any]:
        """
        Analyse l'efficacité d'un prompt
        
        Args:
            prompt: Prompt utilisé
            response: Réponse générée
            user_feedback: Feedback utilisateur (0-5)
            
        Returns:
            Métriques d'analyse
        """
        analysis = {
            'prompt_length': len(prompt),
            'response_length': len(response),
            'clarity_score': self._calculate_clarity_score(response),
            'structure_score': self._calculate_structure_score(response),
            'educational_value': self._calculate_educational_value(response)
        }
        
        if user_feedback is not None:
            analysis['user_satisfaction'] = user_feedback
            self.metrics['user_satisfaction'].append(user_feedback)
        
        return analysis
    
    def _calculate_clarity_score(self, response: str) -> float:
        """Calcule un score de clarté basé sur la structure"""
        # Métrique simple basée sur la longueur des phrases
        sentences = re.split(r'[.!?]+', response)
        avg_sentence_length = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
        
        # Score optimal pour phrases de 15-20 mots
        if 15 <= avg_sentence_length <= 20:
            return 1.0
        elif 10 <= avg_sentence_length <= 25:
            return 0.8
        else:
            return 0.6
    
    def _calculate_structure_score(self, response: str) -> float:
        """Calcule un score de structure"""
        structure_indicators = [
            r'\b\d+\.\s',  # Listes numérotées
            r'^\s*-\s',    # Listes à puces
            r'\b(d\'abord|ensuite|enfin|en conclusion)\b',  # Mots de transition
            r'\b(par exemple|notamment|c\'est-à-dire)\b'    # Mots d'illustration
        ]
        
        score = 0
        for pattern in structure_indicators:
            if re.search(pattern, response, re.MULTILINE | re.IGNORECASE):
                score += 0.25
        
        return min(score, 1.0)
    
    def _calculate_educational_value(self, response: str) -> float:
        """Calcule la valeur éducative"""
        educational_indicators = [
            r'\b(par exemple|exemple|illustration)\b',
            r'\b(comme|tel que|similaire à)\b',
            r'\b(principe|concept|théorie)\b',
            r'\b(application|pratique|usage)\b'
        ]
        
        score = 0
        for pattern in educational_indicators:
            matches = len(re.findall(pattern, response, re.IGNORECASE))
            score += matches * 0.1
        
        return min(score, 1.0)


# Test et exemple d'utilisation
if __name__ == "__main__":
    print("🧪 Test de l'optimiseur de prompts...")
    
    # Créer un fichier de templates temporaire pour le test
    import tempfile
    test_templates = {
        "templates": {
            "intents": {
                "explanation": "Explique clairement ce concept : {concept}",
                "general": "Réponds de manière pédagogique."
            }
        }
    }
    
    with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
        json.dump(test_templates, f)
        test_file = f.name
    
    # Test de l'optimiseur
    optimizer = PromptOptimizer(test_file)
    
    if optimizer.is_ready():
        print("✅ Optimiseur initialisé")
        
        # Test de création de prompt
        test_concepts = [
            {
                'title': 'Réseau de neurones',
                'description': 'Modèle informatique inspiré du cerveau',
                'examples': ['Reconnaissance vocale']
            }
        ]
        
        prompt = optimizer.create_educational_prompt(
            user_message="Explique-moi les réseaux de neurones",
            user_level="beginner",
            relevant_concepts=test_concepts
        )
        
        print(f"Prompt généré: {len(prompt)} caractères")
        print("✅ Test réussi")
    else:
        print("❌ Échec de l'initialisation")
    
    # Nettoyage
    import os
    os.unlink(test_file)
    
    print("✅ Tests terminés")