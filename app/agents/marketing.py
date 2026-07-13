from langgraph.graph import END
from langgraph.types import Command

from app.graph.state import ArtistsState, MarketingPlan


def marketing_planner(state: ArtistsState):
    print("Marketing planner running")
    plan: MarketingPlan = {
        "marketing_platform": "youtube",
        "marketing_type": "social media",
        "marketing_title": "Hua Aisa",
        "marketing_description": "Hua Aisa is a song about two sided love",
    }
    return Command(
        update={"marketing_plan": plan},
        goto=END,
    )
