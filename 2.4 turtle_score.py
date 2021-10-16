###1. 設定scoreboard記分版
from turtle import turtles
ALIGNMENT = "centre"
FONT = ("Courier", 24, "normal")

##承傳turtle
class Scoreboard(turtle):
##指出屬性(如雙人計分就要加入l_score)
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.high_score = 0

##更新紀錄
    def update_scoreborard(self):
        self.write(f"Score: {self.score}",align=ALIGNMENT, font=FONT)

##最高分
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode ="w") as data:
                data.write(f"{self.high_score}")

##加分及清空機制
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

##2. 設定完結
    def game(self):
        self.goto(0, 0)
        self.write("GAME OVER", aligen=ALIGNMENT, font=FONT)

while len(guessed_states) < 50:
    ...
    if answer_state == "Exit":
        break