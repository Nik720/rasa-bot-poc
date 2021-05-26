# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from main import findData
from rasa_sdk.events import SlotSet


# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionGetResponse(Action):

    def name(self) -> Text:
        return "action_get_response"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        sunbird_object = tracker.get_slot('sunbird_object')
        responseObj = ""
        try:
            if sunbird_object == '' or sunbird_object == 'empty':
                intentKey = 'start'
            else:
                intentKey = sunbird_object
            responseObj = findData(intentKey)
            dispatcher.utter_message(custom=responseObj)
        except:
            dispatcher.utter_message(custom={'text': "Sorry not found! Try Again"})

        return [SlotSet("sunbird_object", "")]
