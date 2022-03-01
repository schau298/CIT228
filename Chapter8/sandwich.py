def sandwich(*toppings):
    print("What toppings would you like on your sandwich:")
    for topping in toppings:
        print(f"\n-----{topping} was added to your sandwich!")
    print("\nYour sandwich is complete!)\n")
    
sandwich('salami', 'pepperoni', 'pepperjack', 'marinara')
sandwich('ham', 'turkey', 'lettuce','tomato', 'bacon', 'mayo')
sandwich('tuna', 'cheese','lettuce','onions')