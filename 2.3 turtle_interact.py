##1.1 設定turtle動作 function
def move_forwards():
    tim.forward(10)

##1.2. 設定與鍵連定
screen.listen()
screen.onkey(fun=move_forwards, key="space")
screen.exitonclick()

##滑鼠得到位國


######2. 提問箱及開始
user_bet = screen.textinput(title="this is your topic", prompt='what do u want to ask')
print(user_bet)

if user_bet:
    is_race_on = True

################跑車按鍵
def up():
    tim.forward(10)

def down():
    tim.backward(10)

def left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(fun=up, key="w")
screen.onkey(fun=down, key="s")
screen.onkey(fun=letf, key="a")
screen.onkey(fun=right, key="d")
screen.onkey(fun=clear, key="c")

###############不可回頭設定
UP = 90
DOWN = 270
LEFT = 180
RIGHT 0

####在class 內###
def up(self):
    if self.head.heading() != DOWN:
        self.head.setheading(UP)

def down(self):
    if self.head.heading() != UP:
        self.head.setheading(DOWN)

def left(self):
    if self.head.heading() != RIGHT:
        self.head.setheading(LEFT)

def right(self):
    if self.head.heading() != LEFT:
        self.head.setheading(RIGHT)

####垂直移位

def up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddley.xcor(), new_y)

def down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)

screen.listen()
screen.onkey(up,"up")
screen.onkey(down,"down")

