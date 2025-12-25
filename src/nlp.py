import re

def parse_question(question: str):
    q = question.lower()

    # détecter la maladie (mot après "de la", "de le", "de l'", "de ")
    # pour le projet, tu peux simplifier et faire des if
    maladie = None
    # exemples simples
    if "grippe" in q:
        maladie = "Grippe"
    elif "migraine" in q:
        maladie = "Migraine"

    # intention : symptômes ?
    if "symptome" in q or "symptômes" in q:
        intent = "symptomes_maladie"
    # intention : traitement ?
    elif "traitement" in q or "soigne" in q or "traiter" in q:
        intent = "traitements_maladie"
    else:
        intent = "inconnu"

    return intent, maladie

PREFIX = """
PREFIX : <http://example.org/sante#>
"""

def build_sparql(intent: str, maladie: str | None):
    if maladie is None:
        return None

    if intent == "symptomes_maladie":
        return PREFIX + f"""
        SELECT ?symptome WHERE {{
          :{maladie} :aSymptome ?symptome .
        }}
        """
    elif intent == "traitements_maladie":
        return PREFIX + f"""
        SELECT ?traitement WHERE {{
          :{maladie} :estTraiteePar ?traitement .
        }}
        """
    else:
        return None
