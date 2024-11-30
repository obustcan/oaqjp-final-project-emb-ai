from flask import Flask, make_response, request
from EmotionDetection import analyze_emotion

app = Flask(__name__)

@app.route("/emotionDetector/<query>")
def emotion_detection(query):
    result = analyze_emotion(query)
    formatted_response = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )
    return {"response": formatted_response}, 200

if __name__ == "__main__":
    app.run(debug=True)