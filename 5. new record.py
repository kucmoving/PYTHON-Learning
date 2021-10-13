#loop - newrecord 刷新機制
highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

#random number not overlap 相同刷新機制
num_a = random.choice(1,5)
num_b = random.choice(1,5)
if num_a == num_b:
    num_b = random.choice(1,5)
