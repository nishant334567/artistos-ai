from langchain_ollama import ChatOllama
from langgraph.types import Command
from pydantic import BaseModel
from app.graph.state import ArtistsState

class MarketingPlanOutput(BaseModel):
    marketing_platform: str
    marketing_type: str
    marketing_title: str
    marketing_description: str

llm = ChatOllama(model="gemma4:latest")
structured_model = llm.with_structured_output(MarketingPlanOutput)


def marketing_planner(state: ArtistsState):
    print("Marketing planner running")
    response = structured_model.invoke(
        "You are a music marketing planner. "
        "Fill every field with concrete values for this artist request. "
        "Pick a primary platform, campaign type, a clear title, "
        "and a short actionable description.\n\n"
        f"Request: {state['user_request']}"
    )
    return Command(
        update={"marketing_plan": response.model_dump()},
        goto="supervisor",
    )
