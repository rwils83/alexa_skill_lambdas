# -*- coding: utf-8 -*-
# import requests
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
    print
    "Starting new session."


def on_launch(launch_request, session):
    return get_welcome_response()


def on_intent(intent_request, session):
    intent = intent_request["intent"]
    intent_name = intent_request["intent"]["name"]

    if intent_name == "greeting":
        return helloyou(intent)
    elif intent_name == "badday":
        return badday(intent)
    elif intent_name == "fangtastic":
        return fangtastic(intent)

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
    card_title = "Hello, Danny. I am going to read you a book!. What book would you like to hear?"
    speech_output = "Hello, Danny, I am going to read you a book!. What book would you like to hear?"
    reprompt_text = "Are you ready?"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def helloyou(intent):
    # print "Got Domain Intent"
    session_attributes = {}
    card_title = "What book should I read?"
    speech_output = "What book should I read?"
    reprompt_text = "Are you ready?  "
    should_end_session = False
    print
    str(intent)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def fangtastic(intent):
    session_attributes = {}
    card_title = "Fangtastic"
    speech_output = """I will read you Fangtastic, by Disney."
    Henry Hugglemonster loves mornings! He turns off his roaring alarm clock, does some monster stretches, and then stomps off to start a brand new day. 
    It's really important for monsters to have a good wake-up routine Henry tells his monster dog, Beckett. 
    I start by washing up." Henry closes his eyes and covers his face with soap suds. 
    But, when he reaches for his towel, he grabs Beckett by mistake. 
    "Now comes the part I like best says Henry. Brushing my fangs!"
    "Henry squeezes some fangpaste onto his fangbrush and starts brushing. But something feels different." He puts the fang brush down and wiggles one of his fangs. 
    "ITS LOOSE! 
    Henry runs downstairs to tell his parents the good news. Momma tells henry about the Fang Monster. 
    She flies into your room at night, takes your baby fang from under your pillow, and leaves you a special gift. 
    A special gift? Roarsome! roars henry. He wants his fang to fall out right away. 
    Henry's mother has an idea. She pours super-sticky monster molasses over his monstercakes. 
    After just one bite, Henry's loose fang pops out. 
    It worked! shouts henry. And it didn't even hurt! 
    Way to go kiddo says daddo. 
    Henry is so happy he wants to roar. but all that comes out is a little whistle. He tries again and the same thing happens. 
    When henry lost his fang, he also lost his roar. Oh no henry cries. my roar is my best thing. It's what makes me Henry Hugglemonster. 
    Daddo explains to henry that monster fangs grow back quickly. Before you know it, you'll have your roar back. and a brand new big monster fang. 
    Henry is sad. He leaves the kitchen and runs into his sister in the hallway. 
    You're just the monster I was looking for. Summer says. I have your costume right here. 
    She reminds Henry that he is supposed to play the roaring lion in her new play. You're perfect for this part. 
    Without his roar, Henry doesn't feel perfect at all. 
    Summer puts the cosume on her brother so they can practice their big duet. He's the king the jungle, royal to the core. but the coolest thing of all is great big lion roar, sings Summer. 
    But as henry opens his mouth to roar, the doorbell rings. 
    He slips out of the costume and rushes off to see who is there. Denzel, Gertie, and Estelle have come invite Henry to play Huggleball with them. 
    Henry loves Huggleball. All you have to do is catch, throw, and run. No roaring required!
    Sorry Summer. I can't let down my friends. They need me, he tells his sister, and he heads out the door. The four friends run to the yardand start playing. 
    Before long Henry scores the first goal. The monsters let out a big roar! But not Henry. You didn't do the score roar,Denzel says to Henry. 
    When somebody scores, we all roar, Gertie reminds him. Henry is worried his friends will laugh at his whistle.
    So instead, he picks up the huggleball and keeps playing. Gertie runs to block Henry by standing between him and the goal, but nothing
    can stop Henry Hugglemonster! He leaps over Gertie and scores again. Henry feels great. This time he joins his friends for the Score Roar.....and lets out a whistle. 
    Estelle, Denzel, and Gertie all turn to stare at Henry. Henry is embarrased. But his friends love the whistle. 
    I've always wanted to whistle but never could, Denzel admits. 
    Can you do it again, Gertie asks. 
    Do it again. Do it again Estelle chants. 
    When Henry whistles again, Beckett runs over and does a flip. that is so cool says Estelle. 
    I thought you were all going to laugh at me when you found out I lost my roar, Henry admits. 
    Don't be silly, Denzel tells him. We're your best friends. 
    Henry keeps whistling and Beckett keeps flipping. 
    Soon, Summer comes outside. What's going on, she asks. 
    Henry finally tells his sister that he lost his roar.All I can do is this.... He whistles, and Beckett flips. I can't be the Roaring Lion in your play, but I could be a whistling lion. 
    Summer loves that idea. 
    Later that day, Henry's family and freinds gather to watch Summer's play. the whistling lion and his flipping lion cub are a big hit. 
    Momma is glad to see that Henry is feeling better about losing his roar. 
    Henry puts his arms around Gertie, Denzel, and Estelleand tells her, That's because I've got the most roarsome friends in the world. 
    That night, as Henry brushes his teeth, he sees a brand new fang already growing in. 
    Daddo was right, monster fangs do grow really fast! Then Henry lets out a big Roar. My roar is back! Wahoooo, he cheers.
    After such a roarsome day, Henry has a monstrously good night's sleep. The end"""
    reprompt_text = "Are you ready?"
    should_end_session = True
    print
    str(intent)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def badday(intent):
    session_attributes = {}
    card_title = "Hope your day gets better!"
    speech_output = "Hope your day gets better!"
    reprompt_text = "Are you still deciding?"
    should_end_session = True
    print
    str(intent)
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


