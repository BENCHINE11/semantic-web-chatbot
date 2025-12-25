# Chatbot Web Sémantique (Santé)

Ce projet implémente un mini chatbot utilisant les technologies du Web sémantique :
- Ontologie OWL et base de connaissances en RDF (domaine de la santé)
- Graphe de connaissances interrogé en SPARQL
- Module NLP simple pour transformer une question en requête SPARQL

## Installation

```bash
pip install -r requirements.txt
```

## Exécution
```bash 
python src/chatbot.py
```

## Exemples de questions :

- `Quels sont les symptômes de la grippe ?`
- `Quel est le traitement de la migraine ?`


---

## 8. Rapport (rapide mais propre) dans `report/rapport.md`

Je te propose une structure **très courte**, que tu peux remplir vite :

```markdown
# Projet Web Sémantique : Chatbot pour la santé

## 1. Introduction
- Du Web de documents au Web de données.
- Objectif : construire un chatbot qui répond à des questions de santé en s'appuyant sur une ontologie, un graphe RDF et des requêtes SPARQL.

## 2. Technologies utilisées
- RDF pour représenter les connaissances sous forme de triplets.
- OWL pour définir l'ontologie du domaine (Maladie, Symptome, Traitement).
- Base de connaissance = ensemble d'individus RDF instanciant l'ontologie.
- SPARQL pour interroger le graphe.
- NLP (pattern matching) pour analyser les questions et construire les requêtes SPARQL.

## 3. Modélisation du domaine (Ontologie OWL)
- Classes : `Maladie`, `Symptome`, `Traitement`.
- Propriétés d'objet : `aSymptome`, `estTraiteePar`.
- Exemple d'individus : `Grippe`, `Migraine`, `Fievre`, `Toux`, `Paracetamol`, `Ibuprofene`.

## 4. Construction de la base de connaissances (RDF)
- Fichier `ontology/sante.owl.ttl` contenant :
  - la TBox (classe, propriétés OWL),
  - l'ABox (triplets RDF représentant les maladies, symptômes et traitements).
- Ce fichier est chargé dans le programme Python via `rdflib`.

## 5. NLP et génération de requêtes SPARQL
- Module `nlp.py` :
  - détecte l'intention de la question (symptômes d'une maladie, traitements d'une maladie),
  - extrait la maladie (ex : Grippe, Migraine) à partir de la question.
- Génération de requêtes SPARQL paramétrées en fonction de l'intention :
  - Exemple : récupérer les symptômes d'une maladie donnée.

## 6. Chatbot sémantique
- Module `chatbot.py` :
  - boucle de dialogue en console,
  - pour chaque question :
    - NLP → intention + maladie,
    - construction de la requête SPARQL,
    - exécution sur le graphe RDF,
    - formatage de la réponse en langage naturel.

## 7. Résultats et limites
- Le chatbot répond correctement à des questions simples :
  - "Quels sont les symptômes de la grippe ?"
  - "Quel est le traitement de la migraine ?"
- Limites :
  - NLP basé sur des règles simples,
  - domaine limité à quelques maladies et traitements.

## 8. Conclusion et perspectives
- Le projet illustre le lien entre NLP, Web sémantique et graphe de connaissances.
- Pistes d'amélioration :
  - élargir le domaine,
  - utiliser un modèle NLP plus avancé,
  - ajouter une interface web.