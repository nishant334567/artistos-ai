from typing import Literal

from langchain_ollama import ChatOllama
from langgraph.types import Command
from pydantic import BaseModel

from app.graph.state import ArtistsState


class PlatformReleasePlan(BaseModel):
    release_platform: Literal["spotify", "apple music", "youtube music", "deezer"]
    release_strategy: str


class ReleasePlanOutput(BaseModel):
    plans: list[PlatformReleasePlan]


llm = ChatOllama(model="gemma4:latest")
structured_model = llm.with_structured_output(ReleasePlanOutput)


def release_planner(state: ArtistsState):
    print("Release planner running")
    response = structured_model.invoke(
        "You are a music release planner. "
        "Create one release plan for each platform: "
        "spotify, apple music, youtube music, and deezer. "
        "Every plan must have a concrete release_strategy "
        "tailored to that platform.\n\n"
        f"Request: {state['user_request']}"
    )
    return Command(
        update={"release_plan": response.model_dump()["plans"]},
        goto="supervisor",
    )
