from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

rv_dict = {
    "videoId1": {
        "id": "q_TG6vNJPJE",
        "title": "Train Simulator World - AWVR 777 Unstoppable Train Challenge"
    },
        "videoId2": {
        "id": "FAB1xEe1A1c",
        "title": "I Bought 10 Trailers In ETS2!"
    },
        "videoId3": {
        "id": "4BpSUmOVr_4",
        "title": "Victory Day, but its in War Thunder"
    },
        "videoId4": {
        "id": "dSlxRQ_u8RE",
        "title": "Ivanovo Besnilo (presmješno)"
    },
        "videoId5": {
        "id": "pe9OQaaiqNI",
        "title": "TWITCH GIRL KICKED FROM GAME! - CS GO Funny Moments"
    },
        "videoId6": {
        "id": "enQrOaZLC70",
        "title": "I1van - PJESMA ZA IVANČETA (Cosmitaur Remix)"
    },
        "videoId7": {
        "id": "PQfkvC6RASA",
        "title": "SpaceX Starship - Reentry"
    },
        "videoId8": {
        "id": "GtUaeNQCqmM",
        "title": "Space Shuttle Landing - Without Reading The Manual"
    },
        "videoId9": {
        "id": "QNv2aCh7MHc",
        "title": "Simulacija Nuklearne Rakete"
    },
}

home_dict = {
    "videoId1": {
        "id": "1weAWiePcsQ",
        "title": "A map of all steam users… Part 3"
    },
        "videoId2": {
        "id": "GtUaeNQCqmM",
        "title": "Space Shuttle Landing - Without Reading The Manual"
    },
        "videoId3": {
        "id": "dSlxRQ_u8RE",
        "title": "Ivanovo Besnilo (presmješno)"
    },
        "videoId4": {
        "id": "PQfkvC6RASA",
        "title": "SpaceX Starship - Reentry"
    },
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/url/{url_id}")
async def read_item(url_id: str):
    if url_id in rv_dict:
        return {"item_id": url_id, "url": rv_dict[url_id]}
    else:
        raise HTTPException(status_code=404, detail="Item not found")
    

@app.get("/rvvideos")
async def return_url():
    return {"rv_videos": rv_dict}

@app.get("/homevideos")
async def return_url():
    return {"home_videos": home_dict}