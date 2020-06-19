import time
import os
def login():
    print("......................")
    print("What do you want to do?")
    print("......................")
    print("{1} Login")
    print("{2} Sing up")
    print("{3} Leave")
    print("......................")
    print("Coded by Paul")

    cmd = int(input("Enter number: "))

    if cmd == 1: #Login
        print("......................")
        user = str(input("Enter your username: "))
        print("......................")
        pwd = str(input("Enter your password: "))
        print("......................\n\n\n")
        f = open(user + ".txt", "r")
        data = f.readline()
        f.close()
        if data == user + ", " + pwd:
            print("///////////////////////")
            print("Logged in")
            print("///////////////////////")
            print("Coded by Paul")
            time.sleep(3)
        else:
            print("///////////////////////")
            print("Username or password wrong!")
            print("///////////////////////")
            print("Coded by Paul")
            login()

    elif cmd == 2: #Sing up
        print("......................")
        new_user = str(input("Enter your username: "))
        print("......................")
        new_pwd = str(input("Enter your password: "))
        print("......................\n\n")
        for f_name in os.listdir("C:/Users/Paul/Desktop/Development/Python/Export"):
            if f_name.endswith(".txt"):
                if f_name == new_user+".txt":
                    print("///////////////////////")
                    print("Username already exists")
                    print("///////////////////////")
                    print("Coded by Paul")
                    login()
                    return
                else:
                    print("///////////////////////")
                    print("New Account Created")
                    print("///////////////////////")
                    print("Coded by Paul")
                    login()

        f = open(new_user + ".txt", "w")
        f.write(new_user + ", " + new_pwd)
        f.close()
    elif cmd == 3: #Leave
        print("//////////////////////////////")
        print("Leaving.....")
        print("//////////////////////////////")
        print("Coded by Paul")
        time.sleep(2)
        quit()
    else:
        print("\n//////////////////////////////")
        print("Number not available!")
        print("//////////////////////////////\n")
        print("Coded by Paul")
        login()

login()