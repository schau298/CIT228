def get_formatted_city(city, country, population=""):
    if population:
        info = f"{city}, {country} - Population: {population}"
    else:
        info = f"{city}, {country}"
    return info.title()


