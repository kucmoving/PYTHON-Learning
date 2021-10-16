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

#隨機抽選，特定次數 ##random 下可以直接做choice(letters)
letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
password_letters = [choice(letters) for _ in range(randint(8, 10))]

#表內次序調換
random.shuffle(letters)
print(letters)

#random color
def random_color()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color
