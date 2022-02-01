games={
    "Xbox":["Minecraft","Gears of War","Halo Infinite"],
    "Mobile":["Sideswipe","Brawl Stars","Clash of Clans"],
    "Playstation":["Spiderman"]
}
print("-----------Games and Platforms")
for key, value in games.items():
    if type(value)==list:
        print(f"The best game(s) on {key.title()}  are: ")
        for v in value:
            print("\t\t\t\t",v)
print("-----------------Platforms---------------")
for key in games.keys():
    print(key.title())
print("------------------------Games------------------")
for value in games.values():
    if type(value)==list:
        for v in value:
            print(v)
        else:
            print(value)

