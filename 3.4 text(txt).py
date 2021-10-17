
###1. 開文件夾 (使用with可以自動關上，沒檔案也會加)
with open("my_file.txt","r") as file_file:
    names = names_file.readline()
    print(names)

###2. 進行寫作
with open("my_file.txt","w") as file:
    file.write("new text.")

##3. 進行附加
with open("my_file.txt", "a") as file:
    file.write("\nnew text.")

##4) 將a及b進行merge 形成c檔案 replace
PLACEHOLDER ="[name"]

with open("abc.txt") as names_file:
    names = names_file.readline()

with open("def.txt", "r") as letter_file:
    letter_contents = letter_file.readline()

# 進行修改，並開新TXT
for name in names():
    stripped_name = name.strip()
    new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)

    with open(f"./readytosend/letter_for_{stripped_name}.txt", "w") as completed_letter:
        completed_letter.write(new_letter)



