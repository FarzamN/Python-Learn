from cryptography.fernet import Fernet

masterPassword = input("Enter the master password: ")


# def view():
#     with open("passwords.txt", "r") as f:
#         for line in f.readlines():
#             data = line.rsplit()
#             print(data)
#             user, password = data.split()
#             print(f"User: {user}, Password: {password}")


def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.strip().split(" | ")
            user, password = data
            print(f"User: {user}, Password: {password}")


def add():
    name = input("Account Name: ")
    pwd = input("Password: ")

    with open("./passwords.txt", "a") as f:
        f.write(name + " | " + pwd + "\n")


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
