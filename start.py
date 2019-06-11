import nltk
import json
from nltk.chat.util import Chat, reflections
import numpy as np
import random
import string # to process standard python strings
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import copy




reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

my_dummy_reflections= {
    "go"     : "gone",
    "hello"    : "hey there"
}


pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?,Hi there, how can I help?",]
    ],
        [
        r"(.*) created ?",
        ["XXYY created me using Python's NLTK library ","top secret ;)",]
    ],
     [
        r"what is your name ?",
        ["My name is Chatty and I'm a chatbot ?",]
    ],
    [
        r"how are you ?",
        ["I'm doing good\nHow about You ?",]
    ],
    [
        r"sorry (.*)",
        ["Its alright","Its OK, never mind",]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that","Alright :)","dont repete again :)",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ],
    [
        r"(.*) age?",
        ["I'm a computer program dude\nSeriously you are asking me this?",]
        
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
        
    ],

    [
        r"(.*) (location|city) ?",
        ['Ch, Tam',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    ],
[
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Football",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Messy","Ronaldo","Roony"]
],    
[
        r"fine (.*) you ?",
        ["whats new?","go on ask question?","I dont think it valid, do you?"]
],
    [
        r"who (.*) (moviestar|actor)?",
        ["Brad Pitt"]
],
    [
        r"quit",
        ["BBye take care. See you soon :) ","It was nice talking to you. See you soon :)"]
],
]

def convertToPair(fileName):

    mylist=[]

    mylistPatterns =[]
  
    with open("intents.json") as file:
        data = json.load(file)

    for intent in data["intents"]:

        mylistPatterns.extend(intent["patterns"])
        mylistPatterns.append(intent["responses"])

        mylist.append(mylistPatterns.copy())

        mylistPatterns.clear()
    #for k, v in mylist:
    #    print(k,"=:=", v)
    return mylist


def chatty():

    myResultlist=convertToPair("intents.json")

    print("Hi, I'm Chatty and I chat alot ;)\nPlease type lowercase English language to start a conversation. Type quit to leave ") #default message at the start
    #chat = Chat(tuples, reflections)
    chat = Chat(myResultlist, reflections)    
    chat.converse()
if __name__ == "__main__":
    chatty()