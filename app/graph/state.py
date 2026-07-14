from typing import TypedDict


class ReleasePlan(TypedDict):
    release_platform: str
    release_strategy: str


class MarketingPlan(TypedDict):
    platform: str
    marketing_type: str
    marketing_title: str
    marketing_description: str


class ArtistsState(TypedDict):
    user_request: str
    selected_agents: list[str]
    release_plan: list[ReleasePlan] | None
    marketing_plan: list[MarketingPlan] | None
    final_response: str | None
