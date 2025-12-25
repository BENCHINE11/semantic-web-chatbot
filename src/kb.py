from rdflib import Graph

class KnowledgeBase:
    def __init__(self):
        self.g = Graph()

        # On charge uniquement la version RDF/XML de l'ontologie
        # qui contient les classes, propriétés et individus.
        self.g.parse("ontology/sante_ontologie.rdf", format="xml")

        print(f"[KB] Graph chargé avec {len(self.g)} triplets.")

    def query(self, sparql_query: str):
        return self.g.query(sparql_query)
