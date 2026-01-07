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
    print("\n" + "=" * 45)
    print("🤖  CHATBOT SÉMANTIQUE — Domaine : Santé")
    print("=" * 45)

    print("\n📚 Crédits : Ahmedmessoudi / Project-WebSemantique")

    print("\n💬 Exemples de questions :")
    print("   • Qui sont les patients de Dr Aymen ?")
    print("   • Quels sont les patients diagnostiqués COVID-19 ?")
    print("\n👉 Tapez 'quit' pour quitter le programme.")

    while True:
        question = input("\n💻 Vous > ")
        if question.lower().strip() in ("quit", "exit"):
            print("\n" + "=" * 55)
            print("👋  Merci d'avoir utilisé le chatbot — à bientôt !")
            print("✨ N’hésitez pas à revenir poser d’autres questions.")
            print("=" * 55 + "\n")
            break

        intent, value = parse_question(question)
        sparql = build_sparql(intent, value)

        if sparql is None:
            print(
                "\n🤖 Bot > Désolé, je n’ai pas bien compris votre question "
                "ou je ne peux pas encore y répondre.\n"
                "💡 Astuce : essayez de reformuler ou posez une question plus précise.\n"
            )
            continue

        # 🌐 Affichage du traitement sémantique + requête SPARQL
        print("\n🧠 Traitement sémantique")
        print(f"1. Identification de l’entité {value}...")
        print("2. Correspondance avec les concepts de l’ontologie médicale...")
        print("3. Génération automatique d’une requête SPARQL...\n")
        print("📎 Requête SPARQL générée :")
        print(sparql)
        print("=" * 45)

        # Exécution de la requête sur le graphe RDF
        results = list(kb.query(sparql))

        # Intention : patients d'un médecin
        if intent == "patients_medecin":
            patients = [pretty_name(str(row[0])) for row in results]
            if patients:
                print(f"\n🤖 Bot > Résultat trouvé pour le médecin {value} :\n")
                print("🩺 Patients suivis :")
                for p in patients:
                    print(f"   • {p}")
            else:
                print(f"\n🤖 Bot > Aucun patient trouvé pour le médecin {value}.")
                print("💡 Astuce : Vérifiez l’orthographe ou essayez un autre médecin.")

        # Intention : établissements où travaille un médecin
        elif intent == "etablissements_medecin":
            etabs = [pretty_name(str(row[0])) for row in results]
            if etabs:
                print(
                    f"\n🤖 Bot > Le médecin {value} exerce dans les établissements suivants :\n"
                )
                for e in etabs:
                    print(f"   • {e}")
                print()
            else:
                print(
                    f"\n🤖 Bot > Je n'ai trouvé aucun établissement pour {value}.\n"
                    f"💡 Astuce : Essayez une autre orthographe ou un autre nom.\n"
                )

        # Intention : traitements prescrits par un médecin
        elif intent == "traitements_medecin":
            traitements = [pretty_name(str(row[0])) for row in results]
            if traitements:
                print(f"\n🤖 Bot > {value} prescrit les traitements suivants :\n")
                for t in traitements:
                    print(f"   • {t}")
                print()
            else:
                print(
                    f"\n🤖 Bot > Je n'ai trouvé aucun traitement prescrit par {value}.\n"
                    f"💡 Astuce : Essayez une autre orthographe ou un autre nom.\n"
                )

        # Intention : patients avec un diagnostic donné (ex: COVID-19)
        elif intent == "patients_diagnostic":
            patients = [pretty_name(str(row[0])) for row in results]
            if patients:
                print(f"\n🤖 Bot > Les patients avec ce diagnostic sont : \n")
                for p in patients:
                    print(f"   • {p}")
                print()
            else:
                print(
                    "\n🤖 Bot > Je n'ai trouvé aucun patient ayant ce diagnostic.\n"
                    "💡 Astuce : Essayez de reformuler ou vérifiez le diagnostic demandé.\n"
                )

        else:
            print(
                "\n🤖 Bot > Pour l’instant, je peux répondre sur :\n"
                "   • les patients\n"
                "   • les établissements\n"
                "   • les traitements\n"
                "   • les diagnostics (ex : COVID-19)\n"
                "💡 Astuce : N’hésitez pas à poser une question dans ces thèmes.\n"
            )

if __name__ == "__main__":
    main()
