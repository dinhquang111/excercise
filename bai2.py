from random import choice
import random

questions = {
"strong": "Do ye like yer drinks strong?",
"salty": "Do ye like it with a salty tang?",
"bitter": "Are ye a lubber who likes it bitter?",
"sweet": "Would ye like a bit of sweetness with yer poison?",
"fruity": "Are ye one for a fruity finish?"
}

ingredients = {
"strong": ["glug of rum", "slug of whisky", "splash of gin"],
"salty": ["olive on a stick", "salt-dusted rim", "rasher of bacon"],
"bitter": ["shake of bitters", "splash of tonic", "twist of lemon peel"],
"sweet": ["sugar cube", "spoonful of honey", "spash of cola"],
"fruity": ["slice of orange", "dash of cassis", "cherry on top"]
}

def choose(usrIp):
    while True:
        a = input(questions[usrIp] + " Yes or no:" + "\n")
        if a == "yes":
            print(choice(ingredients[usrIp]))
            break
        elif a == "no":
            arr = []
            for key in questions.keys():
                arr.append(key)
            b = input("Why don't we try another one? How about " + arr[random.randrange(0,5,1)] + ": ")
            if b == "yes":
                print("Enjoy " + choice(ingredients[arr[random.randrange(0,5,1)]]))
                break
            else:
                print("OK, have a good night!")
                break
        else:
            print("wrong answer")

while True:
    ip = input("Please type your taste: strong, salty, bitter, sweet or fruity: ")
    if ip == "strong" or ip == "salty" or ip == "bitter" or ip == "sweet" or ip == "fruity":
        choose(ip)
        break
    else:
        print("wrong answer, type again!")