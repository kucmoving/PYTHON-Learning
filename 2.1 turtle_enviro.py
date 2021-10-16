#1. 引入烏龜與螢幕
from turtle import Turtle, Screen
tim = Turtle()

#2. 設定螢幕大小
my_screen = Screen()
screen.setup(width=500, height=400)
print(my_screen.canvheight, my_screen.canvwidth)

#3. 處理背景
screen.bgcolor("black")

#4. 修改標題
screen.title("My Snake Game")

#4. 等候時間設置(遊戲開始時可以先停)
import time
time.sleep(1)

###4 設定螢幕跟隨, 變0會取消進場
screen.tracer(8,25)


###5. 設定畫面刷新/ 當遊戲進行時需要(screen.update())
while game_is_on:
    for seg in segments:
        seg.forward(20)
        screen.update()

#3. 點擊才離開
my_screen.exitonclick()





