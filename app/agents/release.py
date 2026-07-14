from langchain_ollama import ChatOllama
from langgraph.types import Command
from pydantic import BaseModel

from app.graph.state import ArtistsState


class ReleasePlanOutput(BaseModel):
    release_date: str
    release_type: str
    release_title: str
    release_description: str


llm = ChatOllama(model="gemma4:latest")
structured_model = llm.with_structured_output(ReleasePlanOutput)


def release_planner(state: ArtistsState):
    print("Release planner running")
    response = structured_model.invoke(
        "You are a music release planner. "
        "Fill every field with concrete values for this artist request. "
        "Pick a release date, type (single/EP/album), a clear title, "
        "and a short actionable description.\n\n"
        f"Request: {state['user_request']}"
    )
    return Command(
        update={"release_plan": response.model_dump()},
        goto="supervisor",
    )
