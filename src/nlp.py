PREFIX = """
PREFIX ont: <http://www.co-ode.org/ontologies/ont.owl#>
"""

# Mapping texte -> ID des individus dans l'ontologie
MEDECIN_MAP = {
    "dr aymen": "DrAymen",
    "aymen": "DrAymen",
    "dr hicham": "DrHicham",
    "hicham": "DrHicham",
    "dr khadija": "DrKhadija",
    "khadija": "DrKhadija",
}

DIAGNOSTIC_MAP = {
    "covid": "Diagnostique_COVID19",
    "covid-19": "Diagnostique_COVID19",
    "covid19": "Diagnostique_COVID19",
}


def parse_question(question: str):
    """
    Analyse très simple de la question en français :
    - détecte l'intention
    - détecte un médecin ou un diagnostic si applicable

    Retourne (intent, value) où value est:
    - un identifiant de médecin (ex: "DrAymen"),
    - ou un identifiant de diagnostic (ex: "Diagnostique_COVID19"),
    - ou None.
    """
    q = question.lower().strip()

    # 1) Cas "patients diagnostiqués COVID-19"
    if "patient" in q and ("diagnostiqu" in q or "diagnostic" in q):
        for k, diag_id in DIAGNOSTIC_MAP.items():
            if k in q:
                return "patients_diagnostic", diag_id

    # 2) Chercher le médecin mentionné
    medecin_id = None
    for key, mid in MEDECIN_MAP.items():
        if key in q:
            medecin_id = mid
            break

    # 3) Déterminer l'intention liée au médecin
    if medecin_id:
        # Patients d'un médecin
        if "patient" in q:
            return "patients_medecin", medecin_id

        # Établissements où il travaille
        if "travaille" in q or "établissement" in q or "etablissement" in q or "où" in q or "ou" in q:
            return "etablissements_medecin", medecin_id

        # Traitements prescrits
        if "traitement" in q or "prescrit" in q or "prescrire" in q:
            return "traitements_medecin", medecin_id

    return "inconnu", None


def build_sparql(intent: str, value: str | None):
    """
    Construit la requête SPARQL correspondant à l'intention.
    """
    if intent == "inconnu" or value is None:
        return None

    # value = identifiant de médecin (ex: "DrAymen")
    if intent in ("patients_medecin", "etablissements_medecin", "traitements_medecin"):
        med = value  # identifiant sans le prefix, ex: "DrAymen"

        if intent == "patients_medecin":
            return PREFIX + f"""
            SELECT DISTINCT ?patient WHERE {{
              ont:{med} ont:aPourPatient ?patient .
            }}
            """

        if intent == "etablissements_medecin":
            return PREFIX + f"""
            SELECT DISTINCT ?etab WHERE {{
              ont:{med} ont:TravailleDans ?etab .
            }}
            """

        if intent == "traitements_medecin":
            return PREFIX + f"""
            SELECT DISTINCT ?traitement WHERE {{
              ont:{med} ont:prescrit ?traitement .
            }}
            """

    # value = identifiant de diagnostic (ex: "Diagnostique_COVID19")
    if intent == "patients_diagnostic":
        diag = value
        return PREFIX + f"""
        SELECT DISTINCT ?patient WHERE {{
          ?patient ont:aPourDiagmostic ont:{diag} .
        }}
        """

    return None
