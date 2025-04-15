from fastapi import FastAPI, HTTPException

app = FastAPI()


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

@app.get("/url/{item_id}")
async def read_item(item_id: str):
    if item_id in urldict:
        return {"item_id": item_id, "url": urldict[item_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")