from kb import KnowledgeBase

kb = KnowledgeBase()

q = """
PREFIX ont: <http://www.co-ode.org/ontologies/ont.owl#>
SELECT DISTINCT ?m WHERE {
  ?m a ont:Medecin .
}
"""
for row in kb.query(q):
    print(row[0])
