group=input("How many people are in your dinner group:")
group = int(group)

if group >= 10:
    print(f"\nPlease wait in the lounge until a table is available.")
else:
    print(f"\nYour table is ready, please follow me.")