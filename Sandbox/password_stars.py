def main():
    password = get_password(8)
    for i in range(len(password)):
        print("*", end="")
    print()


def get_password(min_len):
    while True:
        password = input("Enter your password: ")
        if len(password) < min_len:
            print("Password is too short!")
        else:
            return password


if __name__ == '__main__':
    main()
