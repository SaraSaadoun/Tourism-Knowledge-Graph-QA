from langchain_neo4j import Neo4jGraph
from config import Config

class Neo4jClient:
    def __init__(self):
        self._uri = Config.NEO4J_URI
        self._username = Config.NEO4J_USERNAME
        self._password = Config.NEO4J_PASSWORD
        self.graph = None
        self._connect()

    def _connect(self):
        try:
            self.graph = Neo4jGraph(url=Config.NEO4J_URI, username=Config.NEO4J_USERNAME, password=Config.NEO4J_PASSWORD)
            print("Successfully connected to Neo4j!")
        except Exception as e:
            raise ConnectionError(f"Failed to connect to Neo4j: {e}")


    def execute_query(self, query:str, parameters:dict=None)->list:
        if not parameters:
            parameters = {}
        try:
            result = self.graph.query(query, params=parameters)
            return result
        except Exception as e:
            raise Exception(f"Error executing query: {e}")

    def create_node(self, label:str, properties:dict)->list:
        query = f"CREATE (n:{label} {{ {', '.join([f'{key}: ${key}' for key in properties])} }}) RETURN n"
        return self.graph.query(query, properties)

    def get_all_nodes(self, label:str)->list:

        query = f"MATCH (n:{label}) RETURN n"
        return self.graph.query(query)

    def create_relationship(self, relationship_type:str)->list:
        query = """
        match (x:TouristicAttraction), (y:Country)
        WHERE y.id = x.country_id
        CREATE (x) -[r:LOCATED_AT]->(y)
        return r
        """
        return self.graph.query(query)

