# Chatbot Web Sémantique — Domaine Santé 🩺

Projet académique visant à démontrer l’utilisation conjointe de :

- NLP (traitement du langage naturel)
- Ontologies OWL
- RDF & Graphe de connaissances
- SPARQL

pour construire un chatbot capable d’interroger une base de connaissances médicale.

L’utilisateur pose une question en langage naturel (ex. *« Dans quels établissements travaille Dr Hicham ? »*),
le système la convertit en requête SPARQL, interroge le graphe RDF et renvoie une réponse compréhensible.


## 🎯 Objectifs pédagogiques

Ce projet montre concrètement :

1. Comment passer d’un texte humain à une requête sémantique.
1. Comment une ontologie OWL structure un domaine (ici : santé).
1. Comment RDF permet de créer un graphe de connaissances.
1. Comment SPARQL permet d’interroger ce graphe.
1. Comment intégrer tout cela dans un chatbot fonctionnel.

## 🏥 Domaine d'application : la santé

Le domaine modélisé couvre notamment :

- Médecins
- Patients
- Établissements de santé
- Diagnostics
- Traitements

Les relations principales incluent :

- `aPourPatient` — lie un médecin à ses patients
- `TravailleDans` — lie un médecin à son établissement
- `aPourDiagmostic` — lie un patient à un diagnostic
- `prescrit` — lie un médecin à un traitement

## 📚 Ontologie et Base de Connaissances utilisées

Le projet s’appuie sur une ontologie existante publiée sur GitHub :

👉 [https://github.com/Ahmedmessoudi/Project-WebSemantique](https://github.com/Ahmedmessoudi/Project-WebSemantique)

Les fichiers suivants ont été utilisés :

| Fichier |	Rôle |
|---|---|
| sante_ontologie.owl	| Ontologie (schéma, TBox) — éditée sous Protégé |
| sante_ontologie.rdf	| Base de connaissances RDF (ABox) — utilisée par le chatbot |

💡
Le fichier `.rdf` contient déjà **classes** + **propriétés** + **individus**, et il est entièrement compatible avec `rdflib`.
Le chatbot charge donc ce fichier pour construire et interroger le graphe.

**📌 Remerciement**

>Merci à Ahmed Messoudi pour la mise à disposition publique de ces fichiers OWL/RDF qui servent de fondation au projet.

## ⚙️ Architecture technique
```text
Utilisateur → NLP → Générateur SPARQL → Graphe RDF → Réponse textuelle
```


Organisation du projet :

```text
web-semantique-chatbot/
├─ ontology/
│  ├─ sante_ontologie.owl
│  └─ sante_ontologie.rdf
├─ src/
│  ├─ kb.py
│  ├─ nlp.py
│  └─ chatbot.py
├─ report/
│  └─ rapport.md
└─ README.md
```

## ▶️ Exécution du projet
### 1️⃣ Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2️⃣ Lancer le chatbot
```bash
python src/chatbot.py
```

## 💬 Exemples d’utilisation
#### Exemple 1 — Établissements d’un médecin

**Question :**

```nginx
Dans quels établissements travaille Dr Hicham ?
```

**Requête SPARQL générée :**
```sparql
PREFIX ont: <http://www.co-ode.org/ontologies/ont.owl#>

SELECT DISTINCT ?etab WHERE {
  ont:DrHicham ont:TravailleDans ?etab .
}
```

**Réponse du chatbot :**
```yaml
DrHicham travaille dans : Cabine_DrHicham, Hopital_IbnSina.
```

➡️ La réponse provient directement du **graphe RDF**.

## 🔍 Fonctionnement interne (A → Z)

1️⃣ **Chargement de la base de connaissances**
`rdflib` lit le fichier RDF et construit un graphe en mémoire.

2️⃣ **Analyse NLP de la question**
Un module NLP simple (pattern-based) détecte :

- l’intention → (*patients, traitements, établissements, diagnostic…*)
- l’entité → (*DrAymen, COVID19, etc.*)

3️⃣ **Génération automatique d’une requête SPARQL**

4️⃣ **Exécution sur le graphe RDF**

5️⃣ **Transformation en réponse lisible**

## 🚀 Améliorations possibles

Pour des prochaines versions :

- ✔️ Ajouter une **interface web** (Flask / React)
- ✔️ Supporter plus de types de questions (symptômes, examens, prescriptions complexes…)
- ✔️ Utiliser un vrai modèle NLP (spaCy / Transformers)
- ✔️ Ajouter un moteur d’inférence OWL (raisonneur)
- ✔️ Étendre la base de connaissances avec des données ouvertes (SNOMED, UMLS…)

## 🧰 Technologies utilisées
| Technologie |	Rôle |
|---|---|
| **Python** | Backend & chatbot |
| **rdflib** |	Manipulation RDF + SPARQL |
| **OWL** |	Modélisation sémantique du domaine |
| **RDF/XML** |	Représentation des connaissances |
| **SPARQL** |	Langage d’interrogation |
| **NLP (rules-based)** |	Analyse des questions |
| **Protégé** |	Conception et édition de l’ontologie |

## ✍️ Auteur

**Abdelilah BENCHINE**
ENSA Tanger — Module Web Sémantique

📧 contact sur demande
🙏 Merci à **Ahmed Messoudi** pour la contribution open-source à l’ontologie.