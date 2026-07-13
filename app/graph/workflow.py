from langgraph.graph import StateGraph, START, END

from app.graph.state import ArtistsState
from app.agents.supervisor import supervisor
from app.agents.release import release_planner
from app.agents.marketing import marketing_planner

builder = StateGraph(ArtistsState)

builder.add_node("supervisor", supervisor)
builder.add_node("release_planner", release_planner)
builder.add_node("marketing_planner", marketing_planner)


builder.add_edge(START, "supervisor")

graph = builder.compile()