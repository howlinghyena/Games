pwd=input("Type the master password: ")

def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user, passw = data.split("|")
            print("User:", user, " | password:", passw)


def add():
    name = input("Enter Account name: ")
    pwd = input("Enter Password: ")

    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + pwd + "\n")



while True:

    mode = input("would you like to add a new password or view existing ones(view, add)?")
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("invalid mode.")
        continue
