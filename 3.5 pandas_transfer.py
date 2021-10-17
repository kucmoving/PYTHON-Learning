import pandas

##1) 將variables內容編入csv
data_dict= {
    "Fur Color": ["Gray", "Cinnamon," "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
print(df)
df.to_csv("squirrel_count.csv")

##2) 如果輸入與txt有相同..就
if answer_state in all_states:
    t = turtle.Turtle()
    state_data = data[data.state == answer_state]
    t.goto(int(state_data.x), int(state_data.y))
    t.write(answer_state)

##用pandas 讀取整個字典形狀 ###調配位置包括index,row,column
for (index.row) in student_data_frame.iterrows():
    print(index)

###重製整個排列次序,row,index, column name
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

