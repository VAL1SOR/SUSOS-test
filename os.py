import assistant
import webbrowser
import time
import os

if (os.path.isfile("user/username.susdata")):
    pass
else:
    os.system("python3 login.py")

l_u = open("user/username.susdata").read()

os.system("cls")
print("Logged in as " + l_u + "\n" + "At " + time.strftime("%H:%M:%S %d/%m/%Y\n"))

while True:
    command = str(input(l_u + " $ "))
    if command == "exit":
        os.system("cls")
        break
    elif command == "openlink":
        os.system("cls")
        link = input("Note: You can type the link without https://\nLink: ")
        webbrowser.open_new_tab(link)
    elif command == "update":
        os.system("pip install --upgrade https://github.com/VAL1SOR/SUSOS-test.git")
    elif command == "assistant":
        os.system("cls")
        assistant.assistant()