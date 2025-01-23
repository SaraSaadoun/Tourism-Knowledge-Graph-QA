from config import Config
from Neo4jClient import Neo4jClient
from WikidataClient import WikidataSPARQL
from DataLoader import DataLoader

Config.validate()

wikidata_client = WikidataSPARQL()
neo4j_client = Neo4jClient()

data_loader = DataLoader(wikidata_client, neo4j_client)

print('start touristic data loading..', flush=True)
data_loader.load_touristic_attractions()
print('finished touristic data loading.', flush=True)
print('--------------------------------', flush=True)

print('start countries data loading..', flush=True)
data_loader.load_countries()
print('finished countries data loading.', flush=True)
print('--------------------------------', flush=True)


print('start creating relationships..', flush=True)
data_loader.create_relationships()
print('finished creating relationships.', flush=True)
print('--------------------------------', flush=True)

