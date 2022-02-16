
def addition(n,a):
    return n+a

quit=""
while quit != "q":
    try:
        n = int(input("Enter a number you would like to add: "))
        a = int(input("Enter a number you would like to add: "))
    except ValueError:
        print("You entered a non-integer value!")
    else:
        print(n, "+", a, "=", addition(n,a))
    finally:
        print("Your problem has been solved!")

    quit=input("Would you like to give me another problem (q to quit)?")