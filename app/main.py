from dotenv import load_dotenv

load_dotenv()

from fastapi import FastAPI
from pydantic import BaseModel

from app.graph.workflow import graph

app = FastAPI(title="ArtistOS AI")


class PlanRequest(BaseModel):
    user_request: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/plan")
def create_plan(request: PlanRequest):
    result = graph.invoke(
        {
            "user_request": request.user_request,
            "selected_agents": [],
            "release_plan": None,
            "marketing_plan": None,
            "research": None,
            "final_response": None,
        }
    )
    return {
        # "release_plan": result["release_plan"],
        # "marketing_plan": result["marketing_plan"],
        "final_response": result["final_response"],
        "status": "success",
        "message": "Plan created successfully",
    }
