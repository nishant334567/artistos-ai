from langgraph.types import Command

from app.graph.state import ArtistsState, ReleasePlan


def release_planner(state: ArtistsState):
    print("Release planner running")
    plan: ReleasePlan = {
        "release_date": "2026-07-13",
        "release_type": "single",
        "release_title": "Hua Aisa",
        "release_description": "Hua Ais is a song about two sided love",
    }
    return Command(
        update={"release_plan": plan},
        goto="marketing_planner",
    )