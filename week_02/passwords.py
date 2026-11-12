def main():
    # ask user for password
    quit = "q"
    quit = quit.lower()
    password = input("Enter a password: ")
    while password != quit:
        password = input("Enter a password: ")

    main()


if __name__ == "__main__":
    main()
