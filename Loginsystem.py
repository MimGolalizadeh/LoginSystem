user_data_store = {
   1: {"First name": "Brad", "Last name": "Pitt", "Email address": "Brad@Pitt.com", "Password": "2021"},
   2: {"First name": "Tom", "Last name": "Hanks", "Email address": "Tom@Hanks.com", "Password": "2022"},
   3: {"First name": "Will", "Last name": "Smith", "Email address": "Will@Smith.com", "Password": "2023"},
   4: {"First name": "Tom", "Last name": "Hardy", "Email address": "Tom@Hardy.com", "Password": "2024"},
}

auth_check_item = False
while auth_check_item != True:
    username = input(f"USER NAME: ").title()
    password = input(f"PASSWORD: ")
    for dict_number in user_data_store:
        if username == user_data_store[dict_number]["Email address"].title() and password == user_data_store[dict_number]["Password"]:
            fullname = user_data_store[dict_number]["First name"] + " " + user_data_store[dict_number]["Last name"]
            message1 = f"Hello, {fullname}, you have successfully logged in"
            auth_check_item = True
        else:
            message2 = f"Your login information is incorrect"
            dict_number += 1
    if auth_check_item == True:
       print(message1)
    else:
       print(message2)
