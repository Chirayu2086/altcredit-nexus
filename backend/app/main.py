from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers.score_router import router as score_router

app = FastAPI(
    title="AltCredit Nexus",
    description="Privacy-First AI Credit Scoring Platform",
    version="1.0.0"
)

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to specific domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(score_router, prefix="/api")

@app.get("/")
async def root():
    return {
        "message": "✅ AltCredit Nexus API is running!",
        "docs": "/docs",
        "version": "1.0.0"
    }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
