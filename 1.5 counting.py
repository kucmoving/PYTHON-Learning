#loop counting / 數字疊加
total = 0
for number in range(1, 101):
    total += number

#loop / 不停進行扣減 A. 前置設定 B. 循環設定 C. 疊加
lives = 6

if guess not in chosen_word:
    lives -= 1
    if lives == 0:
        end_of_game = True
        print("you lose.")

