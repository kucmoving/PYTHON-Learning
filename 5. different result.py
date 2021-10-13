#mark counting with condition ( +=, *=, -=, /=) / 按照情況予分
bill = 0
size = input("plz choose a size,S,M,L").lower()
if size == 's':
    bill += 15
elif size == 'm':
    bill += 20
else:
    bill += 25
print(bill)


