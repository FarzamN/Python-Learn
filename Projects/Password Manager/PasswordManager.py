from cryptography.fernet import Fernet


def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)


def loadKey():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key


masterPassword = input("Enter the master password: ")

key = loadKey() + masterPassword.encode()
fer = Fernet(key)


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.strip().split(" | ")
            user, password = data
            print(f"User: {user}, Password: {str(fer.decrypt(password.encode()))}")


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("./passwords.txt", "a") as f:
        f.write(name + " | " + str(fer.encrypt(pwd.encode())) + "\n")


while True:
    mode = input(
        "Do you want to add a new password or view existing ones? (add/view) press q to quit: "
    ).lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid mode.")
        continue
