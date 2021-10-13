## First!!!we have to import random!! import random 插入random 配件
import random

#random number
random_integer = random.randint(1,10)#from 1 - 10
print(random_integer)

random_float = random.random() #from 0-1
print(random_float)

#random a string from list
word_list = ["apple", "orange", "banana"]
chosen_word = random.choice(word_list)
print(chosen_word)

#generate a list of random letter
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
password = ""
for letter in letters:
    password += random.choice(letters)
print(password)

#random letter in list
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
random.shuffle(letters)
print(letters)

