###2. 設定tutle身體(不變的項目要永遠大階)
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
segments= []

def create_snake(self):
    for position in STARTING_POSITIONS:
        self.add_segment(position)

def add_segment(self, position):
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    self.segments.append(new_segment)

##延長身體
def extend(self):
    self.addsegment(self.segments[-1].position())


#####3. 設定turtle 多寡
all_turtle =[]
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=ypositions[index_index])
    all_turtles.append(new_turtle)

##遺承turtle
class Food(Turtle):
    def __init__(self):
        super().__init__()

#設定形狀, 陰影
self.shape("circle")
self.shapesize(0.5, 0.5,12)

#加上文字
tim.write("Some Text", font = ("Times New Roman", 80, "bold"))

#速度
speed("fastest")

##設定object 兩塊版
from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))

#設置移動物
class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1