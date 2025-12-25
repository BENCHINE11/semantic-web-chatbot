from kb import KnowledgeBase
from nlp import parse_question, build_sparql

def main():
    kb = KnowledgeBase()
    print("Chatbot sémantique (domaine : santé). Tape 'quit' pour sortir.\n")

    while True:
        question = input("Vous: ")
        if question.lower() in ("quit", "exit"):
            break

        intent, maladie = parse_question(question)
        sparql = build_sparql(intent, maladie)

        if sparql is None:
            print("Bot: Désolé, je n'ai pas compris la question ou la maladie.\n")
            continue

        results = kb.query(sparql)

        # formater la réponse en français
        if intent == "symptomes_maladie":
            symptomes = [str(row[0]).split("#")[-1] for row in results]
            if symptomes:
                print(f"Bot: Les symptômes de {maladie} sont : {', '.join(symptomes)}.\n")
            else:
                print(f"Bot: Je n'ai trouvé aucun symptôme pour {maladie}.\n")

        elif intent == "traitements_maladie":
            traitements = [str(row[0]).split("#")[-1] for row in results]
            if traitements:
                print(f"Bot: Les traitements de {maladie} sont : {', '.join(traitements)}.\n")
            else:
                print(f"Bot: Je n'ai trouvé aucun traitement pour {maladie}.\n")

if __name__ == "__main__":
    main()
