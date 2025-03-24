from pydantic import BaseModel, Field


class Edge(BaseModel):
    source: str = Field(..., description="The source node of the edge")
    target: str = Field(..., description="The target node of the edge")
    relationship: str = Field(
        ..., description="The relationship between the source and target nodes"
    )


class Node(BaseModel):
    id: str = Field(..., description="The unique identifier of the node")
    type: str = Field(..., description="The type or label of the node")
    properties: dict | None = Field(
        ..., description="Additional properties and metadata associated with the node"
    )


class EntityGraph(BaseModel):
    nodes: list[Node] = Field(..., description="List of nodes in the entity graph")
    edges: list[Edge] = Field(..., description="List of edges in the entity graph")


class QueriedGraph(BaseModel):
    queried_graph: EntityGraph = Field(..., description="The generated entity graph based on the user query")
    target_graph: EntityGraph = Field(..., description="The target entity graph to retrieve information from")