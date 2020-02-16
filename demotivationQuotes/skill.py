# -*- coding: utf-8 -*-
# import requests
import json
from botocore.vendored import requests
from random import randint

API_ENDPOINT = "https://api.paperquotes.com/apiv1/quotes?tags=absurd&limit=10"
API_TOKEN = "eaf226c49651532a317c53f7cb42cff8686be774"
HEADERS = {'Authorization': 'TOKEN {}'.format(API_TOKEN)}
pullQuotes = {}


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        "outputSpeech": {
            "type": "PlainText",
            "text": output
        },
        "card": {
            "type": "Simple",
            "title": title,
            "content": output
        },
        "reprompt": {
            "outputSpeech": {
                "type": "PlainText",
                "text": reprompt_text
            }
        },
        "shouldEndSession": should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        "version": "1.0",
        "sessionAttributes": session_attributes,
        "response": speechlet_response

    }


def lambda_handler(event, context):
    # if event["session"]["application"]["applicationId"] != "amzn1.ask.skill.85f2eb3b-7085-483f-b71f-20042600b163":
    #	raise ValueError("Wrong application")
    if event["session"]["new"]:
        on_session_started({"requestId": event["request"]["requestId"]}, event["session"])

    if event["request"]["type"] == "LaunchRequest":
        return on_launch(event["request"], event["session"])
    elif event["request"]["type"] == "IntentRequest":
        return on_intent(event["request"], event["session"])
    elif event["request"]["type"] == "SessionEndedRequest":
        return on_session_ended(event["request"], event["session"])


def on_session_started(session_started_request, session):
    print
    "Starting new session."


def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "yesanswer":
        return helloyou(intent)
    elif intent_name == "noanswer":
        return badday(intent)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    print
    "Ending session."
    # Cleanup goes here...


def handle_session_end_request():
    card_title = "TITLE"
    speech_output = "Have a good night, Danny!"
    should_end_session = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


def get_welcome_response():
    session_attributes = {}
    card_title = "Welcome to the abusrd quote skill. Here, you will be read a random absurd quote! Would you like to hear the quote now?"
    speech_output = """Welcome to the absurd quote skill. Here you will be read a 
    random absurd quote. Would you like to hear the quote now?"""
    reprompt_text = "Are you ready?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def helloyou(intent):
    session_attributes = {}
    l = get_my_quote(API_ENDPOINT, HEADERS)
    card_title = "{}".format(l)
    speech_output = "{}".format(l)
    reprompt_text = "Are you ready?"
    should_end_session = True
    print
    str(intent)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def badday(intent):
    session_attributes = {}
    card_title = "What a shame"
    speech_output = "Well, that was a waste of a launch, wasn't it. Just kidding; I love you!"
    reprompt_text = "Got here"
    should_end_session = True
    print
    str(intent)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))

def get_my_quote(endpoint, headers):
    r = requests.get(endpoint, headers=headers)
    quotes = r.json()  # ['results']
    i = 0
    for each in quotes['results']:
        i += 1
        d = {i: each['quote']}
        pullQuotes.update(d)
    j = randint(1, 23)
    return pullQuotes[j]
