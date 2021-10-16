##1 建立空白CLASS
class User:
    pass

user_1 = User()
usder_1.id ="001"
user_1.username ="angela"
print(user_1.username)

##2 使用預設機制(initialize attributes)-->使用init後才有object都有該屬性
class Car:
    def __init__(self):
        print("new user being created...")

##3 設置object,須用多parameters 運作, 如沒有相關,就會error
class Question:
    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer

new_q = Question("sdfsdf", "False")
print(new_q.text)



