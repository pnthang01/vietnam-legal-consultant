from dotenv import load_dotenv
from mirascope.core import openai, prompt_template

from test.graph_model import EntityGraph, QueriedGraph

load_dotenv()


@openai.call(model="gpt-4o-mini", response_model=QueriedGraph)
@prompt_template(
    """
    You are tasked with converting a user's natural language query into structured JSON data that reflects an entity-relation graph. 
    
    Given the following entity relationship context:
    - "Product" (Node) will "belongTo" (Edge) to "Category" (Node)
    - "InternalCategory" (Node) will "aliasAs" (Edge) to "PlatformCategory" (Node)
    - "PlatformCategory" (Node) will "belongTo" (Edge) to "Platform" (Node)
    - "Product" (Node) will also "belongTo" (Edge) to "PlatformCategory" (Node)
    - "Product" (Node) will "belongTo" (Edge) to "Brand" (Node)
    - "Brand" (Node) will "ownedBy" (Edge) to "Company" (Node)
    - "Company" (Node) will "competesWith" (Edge) to "Company" (Node)
    
    Now, given a user's query (e.g., "{query}), please:
    1. Extract and list all entities mentioned in the query.
    2. Identify the relationships between these entities based on the context provided.
    3. Output the extracted information as a JSON object following this structure:
    
    {
      "nodes": [
        {"name": "<entity_name>", "type": "Node"}
      ],
      "edges": [
        {"source": "<source_entity>", "relationship": "<relationship>", "target": "<target_entity>"}
      ]
    }
    
    If any term or relationship is ambiguous, include a note detailing the ambiguity.  

    """
)
def generate_knowledge_graph(query: str) -> openai.OpenAIDynamicConfig:
    return {"computed_fields": {"query": query}}


question = "Find me all competitors which have same category as the product with id 456 on Amazon channel?"

kg = generate_knowledge_graph(question)
print(kg)
