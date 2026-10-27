
"""Flask application for the Emotion Detector."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)


@app.route("/")
def render_index_page():
    """Render the main application page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def sent_analyzer():
    """Analyze input text and return its detected emotions."""
    text_to_analyze = request.args.get("textToAnalyze", "")

    if not text_to_analyze.strip():
        return "Invalid input! Please enter a statement.", 400

    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Emotion service is unavailable. Please try again later.", 503

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
