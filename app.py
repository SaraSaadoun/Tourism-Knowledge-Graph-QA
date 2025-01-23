from langchain_groq import ChatGroq
from langchain_neo4j import GraphCypherQAChain, Neo4jGraph
import gradio as gr
from config import Config


Config.validate()

graph = Neo4jGraph(url=Config.NEO4J_URI, username=Config.NEO4J_USERNAME, password=Config.NEO4J_PASSWORD)
llm=ChatGroq(model_name='gemma2-9b-it')
chain=GraphCypherQAChain.from_llm(llm=llm, graph=graph, allow_dangerous_requests=True)

def get_answer(question):
    result = chain.invoke({'query': question})['result']
    return result

app = gr.Interface(
    fn=get_answer,
    inputs=['text'],
    outputs=['text'],
    title='Ask me sth about Touristic Places :)',
)

app.launch()

