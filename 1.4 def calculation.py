#basic calculation
Bmi = weight / height * height



# multi collect and calculate(1. input + 2. def(calculate and display)+ 3. call function) - 1. 收集 2. DEF(計算,展示) 3. 召回
get_price = float(input("how much is the bill"))
get_tips = float(input("how much is the tips, 0.12 or 0.15"))
get_people = int(input("how many people are there "))

def pay_bill(price, tips, people):
    number_per_person = (price / people)* (1 + tips)
    print(f"you have to pay {number_per_person}")

pay_bill(price = get_price, tips = get_tips, people = get_people)



