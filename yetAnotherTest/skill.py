# -*- coding: utf-8 -*-
#import requests
import re
import json




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
    print "Starting new session."


def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "greeting":
        return helloyou(intent)
    elif intent_name == "badday":
        return badday(intent)
    elif intent_name == "goodday":
        return goodday(intent)
        
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    print "Ending session."
    # Cleanup goes here...


def handle_session_end_request():
    card_title = "TITLE"
    speech_output = "Thank you, see you next time!"
    should_end_session = True

    return build_response({}, build_speechlet_response(card_title, speech_output, None, should_end_session))


def get_welcome_response():
    session_attributes = {}
    card_title = "Hello, welcome to the how's your day skill."
    speech_output = "Hello, welcome to the how's your day skill."
    reprompt_text = "Are you still there?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def helloyou(intent):
    #print "Got Domain Intent"
    session_attributes = {}
    card_title = "How are you"
    speech_output = "How you doing?"
    reprompt_text = "Are you still there?  "
    should_end_session = False
    print str(intent)
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))
    
    
def goodday(intent):
    session_attributes = {}
    card_title = "Glad to hear that!"
    speech_output = "Glad to hear that!"
    reprompt_text = "Are you still deciding?"
    should_end_session = True
    print str(intent)
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))

def badday(intent):
    session_attributes = {}
    card_title = "Hope your day gets better!"
    speech_output = "Hope your day gets better!"
    reprompt_text = "Are you still deciding?"
    should_end_session = True
    print str(intent)
    return build_response(session_attributes, build_speechlet_response(
    card_title, speech_output, reprompt_text, should_end_session))


