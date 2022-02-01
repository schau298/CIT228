games = {
    'Minecraft':{
    'name':"Minecraft",
    'platform':"all",
    'genre':"adventure",
    'co-op':"yes",
    },
    'Rocket League Sideswipe':{
        'name':"Rocket League Sideswipe",
        'platform':"mobile",
        'genre':"sport",
        'co-op':"yes",
    },
    'Halo Infinite':{
        'name':"Halo Infinite",
        'platform':"xbox",
        'genre':"sci-fi",
        'co-op':"yes",
    },
    'Mariokart 8':{
        'name':"Mariokart 8",
        'platform':"nintendo switch",
        'genre':"racing",
        'co-op':"yes",
    },
}

for g, info in games.items():
    print(f"\nGame: {info['name']}")
    platform =info['platform']
    genre=info['genre']
    cooperative=info['co-op']
    
    print(f"\tplatform: {platform}")
    print(f"\tgenre: {genre}")
    print(f"\tco-op: {cooperative}")
    