from pathlib import Path

import requests

API_URL = "https://valorant-api.com/v1/agents?isPlayableCharacter=true"
OUT_DIR = Path("icons")
OUT_DIR.mkdir(exist_ok=True)

resp = requests.get(API_URL, timeout=30)
resp.raise_for_status()
agents = resp.json()["data"]

for agent in agents:
    url = agent.get("displayIcon")
    if not url:  # skip agents without an icon
        continue

    name = agent["displayName"].replace("/", "_")
    path = OUT_DIR / f"{name}.png"

    img = requests.get(url, timeout=30)
    img.raise_for_status()
    path.write_bytes(img.content)
    print(f"Saved {path}")
