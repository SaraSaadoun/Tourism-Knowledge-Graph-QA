# Tourism Knowledge Graph QA 🌍🗺️

A question-answering system about tourist places and countries using a Neo4j knowledge graph powered by Wikidata data.

## Screenshots:
1. Gradio App Interface:
   
![Screenshot (649)](https://github.com/user-attachments/assets/ff01e2a8-abcb-433a-bb0f-9be097e27dbe)

2. Neo4j Graph Database:

![Screenshot (651)](https://github.com/user-attachments/assets/bbf0c4c1-f938-4a3b-a4e4-c2018491f4a0)


## Features
- 🏞️ Small curated dataset of 500+ touristic attractions and 600+ countries
- 🔗 Relationship mapping (LOCATED_IN) between attractions and countries
- 💬 Natural language query interface using Gemma-2B LLM
- 📊 Extended properties including geographical metrics and demographic data

## Dataset Structure
**Nodes:**
- `TouristicAttraction`: Name, type, dimensions (length/width/area)
- `Country`: Continent, capital, language, population

**Relationship:**
- `(Attraction)-[LOCATED_IN]->(Country)`

## 🛠️ Tools & Libraries
- **Graph Database**: Neo4j
- **LLM Integration**: LangChain + Groq API (Gemma-2B)
- **Data Sources**: Wikidata SPARQL API
- **UI Framework**: Gradio
- **Core Libraries**: 
  - `langchain_neo4j` - Neo4j graph integration
  - `langchain_groq` - LLM inference
  - `python-dotenv` - Environment management
  - `SPARQLWrapper` - Wikidata query interface

## 🚀 Installation & Setup

### Create environment
```bash
conda create -n kg python=3.11 -y
conda activate kg-env
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Configure environment
```bash
echo "NEO4J_URI='uri'
NEO4J_USERNAME='neo4j'
NEO4J_PASSWORD='your_password_here'
GROQ_API_KEY='your_groq_key_here'" > .env
```
### Run application
```bash
python app.py
```
### Access Interface
Visit http://127.0.0.1:7860/ in your browser
