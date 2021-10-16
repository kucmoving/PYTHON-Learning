##1. 固定方向移動
for _ in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

##2. 隨機方向，隨機色，隨機速度
colors = ["red", "white", "green"]
directions = [0, 90, 180, 270]

for _ range(200):
    tim.forward(30)
    tim.color(random.choice(colors))
    tim.setheading(random.choice(directions))
    tim.forward(random.randint(0,10))

##改變角度
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        time.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)

##3. 設定格子追縱形式慢慢減減追上前格位置, 移動特效
for seg_num in range(len(segments) - 1, 0 -1):
    new_x = segments[seg_num - 1].xcor()
    new_y = segments[seg_num - 1].ycor()
    segments[seg_num].goto(newx, newy)
segments[0].forward(20)


#random color
tim.colormode(255)

def random_color()
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

tim.color(random_color())





