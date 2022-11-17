from random import *

#Code below is the skeleton for a simple haiku generator.

#Create the list of words you want to choose from.
five_syllable = ["Hey, I just met you", "First I was afraid", "Love the one you’re with"]
seven_syllable = ["Now, winter chills on my feet", "A time of joy, peace and love", "Your shadow, one can not find"]

first_sentence = ""
second_sentence = ""
third_sentence = ""

#Generates a random integer.
x = randint(0, len(five_syllable)-1)
print(five_syllable[x])

x = randint(0, len(seven_syllable)-1)
print(seven_syllable[x])

x = randint(0, len(five_syllable)-1)
print(five_syllable[x])
