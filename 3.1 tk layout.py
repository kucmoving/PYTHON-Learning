##Tkinter Layout Managers: pack(), place() and grid()
##所有ITEM都要用pack, place, gird 去做定位才會生效

#1. place 是指定位置(x,y), 如果太多就多功夫
my_label.place(x = 100, y = 200)

#預設是最高，但pack太一致，難精巧

#2. grid 是網格(row, column) , 但pack不可與grid一起
##grid 按比例進行劃分,第一行是0開始
my_label.grid(column = 1, row = 1)
website_entry.grid(row=1, column=1, columnspan=2) #column霸佔的位置可以是2格


