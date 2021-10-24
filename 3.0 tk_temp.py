#匯入並設置object
import tkinter

##############可預設顏色、數值
from tkinter import *

PINK = "#e2979c"
RED = "e7305b"
GREEN = "#9bdeac"
YELLOW = "#7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


############### UI setup
window = tkinter.TK()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20, bg=YELLOW)

###佈景設計
canvas = Canvas(width=200, height=244, bg=YELLOW, highlightthickness=0) #設置背景大細
tomato_img = PhotoImage(file="tomato.png") #加入背景圖片
canvas.create_image(100, 112, image=tomato_img) ###修改圖片位置及引入圖片
canvas.create_text(103, 130, text="00,00", fill="white", font=(FONT_NAME, 35, "bold"))#加入背景文字
canvas.grid(column=1, row=1)


##設好label

###設好button

#mainloop要放到最後
window.mainloop()


######################with object################

from tkinter import *

THEME_COLOR = "#375362"
###製造class
class QuizInterface:
    def __init__(self):
        self.window = TK() ##用tk 做attribute
        self.window = title("Quizzler")
        self.window.config(padx=20, pady=20, bg=theme_color)###留白空間

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)##設定Label樣式
        self.score_label.grid(row=0, column=1) ##進行排位

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text( ###設定背景、文字樣式
            250,
            125,
            text="some question text",
            fill=THEME_COLOR,
            font=("arial", 20, "italic")
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.window.mainloop()


