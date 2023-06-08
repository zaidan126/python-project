import random 
import turtle
for i in range(4):
    turtle.forward(100)
    turtle.left(90)
# 1 generating random number:
print (random.random()) # generate a random float between 0 and 1
a=0
b=10
print (random.randint(a, b)) #to generate a random integer between a and b, inclusive.
print (random.uniform(a, b)) # to generate a random float between a and b
# Randomly selecting elements:
print (random.choice("hello")) # to randomly select an element from a sequence (seq can be a list, tuple, or string).
# random.sample(population, k) # to randomly select k unique elements from a population (without replacement).
# Shuffling elements:
# random.shuffle(lst) # to randomly shuffle the elements of a list lst in place.
# Simulating random events:
# random.random() # Use random functions in combination with conditional statements (if, else) to simulate different outcomes.
# Generating random strings:
# random.choice() # in conjunction with string manipulation to generate random strings.
# For example, you can create a random password by selecting random characters from a pool of characters.
# random.sample()
# Seeding randomness:
# random.seed(x) # to initialize the random number generator with a specific seed value x. This ensures reproducibility of random sequences.






