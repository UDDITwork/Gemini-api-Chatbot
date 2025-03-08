# app.py
from flask import Flask, render_template, request, jsonify
from main import get_response

app = Flask(__name__)

@app.route("/")
def index():
    # Render the HTML template with a chat interface
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    # Receive the user's prompt via JSON
    data = request.get_json()
    user_input = data.get("prompt", "")
    
    if not user_input:
        return jsonify({"response": "No prompt provided."})
    
    # Use the same function from main.py to get the model's response
    bot_response = get_response(user_input)
    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)
