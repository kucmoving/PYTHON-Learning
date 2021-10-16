#####1. 設定位置
tim.goto(x=-230,y=0)

###2. 關於邊界(xcor, ycor)
if turtle.xor() > 230:
    is_race_on = False
    winning_color = turtle.pencolor()

if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    game_is_on = False

###2. 隨機位置生成
random_x = random.randint(-280,280)
random_y = random.randint(-280,280)
self.goto(random_x,random_y)

##3. 物件距離distance
if snake.head.distance(food) <15:
    food.refresh()

###4. 重置位置
def reset_position(self):
    self.position(0,0)

###自身觸踫
for segment in snake.segments[1:]:
    if segment == snake.head:
        pass
    elif snake.head.distance(segment) < 10:
        game_is_on = False

###設定反彈機制(加強)
if ball.ycor() > 280 or ball.ycor() <- 280:
    ball.bounce_y()

def bounce_y(self):
    self.y_move *= -1
    self.move_speed *= 0.9

def bounce_x(self):
    self.x_move *= -1
    self.move_speed *= 0.9

def move(self):
    new_x = self.xcor() + 10
    new_y = self.ycor() + 10
    self.goto(new_x, new_y)

##得到位置
def get_mouse_click_coor(x,y)
    print(x,y)
get_mouse_click_coor()