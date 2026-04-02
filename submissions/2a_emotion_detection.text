import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = {"raw_document": {"text": text_to_analyze}}  # Use the function parameter here

    response = requests.post(url, json=input_json, headers=headers)
    status_code = response.status_code

    return response.text

if __name__ == "__main__":
    # Example usage:
    text_to_analyze = input("Enter your text: ")
    result = emotion_detector(text_to_analyze)
    print(result)

