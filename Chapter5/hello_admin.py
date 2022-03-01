usernames=["admin","Bob","Sally","Jane","Jim"]
print("---------------------Exercise 5-8 ---------------------------")
for user in usernames:
    if user == "admin":
        print("Hello Admin, would you like to see a status report?")
    elif user == "Bob":
        print("Hello Bob, Welcome back!")
    elif user == "Sally":
        print("Hello Sally, Welcome back!")
    elif user == "Jane":
        print("Hello Jane, Welcome back!")
    elif user == "Jim":
        print("Hello Jim, Welcome back!")

print("---------------------Exercise 5-9 ---------------------------")
for user in usernames:
    if user == "admin":
        print("Hello Admin, would you like to see a status report?")
    else:
        print("Hello", user.title(), " thank you for logging in again.")
else:
    print("We need to get some users ASAP!")
    