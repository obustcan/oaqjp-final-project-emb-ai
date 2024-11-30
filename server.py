from flask import Flask, make_response, request
from EmotionDetection import analyze_emotion

app = Flask(__name__)

@app.route("/emotionDetector", methods=['POST'])
def emotion_detection():
    data = request.get_json()
    status_code = 200
    result = {}
    formatted_response = ''

    if not data or "text" not in data:
        status_code = 400
    else:
        text = data["text"]
        result = analyze_emotion(text)

    if result.get('dominant_emotion', None) is None:
        formatted_response = 'Invalid text! Please try again!'
    else:
        formatted_response = (
            f"For the given statement, the system response is "
            f"'anger': {result.get('anger'), 'None'}, 'disgust': {result.get('disgust', 'None')}, "
            f"'fear': {result.get('fear', 'None')}, 'joy': {result.get('joy', 'None')} and "
            f"'sadness': {result.get('sadness', 'None')}. "
            f"The dominant emotion is {result.get('dominant_emotion', 'None')}."
        )
    return {"response": formatted_response}, status_code

if __name__ == "__main__":
    app.run(debug=True)