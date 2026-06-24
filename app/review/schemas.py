from pydantic import BaseModel


class ReviewRequest(BaseModel):
    supervisor_id: int
    final_decision: str