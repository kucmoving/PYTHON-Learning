# 設定烏龜基本畫面設定，再設定SCREEN位置
#screen 要大階, 可看到烏龜位置, Screen是Object, canvheight是attribute

###進行大量引入py object
from turtle import Screen

##再將variable 定義為object


screen = Screen()
screen.bgcolor("black")
image = "blank_state_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.setup(width=1200, height=960)
screen.title("pong")

print(screen.canvheight, screen.canvwidth)
screen.exitonclick()









