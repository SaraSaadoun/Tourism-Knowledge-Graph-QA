from SPARQLWrapper import SPARQLWrapper, JSON

class WikidataSPARQL:
    def __init__(self, endpoint_url="https://query.wikidata.org/sparql"):
        self.endpoint_url = endpoint_url
        self.sparql = SPARQLWrapper(self.endpoint_url)
    
    def query(self, sparql_query):
        self.sparql.setQuery(sparql_query)
        self.sparql.setReturnFormat(JSON)
        try:
            response = self.sparql.query().convert()
            return response["results"]["bindings"]
        except Exception as e:
            print(f"Error executing SPARQL query: {e}")
            return []

# SPARQL queries to retrieve data





