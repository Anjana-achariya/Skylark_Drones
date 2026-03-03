from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from agent import run_agent

app = FastAPI(title="Monday BI Agent")

# allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Monday BI Agent running 🚀"}

@app.get("/ask")
def ask_agent(q: str):
    print("\n==============================")
    print(" New Query:", q)

    answer = run_agent(q)

    return {
        "query": q,
        "answer": answer,
        "status": "success"
    }