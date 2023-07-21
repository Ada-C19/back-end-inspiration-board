from flask import make_response, abort
import requests
import os

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        abort(make_response({"message":f"{model_id} invalid"}, 400))
    
    model = cls.query.get(model_id)
    if not model:
        abort(make_response({"message":f"Board {model_id} not found"}, 404))
    return model

#SLACK API
# def create_msg_slack(card):
#     slack_url = "https://slack.com/api/chat.postMessage"

#     message_body = {
#         "channel": "#in-your-f-a-c-e",
#         "text": f"Group member created a new card! Message: {card.message}"
#     }

#     headers = {
#         "Authorization": os.environ.get("SLACK_API_KEY")
#     }

#     response = requests.post(slack_url, headers=headers, json=message_body)

#     print(response.text)
        