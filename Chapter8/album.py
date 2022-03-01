def make_album(name, title, number=''):
    album = {"Artist":name, "Album":title, "Total songs":number}
    for k, v in album.items():
        print("-------------- Album Details Added ---------------------")
        print(f"{k}: {v}\n\n")

quit = ""   

while quit == "":
    artist = input("Add Artist: ")
    title = input("Add Album: ")
    songCount = input("Add Total # of songs: ")
    make_album(artist, title, songCount)
    quit = input("Press 'q' to quit or enter to add more albums!")
    if quit == "q":
        break