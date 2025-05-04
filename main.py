from app.api.v1.debate import router as debate_router
from fastapi import FastAPI
import uvicorn

app = FastAPI()
app.include_router(debate_router, prefix="", tags=["Moral Debate Endpoint"])

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)