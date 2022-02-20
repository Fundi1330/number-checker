print("The program has started")

while True:
    sym = int(input("Enter a number, and I'll try to tell you about it: "))
    if (sym < 0):
        print("You entered a number: " + str(sym) + " it is negative")
    elif (sym == 3.14):
        print("You entered the number P")
    elif (sym == 0):
        print("You entered zero")
    else:
        print("You entered a positive number")