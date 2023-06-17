import random
words = ["apple", "banana", "carrot", "dog", "elephant", "fish", "giraffe", "hat", "ice", "jacket", "kite", "lamp", "mouse", "nose", "orange", "pencil", "queen", "rainbow", "star", "tree", "umbrella", "violin", "watermelon", "xylophone", "yarn", "zebra"]
answer = random.choice(words)
name=input("please input your name : ")
guess=""
chance=10
print("lets start guessing")
while(chance>0):
    guess_letter=input(" guess a letter of the word :")
    guess+=guess_letter
    wrong=0
    print()
    for i in answer:
        if i in guess:
            print(i,end=" ")
        else:
            print("_",end=" ")
            wrong=1
    if wrong==0:
        print("congratulation!",name,"you complete the word")
        break
    if guess_letter not in answer:
        chance-=1
        print("wrong letter try again")
        print("you have",chance,"chance left")
        if chance==0:
            print("gameover")
            break            