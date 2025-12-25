from kb import KnowledgeBase
from nlp import parse_question, build_sparql


def pretty_name(uri: str) -> str:
    """
    Extrait le 'local name' d'un IRI :
    http://www.co-ode.org/ontologies/ont.owl#DrAymen -> DrAymen
    """
    if "#" in uri:
        return uri.split("#")[-1]
    if "/" in uri:
        return uri.split("/")[-1]
    return uri


def main():
    kb = KnowledgeBase()
    print("Chatbot sémantique (domaine : santé)")
    print("Ontologie : projet GitHub Ahmedmessoudi/Project-WebSemantique")
    print("Exemples de questions :")
    print("- Quels sont les patients de Dr Aymen ?")
    print("- Dans quels établissements travaille Dr Hicham ?")
    print("- Quels traitements prescrit Dr Aymen ?")
    print("- Quels sont les patients diagnostiqués COVID-19 ?")
    print("Tape 'quit' pour sortir.\n")

    while True:
        question = input("Vous: ")
        if question.lower().strip() in ("quit", "exit"):
            break

        intent, value = parse_question(question)
        sparql = build_sparql(intent, value)

        if sparql is None:
            print("Bot: Désolé, je n'ai pas compris la question ou je ne peux pas encore y répondre.\n")
            continue

        results = list(kb.query(sparql))

        # Intention : patients d'un médecin
        if intent == "patients_medecin":
            patients = [pretty_name(str(row[0])) for row in results]
            if patients:
                print(f"Bot: Les patients de {value} sont : {', '.join(patients)}.\n")
            else:
                print(f"Bot: Je n'ai trouvé aucun patient pour {value}.\n")

        # Intention : établissements où travaille un médecin
        elif intent == "etablissements_medecin":
            etabs = [pretty_name(str(row[0])) for row in results]
            if etabs:
                print(f"Bot: {value} travaille dans : {', '.join(etabs)}.\n")
            else:
                print(f"Bot: Je n'ai trouvé aucun établissement pour {value}.\n")

        # Intention : traitements prescrits par un médecin
        elif intent == "traitements_medecin":
            traitements = [pretty_name(str(row[0])) for row in results]
            if traitements:
                print(f"Bot: {value} prescrit les traitements suivants : {', '.join(traitements)}.\n")
            else:
                print(f"Bot: Je n'ai trouvé aucun traitement prescrit par {value}.\n")

        # Intention : patients avec un diagnostic donné (ex: COVID-19)
        elif intent == "patients_diagnostic":
            patients = [pretty_name(str(row[0])) for row in results]
            if patients:
                print(f"Bot: Les patients avec ce diagnostic sont : {', '.join(patients)}.\n")
            else:
                print("Bot: Je n'ai trouvé aucun patient avec ce diagnostic.\n")

        else:
            print("Bot: Pour l'instant je sais répondre sur les patients, établissements, traitements et diagnostics COVID-19.\n")


if __name__ == "__main__":
    main()
