from typing import TypedDict


class ReleasePlan(TypedDict):
    release_date: str
    release_type: str
    release_title: str
    release_description: str


class MarketingPlan(TypedDict):
    marketing_platform: str
    marketing_type: str
    marketing_title: str
    marketing_description: str


class ArtistsState(TypedDict):
    user_request: str
    selected_agents: list[str]
    release_plan: ReleasePlan | None
    marketing_plan: MarketingPlan | None
    final_response: str | None
