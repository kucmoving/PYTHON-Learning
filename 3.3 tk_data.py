##1.進行收集(如果空就彈ERROR).get()
def save():
    website = website_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password ==0):
        messagebox.showinfo(title="oops", message="you should type sth")

##2. 收集數據成檔，並清空(1).delete
def clear_all():
    with open("data.txt", "a") as data_file:
        data_file.write(f"{website} | {email} | {password}\n")
        website_entry.delete(0, END)
        password_entry.delete(0, END)

##2. 重新清空介面(2).after_cancel
def reset():
    window.after_cancel(timer) #進行停止刷新
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="timer")
    check_marks.config(text="")
    global reps
    reps = 0


