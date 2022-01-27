color="Blue"
number1=5
number2=10

deserts=["Chocolate","Pudding", "icecream", "cookies"]

print("----------------------------------True Results---------------------------")
print(number1, "<", number2, number1<number2)
print(number1, "<=", number2, number1<=number2)
print(number2, ">", number1, number2>number1)
print(number2, ">=", number1, number2>=number1)
print(number2, "=", number2, number2==number2)

print(color,"== Blue", color=="Blue")
print("blue==blue", color.lower()=="blue")
print("5>=4 or 10 >=11", number1>=4 or number2 >=11)
print("(5>=4) and (10>=4)",(number1>=4) and (number2>=4))
print("Is chocolate a desert option? ", "Chocolate" in deserts )
desert="Cupcake"
if desert not in deserts:
    print("Sorry Cupcake is not a desert option")

print("----------------------------------False Results---------------------------")
print(number1, ">=", number2, number1>number2)
print(number1, ">=", number2, number1>=number2)
print(number2, "<", number1, number2<number1)
print(number2, "<=", number1, number2<=number1)
print(number1, "=", number2, number1==number2)

print(color, "!= Blue", color!="Blue")


