import math

print("The program has started")

while True:
    sym = float(input("Enter a number, and I'll try to tell you about it: "))
    if (sym < 0):
        print("You entered a number: " + str(sym) + " it is negative")
    elif (sym == math.pi or sym == 3.14):
        print("You entered the number P")
    elif (sym == 0):
        print("You entered zero")
    else:
        print("You entered a number: " + str(sym) + " it is positive")
