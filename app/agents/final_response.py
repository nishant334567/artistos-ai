from langgraph.types import Command
from pydantic import BaseModel
from app.llm import llm
from app.graph.state import ArtistsState

class FinalResponse(BaseModel):
    final_response: str

def final_response(state: ArtistsState):
    response = llm.invoke(
        f"""You are final response. Summarize for the user.
Use concrete tactics from Research when present (do not invent sources).

User query: {state["user_request"]}
Release plan: {state["release_plan"]}
Marketing plan: {state["marketing_plan"]}
Research: {state["research"]}
"""
    )
    return Command(update={"final_response": response.content}, goto="supervisor")