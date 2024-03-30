from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

@app.get("/api/query/{query}")
async def read_query(query: str):
    return [{
        "docId": "doc1",
        "contents": "This is a document.",
        "score": 0.5
    }]

# Mount the static site folder
app.mount("/",
        StaticFiles(directory="frontend/out", html=True),
        name="static")