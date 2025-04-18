from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


urldict = {
  "videoId1": "q_TG6vNJPJE",
  "videoId2": "FAB1xEe1A1c",
  "videoId3": "4BpSUmOVr_4",
  "videoId4": "dSlxRQ_u8RE",
  "videoId5": "pe9OQaaiqNI",
  "videoId6": "enQrOaZLC70",
  "videoId7": "PQfkvC6RASA",
  "videoId8": "GtUaeNQCqmM",
  "videoId9": "QNv2aCh7MHc"
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/url/{url_id}")
async def read_item(url_id: str):
    if url_id in urldict:
        return {"item_id": url_id, "url": urldict[url_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    

@app.get("/url")
async def return_url():
    return {"urls": urldict}