# how to use OOP
# main.py     function  <>  function
# other.py    attribute --> function

#1. import object from other py
from money_machine import MoneyMachine

#2. create object in py(要大階)
money_machine = MoneyMachine()

#3.0 remeber 1 class 1 py(要大階)
#3.1 setup class global (if need)
class MoneyMachine:
    CURRENCY = "$"
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10
    }

#3.1 setup Class attribute in that other py --> support Class function only
    def __init__(self):
        self.profit = 0
        self.money_received = 0

#3.2 setup Class function in that other py -->receive attri and support main py
    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

#4. calling object to function in main.py
#頁內傳召自己一律是   self.coin / self.coin()
#頁內傳召他人是      直接寫 coin / coin () / 主頁時才重新定義
#主頁傳召自己及他人是 money_machine.make_payment()



