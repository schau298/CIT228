current_users = ["bob", "jim", "joe", "don", "sal"]
new_users = ["bob", "jim","meg","flo","lea"]
for username in new_users and current_users:
    if username == "bob":
        print("bob is already taken")
    elif username == "jim":
        print("jim is already taken")
    elif username == "meg":
        print("meg is available")
    elif username == "flo":
        print("flo is avilable")
    elif username == "lea":
        print("lea is avilable")

lower_users=[]
for user in current_users:
    lower_users.append(user.lower())