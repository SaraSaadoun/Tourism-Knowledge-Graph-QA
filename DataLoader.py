
class DataLoader:
    def __init__(self, wikidata_client, neo4j_client):
        self.wikidata_client = wikidata_client
        self.neo4j_client = neo4j_client
        self.touristic_attraction_query = """
            SELECT DISTINCT ?place ?placeLabel ?country ?countryLabel ?type ?typeLabel   
                ?length ?width ?area 
            WHERE {
            ?place wdt:P31 wd:Q570116.  # Find all tourist attractions
            ?place wdt:P17 ?country.   # Optional: Country
            ?place wdt:P31 ?type.   # Optional: Type of place
            ?place wdt:P2043 ?length .
            ?place wdt:P2049 ?width . 
            ?place wdt:P2046 ?area . 
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }
            LIMIT 500
        """
        self.country_query = """
            SELECT DISTINCT ?country ?countryLabel ?continentLabel ?capitalLabel ?languageLabel 
            ?stateHeadLabel ?population
            WHERE {
            ?country wdt:P31 wd:Q6256.  # Find all countries
            ?country wdt:P37 ?language .  # Language
            ?country wdt:P30 ?continent .  # Continent
            ?country wdt:P36 ?capital .  # Capital
            ?country wdt:P35 ?stateHead .  # Head of state
            ?country wdt:P1082 ?population .  # Population
            SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
            }
            LIMIT 600
        """
        self.country_ids = []
        self.touristic_attraction_ids = []

    def load_touristic_attractions(self):
        delete_all_attractions_query = "MATCH (n:TouristicAttraction) DETACH DELETE n"
        self.neo4j_client.execute_query(delete_all_attractions_query)
        print('all attractions are deleted.', flush=True)

        attractions_data = self.wikidata_client.query(self.touristic_attraction_query)
        for attraction in attractions_data:
            properties = {
                "id": attraction["place"]["value"].split("/")[-1],
                "place": attraction["placeLabel"]["value"],
                "country": attraction.get("countryLabel", {}).get("value", ""),
                "country_id": attraction.get("country", {}).get("value", "").split("/")[-1],
                "type": attraction.get("typeLabel", {}).get("value", ""),
                "length": attraction.get("length", {}).get("value", ""),
                "width": attraction.get("width", {}).get("value", ""),
                "area": attraction.get("area", {}).get("value", "")
            }
            self.neo4j_client.create_node("TouristicAttraction", properties)
            self.touristic_attraction_ids.append(properties["country_id"])

    def load_countries(self):
        delete_all_countries_query = "MATCH (n:Country) DETACH DELETE n"
        print('all countries are deleted.', flush=True)
        self.neo4j_client.execute_query(delete_all_countries_query)
        countries_data = self.wikidata_client.query(self.country_query)
        for country in countries_data:
            properties = {
                "id": country["country"]["value"].split("/")[-1],
                "country": country["countryLabel"]["value"],
                "continent": country.get("continentLabel", {}).get("value", ""),
                "capital": country.get("capitalLabel", {}).get("value", ""),
                "language": country.get("languageLabel", {}).get("value", ""),
                "stateHead": country.get("stateHeadLabel", {}).get("value", ""),
                "population": country.get("population", {}).get("value", "")
            }
            self.neo4j_client.create_node("Country", properties)
            self.country_ids.append(properties["id"])

    def create_relationships(self):
        print('length of attractions: %d' % len(self.touristic_attraction_ids))
        print('length of countries: %d' % len(self.country_ids))
        self.neo4j_client.create_relationship("LOCATED_IN")



