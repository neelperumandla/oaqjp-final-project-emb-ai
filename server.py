"""Flask server for Emotion Detection Application."""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/emotionDetector')
def emo_det():
    """
    Endpoint to analyze the emotion in a given text.
    Returns formatted emotion scores and dominant emotion,
    or an error message for invalid input.
    """

    text = request.args.get('textToAnalyze')

    res = emotion_detector(text)
    if res['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (f"For the given statement, the system response is "
        f"'anger': {res['anger']}, 'disgust': {res['disgust']}, "
        f"'fear': {res['fear']}, 'joy': {res['joy']} and 'sadness': {res['sadness']}. "
        f"The dominant emotion is {res['dominant_emotion']}.")

@app.route('/')
def index():
    """
    Serves the main HTML page.
    """

    return render_template('index.html')


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=5000)
    