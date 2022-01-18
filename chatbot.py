import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
from tensorflow.keras.models import load_model
import os
import PySimpleGUI as sg
import os.path

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

lemmatizer = WordNetLemmatizer()
intents = json.loads(open("C:/Users/maciej/Desktop/fun projects/chatbot/intents.json").read())

words = pickle.load(open("words.pkl", "rb"))
classes = pickle.load(open("classes.pkl", "rb"))
model = load_model("bot_model.model")

def cleaning_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    sentence_words = cleaning_sentence(sentence)
    bag = [0] * len(words)
    for x in sentence_words:
        for i, word in enumerate(words):
            if word == x:
                bag[i] = 1
    return np.array(bag)

def predict_class(sentence):
    bag = bag_of_words(sentence)
    res = model.predict(np.array([bag]))[0]
    ERROR_THRESHOLD = 0.25
    results= [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
    return result
layout = [
    [sg.Text("Welcome to TestBot!")],
    [sg.Text("You can ask me without needing to be careful with your wording, I'm smart enough to pick up on your intentions :)")],
    [sg.Text("Try asking about: age, name, projects, info and also greetings and goodbyes!")],
    [sg.Text("You: "), sg.Text(size=(50,1), key="-mytext-")],
    [sg.Text("TestBot: "), sg.Text(size=(50,4), key="-CSI-")],
    [sg.Input(key="-myinput-")],
    [sg.Button("Submit message"), sg.Button("Exit")]
]


window = sg.Window("Test window", layout)


while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "Submit message":
        message = values["-myinput-"]
        ints = predict_class(message)
        res = get_response(ints, intents)
        response = res
        window["-mytext-"].update(message)
        window["-CSI-"].update(response)
window.close()
