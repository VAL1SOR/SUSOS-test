import os

path = "user/"

if (os.path.isfile("user/username.susdata")):
    loginuser = open("user/username.susdata")
    loginpassword = open("user/password.susdata")
    l_u = loginuser.read()
    l_p = loginpassword.read()
    logininput = input("SUS-OS Login m8 or you are SUS\nLog in as " + l_u + ": ")
    if logininput == l_p:
        if os.name == "nt":
            os.system("cls")
            os.system("python3 os.py")
        else:
            os.system("clear")
        pass
        os.system("python3 os.py")
    else:
        print("U ARE SUS MY MAN")
        os.system("python3 login.py")
else:
    user = input("Username: ")
    password = input("Password: ")

    userlines = [user]
    passwordlines = [password]
    if os.path.exists(path):
        print("The user path exists")
    else:
        os.system("mkdir user")
    with open("user/username.susdata", "w") as f:
        f.writelines(userlines)
    with open("user/password.susdata", "w") as f:
        f.writelines(passwordlines)
        f.close()
        os.system("python3 login.py")