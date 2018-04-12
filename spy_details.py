

#spy = {"name": "Spy Singh", "salutation": "Mr", "age": 34, "rating": 3.7}

from datetime import datetime


class Spy:
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


class ChatMessage:
    def __init__(self, name, message, sent_by_me):
        self.name = name
        self.message = message
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.sent_by_me = sent_by_me


class ChatOld:
    def __init__(self, name, message, time, sent_by_me):
        self.message = message
        self.time = time
        self.sent_by_me = sent_by_me
        self.name = name



