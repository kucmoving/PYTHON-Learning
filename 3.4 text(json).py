#Using json in data processing / json.dump()#Write / json.load()#Read / json.update()#update
import json

##1.0 將variable值匯出成json
####設定好輸入的在json的字典格式
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {                      ##這部份是json內的格式
        website: {
            "email": email,
            "password": password,
        }
    }
####加入到json檔
    else:
        with open("data.json", "w") as data_file:
            json.dump(new_data, data_file, indent=4) ##(格式, json檔名)
            website_entry.delete(0, END)
            password_entry.delete(0, END)

####json內會出現字典
{"website": {"email": "email@address.com, "password": "12345"}}

##2.0 存取file時使用teef
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

##3.0 設定搜索詢問機制(使用teef)
search_button = Button(text="Search", width=13, command=find_password)
search_button.grid(row=1, column=2)

def find_password():
    website = website_entry.get()
    try:
        with open("data.json").data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{password}")
        else:
            messagebox.showinfo(title="Error", message= f"no details for {website} exists.")





