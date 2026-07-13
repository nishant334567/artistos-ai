from langchain_ollama import ChatOllama
from langgraph.types import Command

from app.graph.state import ArtistsState, MarketingPlan

llm = ChatOllama(model="gemma4:latest")


def marketing_planner(state: ArtistsState):
    print("Marketing planner running")
    response = llm.invoke(
        "You are a music marketing planner. "
        "Given the artist request, write a short marketing plan "
        "(platform, type, title, description).\n\n"
        f"Request: {state['user_request']}"
    )
    plan: MarketingPlan = {
        "marketing_platform": "TBD",
        "marketing_type": "TBD",
        "marketing_title": "TBD",
        "marketing_description": response.content,
    }
    return Command(
        update={"marketing_plan": plan},
        goto="supervisor",
    )
