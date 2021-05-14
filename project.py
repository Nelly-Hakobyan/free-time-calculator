import json 
from datetime import datetime

def load_data():
    with open('data.json') as UserData:
        data = json.load(UserData)
        return data
def UserData():
    User_data = {
            "Name": "",
            "LastName": "",
            "Age":0,
            "Occupation":"",
            "Last_login_date":""
            }

    User_data["Name"]= input("Please, type your name ")
    User_data["LastName"]=input("Please, type your last name ")
    User_data["Age"]=int(input("Please, insert your age "))
    User_data["Occupation"]=input("What is your occupation? ")
    now = datetime.now()
    User_data["Last_login_date"] = now.strftime("%d / %m / %y")
    return User_data
 
    
def Free_time_calculator():
    Unavailable_Time = []
    Unavailable_Time.append( float(input("How many hours a day do you sleep? ")))
    Unavailable_Time.append( float(input("How many hours a day do you usually spend on your hobbies? ")))
    Unavailable_Time.append( float(input("How many hours a day do you usually spend on your work? ")))
    Unavailable_Time.append( float(input("How many hours a day do you usually spend on your homework? ")))
    Unavailable_Time.append(float(input("How many hours a day you usually spend on your meals? ")))
    sum = 0
    i = 0
    while(i < len(Unavailable_Time)):
        sum = sum + Unavailable_Time[i]
        i= i+1

    while(True):
        answer = input ("Are there any other activities you spend time on dayly? (y,n) ")
        if (answer == "y"):
            extra_time = float(input("How many hours a day do you spend on that activity? "))
            sum = sum + extra_time
        elif (answer == "n"):
            break
        else:
            print("Please enter a valid answer (y,n) ")

    free_time = 24 - sum 

    return free_time

def save_to_json(Users):
    x = open("data.json","w")
    x.write (json.dumps(Users, indent = 2))
    x.close()

def main():
    Users = []
    Users = load_data()
    J = UserData()
    Users.append(J)
    save_to_json(Users)

    F = str(Free_time_calculator())
    print("You have " + F + " hours of free time")

main()
