questions_and_answers = {
    "Q1": "What is the capital of France?",
    "A1": "Paris",
    "Q2": "What is the largest planet in our solar system?",
    "A2": "Jupiter",
    "Q3": "Who is the author of the Harry Potter series?",
    "A3": "J.K. Rowling",
    "Q4": "What is the symbol for the chemical element iron?",
    "A4": "Fe",
    "Q5": "What is the highest mountain in the world?",
    "A5": "Mount Everest",
    "Q6": "What is the largest ocean on Earth?",
    "A6": "Pacific Ocean",
    "Q7": "Who painted the Mona Lisa?",
    "A7": "Leonardo da Vinci",
    "Q8": "What is the currency of Japan?",
    "A8": "Japanese yen",
    "Q9": "Who wrote the play Romeo and Juliet?",
    "A9": "William Shakespeare",
    "Q10": "What is the symbol for the chemical element gold?",
    "A10": "Au",
    "Q11": "What is the capital of Australia?",
    "A11": "Canberra",
    "Q12": "What is the largest continent on Earth?",
    "A12": "Asia",
    "Q13": "Who painted the Sistine Chapel ceiling?",
    "A13": "Michelangelo",
    "Q14": "What is the currency of Brazil?",
    "A14": "Brazilian real",
    "Q15": "Who wrote the novel To Kill a Mockingbird?",
    "A15": "Harper Lee",
    "Q16": "What is the symbol for the chemical element oxygen?",
    "A16": "O",
    "Q17": "What is the capital of South Africa?",
    "A17": "Pretoria",
    "Q18": "What is the largest desert in the world?",
    "A18": "Sahara Desert",
    "Q19": "Who painted the Starry Night?",
    "A19": "Vincent van Gogh",
    "Q20": "What is the currency of Canada?",
    "A20": "Canadian dollar",
    "Q21": "Who wrote the novel Pride and Prejudice?",
    "A21": "Jane Austen",
    "Q22": "What is the symbol for the chemical element hydrogen?",
    "A22": "H",
    "Q23": "What is the capital of China?",
    "A23": "Beijing",
    "Q24": "What is the largest lake in the world?",
    "A24": "Caspian Sea",
    "Q25": "Who painted The Last Supper?",
    "A25": "Leonardo da Vinci",
    "Q26": "What is the currency of India?",
    "A26": "Indian rupee",
    "Q27": "Who wrote the novel 1984?",
    "A27": "George Orwell",
    "Q28": "What is the symbol for the chemical element carbon?",
    "A28": "C",
    "Q29": "What is the capital of Germany?",
    "A29": "Berlin",
    "Q30": "What is the largest waterfall in the world?",
    "A30": "Angel Falls"
}
import random
# Accessing a question and its corresponding answer
# print(questions_and_answers["Q1"])  # Output: What is the capital of France
# print(questions_and_answers["A1"])
# key={i for i in questions_and_answers if questions_and_answers[i]=="Paris"}
# sprint(key)
name=input("please enter your name : ")
number=int(input("how many question do you want : "))
numbers=[]
for i in range(number):
    temp=random.randint(1,30)
    while(temp in numbers):
        temp=random.randint(1,30)
    numbers.append(temp)
# print(numbers)
score=0
for i in range(number):
    print(questions_and_answers["Q"+str(numbers[i])])
    answer=input()
    if answer.lower()==questions_and_answers["A"+str(numbers[i])].lower():
        print("right")
        score+=1
    else:
        print("wrong")
        print("the answer is",questions_and_answers["A"+str(numbers[i])])
if (score/number)*100>50:
    print("congratulations your score is",(score/number)*100)
else:   
    print("too bad your score is",(score/number)*100)