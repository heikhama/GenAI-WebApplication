###app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app) # This allows your HTML page to talk to this API

OLLAMA_URL = "http://localhost:11434/api/generate"

@app.route('/ask', methods=['POST'])
def ask_ollama():
    data = request.json
    user_prompt = data.get("prompt")

    payload = {
        "model": "llama3", # Ensure you have downloaded this model
        "prompt": user_prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=5000, debug=True)
