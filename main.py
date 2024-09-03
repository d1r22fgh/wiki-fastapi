from fastapi import FastAPI
import uvicorn
import nltk

nltk.download("punkt_tab")

from mylib.logic import search_wiki
from mylib.logic import phrase as wiki_phrases
from mylib.logic import wiki as wikilogic

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Wikipedia API. Call / Search / Wiki"}


@app.get("/search/{value}")
async def search(value: str):
    """Page to search in wikipedia"""

    result = search_wiki(value)
    return {"result": result}


@app.get("/wiki/{name}")
async def wiki(name: str):
    """Retrieve Wikipedia Page"""

    result = wikilogic(name)
    return {"result": result}


@app.get("/phrase/{name}")
async def phrase(name: str):
    """Retrieve Wikipedia Page"""

    result = wiki_phrases(name)
    return {"result": result}


# if __name__ == "__main__":
#     uvicorn.run(app, port=8000, reload="True")
