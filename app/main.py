from dotenv import load_dotenv
from fastapi import FastAPI
from pydantic import BaseModel

from app.graph.workflow import graph

load_dotenv()

app = FastAPI(title="ArtistOS AI")


class PlanRequest(BaseModel):
    user_request: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/plan")
def create_plan(request: PlanRequest):
    return graph.invoke(
        {
            "user_request": request.user_request,
            "selected_agents": [],
            "release_plan": None,
            "marketing_plan": None,
            "final_response": None,
        }
    )
