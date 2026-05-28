

from flask import Flask, render_template, request, jsonify
from chatbot import get_response

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    reply, end_chat = get_response(user_message)

    return jsonify({
        "reply": reply,
        "end_chat": end_chat
    })


if __name__ == "__main__":
    app.run(debug=True)
