###########fontend - 設定介面
#1. 話框架
input = Entry(width = 10)
input.pack()
input.get()

#2. 按鈕(可配上width)
true_image = PhotoImage(file="images/true.png")
calculate_button = Button(image=true_image, text = "Calculate", highlightthickness=0,command = miles_to_km)##text上文字, command 是聯繫function
calculate_button.grid(column=1, row=2)

#3. 輸入方格
miles_input = Entry(width=35)
website_entry.focus() ###會出現藍框focus
email_entry.inser(0, "angela@gmail.com")#方格會出現預設文字

#4. 提示箱
from tkinter import messagebox
messagebox.showinfo(title="title", message="Message")

#5. YES OK 箱子
is_ok = messagebox.askokcancel(title=website, message=f"these are the details entered: \nEmail: {email}" f"\nPassword: {password} \nIs it ok to save?")



