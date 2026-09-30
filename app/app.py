import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from flask import Flask, render_template, request, jsonify
from database.database import search_word
app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/search")
def api_search():
    word = request.args.get("word", "").strip()

    if not word:
        return jsonify({
            "found": False,
            "message": "Please enter a word."
        })

    result = search_word(word)

    if result:
        return jsonify({
            "found": True,
            "word": result[0],
            "category": result[1],
            "meaning": result[2]
        })

    return jsonify({
        "found": False,
        "message": f"'{word}' was not found in the VoiceLearn database."
    })


if __name__ == "__main__":
    app.run(debug=True)