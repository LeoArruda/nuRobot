from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core.actions.action import Action
from rasa_core.events import SlotSet
from rasa_core.events import AllSlotsReset
from rasa_core.events import Restarted
# from pymongo import MongoClient
# client = MongoClient('mongodb://localhost:27017')
# db = client['local']

class ActionWeather(Action):
    def name(self):
        return 'action_weather'

    def run(self, dispatcher, tracker, domain):
        from apixu.client import ApixuClient
        api_key = '1499cd68946d4387b6c175525181806'  # your apixu key
        client = ApixuClient(api_key)

        loc = tracker.get_slot('location')
        current = client.getCurrentWeather(q=loc)

        country = current['location']['country']
        city = current['location']['name']
        condition = current['current']['condition']['text']
        temperature_c = current['current']['temp_c']
        feelslike_c = current['current']['feelslike_c']
        humidity = current['current']['humidity']
        wind_kph = current['current']['wind_kph']

        response = """It is currently {} in {}/{} at the moment. \nThe temperature is {} oC feels like {} oC.\n The humidity is {}% and the wind speed is {} kph.""".format(
            condition, city, country, temperature_c, feelslike_c, humidity, wind_kph)

        dispatcher.utter_message(response)
        return [SlotSet('location', loc)]

class ActionName(Action):
    def name(self):
        return 'action_name'

    def run(self, dispatcher, tracker, domain):
        user = tracker.get_slot('username')
        
        if user == None or user == "":
            response = """You didn't say your name"""
        else:
            response = """Your name is {}\n""".format(user)

        dispatcher.utter_message(response)
        return [SlotSet('username', user)]

class ActionNiceToMeetYou(Action):
    def name(self):
        return 'action_nicetomeetyou'

    def run(self, dispatcher, tracker, domain):
        user = tracker.get_slot('username')

        if user == None or user == "":
            response = """Nice to meet you.   ;)\n"""
        else:
            response = """Nice to meet you {}.   ;)\n""".format(user) 

        dispatcher.utter_message(response)
        return [SlotSet('username', user)]


# class ActionAnswer(Action):
#     def name(self):
#         return 'action_answer'

#     def run(self, dispatcher, tracker, domain):
#         # define mongoDB collection
#         knowledge = db.knowledgeBase
#         #Identify the last message intent
#         intent = tracker.latest_message.intent['name']
#         #find in Knowledge base collection the intent answer
#         # you have to treat errors like intent not found and others. I sugest a Try-Exception 
#         docs = knowledge.find_one({'intent':str(intent)})

#         response = """Initial intent is {}. The answer found is:{}""".format(intent, docs["text"])

#         dispatcher.utter_message(response)
#         #dispatcher.utter_attachment()
#         return []


class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'
    def run(self, dispatcher, tracker, domain):
        return[Restarted()]


class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'
    def run(self, dispatcher, tracker, domain):
        return[AllSlotsReset()]