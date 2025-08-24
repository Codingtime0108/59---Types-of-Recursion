def negative():
    num = int(input("Enter any number: "))
    if num < 0:
        print("Negative number found!!")
    else:
        negative()

negative()