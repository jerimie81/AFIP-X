from fastapi import FastAPI
import requests
import json
import os

app = FastAPI()

FIRMWARE_QUEUE = "http://kafka:9092"

@app.get("/scrape/{model}")
def scrape_firmware(model: str):

    sources = [
        f"https://samfw.com/firmware/{model}",
        f"https://samfrew.com/model/{model}/"
    ]

    results = []

    for src in sources:
        try:
            r = requests.get(src)
            if r.status_code == 200:
                results.append({"source": src})
        except:
            pass

    # simulate queue push
    with open("/data/queue.json", "w") as f:
        json.dump(results, f)

    return {"queued": results}
