import requests
import json
from config import OLLAMA_URL, MODEL_NAME

def generate_response(prompt, stream=True):
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": stream
    }

    if stream:
        with requests.post(OLLAMA_URL, json=payload, stream=True) as r:
            for line in r.iter_lines():
                if line:
                    data = json.loads(line)
                    yield data.get("response", "")
    else:
        r = requests.post(OLLAMA_URL, json=payload)
        return r.json()["response"]
