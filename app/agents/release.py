from langchain_ollama import ChatOllama
from langgraph.types import Command

from app.graph.state import ArtistsState, ReleasePlan

llm = ChatOllama(model="gemma4:latest")


def release_planner(state: ArtistsState):
    print("Release planner running")
    response = llm.invoke(
        "You are a music release planner. "
        "Given the artist request, write a short release plan "
        "(date suggestion, type, title, description).\n\n"
        f"Request: {state['user_request']}"
    )
    plan: ReleasePlan = {
        "release_date": "TBD",
        "release_type": "single",
        "release_title": "TBD",
        "release_description": response.content,
    }
    return Command(
        update={"release_plan": plan},
        goto="supervisor",
    )
