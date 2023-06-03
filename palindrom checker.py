exit="no"
while(exit=="no"):
    word= input("put a word or sentence to check: ")
    reversed=word
    # print (word,reversed)
    # for i in range(len(reversed)):
    #     print(reversed[i])
    temp=""
    for i in range(len(reversed),0,-1):
        temp+=(reversed[i-1])
    print(temp)
    reversed=temp
    if word==reversed:
        print("the word is palindrom")
    else:
        print("the word is not palindrom")
    exit=input("do you want to exit yes or no?:  ")