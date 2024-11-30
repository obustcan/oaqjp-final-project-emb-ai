import requests

def analyze_emotion(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock",
        "Content-Type": "application/json"
    }
    input_json = {
        "raw_document": {
            "text": text_to_analyse
        }
    }

    try:
        response = requests.post(url, headers=headers, json=input_json)
        response.raise_for_status()
        data = response.json()  # Convert the response to a dictionary

        # Extract required emotions and their scores
        emotions = data.get("emotionPredictions", {})[0].get("emotion", {})

        emotion_scores = {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0)
        }

        # Find the dominant emotion
        dominant_emotion = max(emotion_scores, key=emotion_scores.get)

        # Format the output
        result = {
            **emotion_scores,
            "dominant_emotion": dominant_emotion
        }

        return result
    except Exception as e:
        print(f"An error occurred: {e}")
        return None