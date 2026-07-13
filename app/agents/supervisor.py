from app.graph.state import ArtistsState
from langgraph.types import Command

def supervisor(state: ArtistsState):
    return Command(
        update={
            "selected_agents": [
                "release_planner",
                "marketing_planner"
            ]
        },
        goto="release_planner"
    )