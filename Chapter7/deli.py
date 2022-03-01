sandwich_orders=["meatball","tuna","pastrami", "italian","pastrami", "breakfast","pastrami","club","vegetable","meat lovers"]
finished_sandwiches=[]

print("I am sorry, we are out of pastrami!!")
while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich.title()} sandwich")
    finished_sandwiches.append(current_sandwich)

print("Sandwiches that were made today include:")
for s in finished_sandwiches:
    print(s.title())