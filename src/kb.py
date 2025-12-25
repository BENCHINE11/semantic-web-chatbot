from rdflib import Graph

class KnowledgeBase:
    def __init__(self, path="ontology/sante.owl.ttl"):
        self.g = Graph()
        self.g.parse(path, format="turtle")

    def query(self, sparql_query: str):
        return self.g.query(sparql_query)
