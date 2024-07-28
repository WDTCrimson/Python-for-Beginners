#Project 3: FizzBuzz

running = True

while (running):
    countInput = False
    repeatInput = False
    count = 0
    repeat = ""

    while (not countInput):
        temp = input("Please enter the number you are counting to: ")
        if (temp.isdigit()):
            count = int(temp)
            countInput = True
        else:
            print("Input was invalid, try again!")

    for i in range (count + 1):
        if (i == 0):
            print(i)
        elif (i % 3 == 0 and i % 5 == 0):
            print("FizzBuzz")
        elif (i % 3 == 0):
            print("Fizz")
        elif (i % 5 == 0):
            print("Buzz")
        else:
            print(i)

    while (not repeatInput):
        temp = input("Do you want to try a different number (yes/no): ")
        if (temp.isalpha() and temp.casefold() == "yes"):
            repeatInput = True
        elif (temp.isalpha() and temp.casefold() == "no"):
            repeatInput = True
            running = False
        else:
            print("Input was invalid, try again!")
