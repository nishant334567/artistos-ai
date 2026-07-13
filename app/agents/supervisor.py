from app.graph.state import ArtistsState
from langgraph.types import Command
from langgraph.graph import END


def supervisor(state: ArtistsState):
    if state["release_plan"] and state["marketing_plan"]:
        return Command(goto=END)
    if state["release_plan"] and not state["marketing_plan"]:
        return Command(goto="marketing_planner")
    if state["marketing_plan"] and not state["release_plan"]:
        return Command(goto="release_planner")
    return Command(goto="release_planner")
