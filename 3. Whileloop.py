#While loop / 循環 A. 前置設定 B. 循環設定 C. 疊加

game_process = True

while game_process == True:

    #can add function here
    result = input("type 'yes if you want to go again. otherwise type 'no.' ")

    #to exit
    if result == "no":
        should_continue = False
        print("bye")

