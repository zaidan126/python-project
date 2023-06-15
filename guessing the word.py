import random
words = ["apple", "banana", "carrot", "dog", "elephant", "fish", "giraffe", "hat", "ice", "jacket", "kite", "lamp", "mouse", "nose", "orange", "pencil", "queen", "rainbow", "star", "tree", "umbrella", "violin", "watermelon", "xylophone", "yarn", "zebra"]
answer = random.choice(words)
name=input("please input your name : ")
guess=""
chance=10
print("lets start guessing")
while(chance>0):
    guess_letter=input("guess a letter of the word :")
    guess+=guess_letter
    wrong=0
    for i in answer:
        if i in guess:
            print(i)
        else:
            print("_")