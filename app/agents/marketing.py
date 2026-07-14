from typing import Literal

from langchain_ollama import ChatOllama
from langgraph.types import Command
from pydantic import BaseModel

from app.graph.state import ArtistsState


class PlatformPlan(BaseModel):
    platform: Literal["youtube", "tiktok", "instagram", "facebook"]
    marketing_type: str
    marketing_title: str
    marketing_description: str


class MarketingPlanOutput(BaseModel):
    plans: list[PlatformPlan]


llm = ChatOllama(model="gemma4:latest")
structured_model = llm.with_structured_output(MarketingPlanOutput)


def marketing_planner(state: ArtistsState):
    print("Marketing planner running")
    response = structured_model.invoke(
        "You are a music marketing planner. "
        "Create one marketing plan for each platform: "
        "youtube, tiktok, instagram, and facebook. "
        "Every plan must have concrete type, title, and a short actionable description "
        "tailored to that platform.\n\n"
        f"Request: {state['user_request']}"
    )
    return Command(
        update={"marketing_plan": response.model_dump()["plans"]},
        goto="supervisor",
    )
