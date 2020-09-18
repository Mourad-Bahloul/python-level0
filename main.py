def main():
    username = "Marc"
    age = 23
    print(username, age + 1)
    # use str() to convert a digit into a string : can't concat a digit with a string otherwise!
    print("Salut " + username, ",vous avez " + str(age) + " ans!")


if __name__ == '__main__':
    main()
