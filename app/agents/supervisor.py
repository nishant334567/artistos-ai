from typing import Literal

from langgraph.graph import END
from langgraph.types import Command
from pydantic import BaseModel

from app.graph.state import ArtistsState
from app.llm import llm


class SupervisorDecision(BaseModel):
    next_agent: Literal["release_planner", "marketing_planner", "final_response", "FINISH"]
    reason: str


structured_model = llm.with_structured_output(SupervisorDecision)


def supervisor(state: ArtistsState):
    response = structured_model.invoke(
        f"""You are supervisor. Based on the user query and current plans, choose ONE next agent.

Agents:
- release_planner: if query is strictly related to releasing, distribution, or streaming platforms
- marketing_planner: if query is strictly related to marketing, promotion, social strategy, or growth
- final_response: if all requested work is done
- FINISH: only if final_response is generated and all requested work is done

Rules:
1. Never choose an agent whose plan already exists or is not needed.
4. If only one type was requested and that plan exists, choose FINISH.

User query: {state["user_request"]}
Release plan: {state["release_plan"]}
Marketing plan: {state["marketing_plan"]}
Final response: {state["final_response"]}

Choose next_agent and briefly explain why in reason.
"""
    )

    next_agent = response.next_agent



    if next_agent == "FINISH":
        return Command(goto=END)
    return Command(
        update={"selected_agents": [next_agent]},
        goto=next_agent,
    )

