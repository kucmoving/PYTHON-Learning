3import math

##設計時鐘
##1.0 設定計時時間###設定5 分鐘計時
def start_timer():
    count_down(5*60)

##2.0 將分秒分開計時 ##計算程序是分開計分鐘及秒數
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec == 0:                 #對付零分鐘
        count_sec ="00"
    if countsec < 10:                  #對付零秒數
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')##修整CANVAS要先打上canvas.itemconfig
    if count > 0:
        window.after(1000, count_down, count -1) #再設置延遲機制

#####################
import time  ##import time是可行的，但太死板
count = 5
while True:
    time.sleep(1)
    count -=1

###########backend - 設定function

