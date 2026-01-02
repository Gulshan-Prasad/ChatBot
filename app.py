from flask import Flask, request, jsonify, url_for, render_template
import requests
import json


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ai", methods=["POST"])
def ai():
    prompt = request.json["prompt"]

    response = requests.post(
      url="https://openrouter.ai/api/v1/chat/completions",
      headers={
        "Authorization": "Bearer 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",
        "Content-Type": "application/json",
        },
  
      data=json.dumps({
        "model": "google/gemma-3-27b-it:free",
        "messages": [
          {
            "role": "user",
            "content": f"{prompt}\n\nReply like You are a Roblox player chatting in Roblox in-game chat. Follow Roblox chat rules: keep messages short, casual, friendly, and safe. Avoid profanity, adult topics, hate, violence, or sensitive content. Use simple words like a normal Roblox player."
          }
        ]
      })
    )

    data = response.json()

    return jsonify({
        "text": data["choices"][0]["message"]["content"]
    })

@app.route("/app")
def mainApp():
    return 'hello, world'

@app.route("/user/<username>")
def profile(username):
    return f'{username}\'s profile'

