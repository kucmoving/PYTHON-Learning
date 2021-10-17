###Optional Arguments, *args and **kwargs Quiz
#ARGUMENT 優次
# 1.	下方position 定位
# 2.	上方position定位
# 3.	下方次序
# 4.	冇寫就預設

def all_aboard(a, *args, **kw):
    print(a, args, kw)

all_aboard(4, 7, 3, 0, x = 10, y = 64)
#4 (7, 3, 0) {'x': 10, 'y': 64}

####參數詳情可見tkinter

#輸入文字(都可以加width, height變闊)
my_label = Label(text = "i am a label", fg=GREEN, bg=YELLOW, font = ("arial", 24, "bold"))
my_label.config(text = "new text") ###簡介文字
my_label.pack(side = "left") #pack 了材可以顯示,有大量argument可以使用

##設置按鍵再修改其他label
def button_clicked():
    print('i got clicked')
    miles = float(miles_input.get())儲存功能
    km = miles * 1.609
    kilometer_result_label.config(text=f"{km}")##修改另一個label

## 在ENTRY上自動顯示文字,password是可以用的variable
password_entry.insert(0, password)

## 自動複雜variable予用家
import pyperclip
pyperclip.copy(password)