import json
glossary={
    "dictionary": "Python data type that stores key:value pairs",
    "tuple":"List of items that do not change",
    "pop()":"Method that removes the last item from the list AND it allows you to save the value removed in a variable",
    "subscript":"Numerical value given to each item in a list starting at 0",
    "append":"The append method adds new items to the end of a list.",
    "list": "Python data type stored as a list of items that can be changed.",
    "elif": "Python version of an if/else",
    "comments": "lines that begin with #",
    "del": "command used to remove a key value pair from the dictionary.",
    "boolean": "variables that evaluate to true or false",
}

for k,v in glossary.items():
    print (k.title())
    print ("\t",v.title())

def menu():
    selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    while selection!=1 and selection!=2 and selection!=3 and selection!=4:
        print("You made an invalid selection, please try again")
        selection = int(input("1-create file, 2-read file, 3-add to file, 4-quit  "))
    return selection

def create(object):
    overwrite = input("You are about to create a new file, existing data will be overwritten (q to quit, any key to continue) ")
    if overwrite !="q":
        with open("Chapter10/glossary.json", "w") as write_file:
            json.dump(object, write_file, indent=4, sort_keys=True)
            print("glossary.json has been created")

def append(new_item):
    with open("Chapter10/glossary.json", "r+") as add_file:
        glossaryDictionary = json.load(add_file)
        glossaryDictionary.update(new_item)
        add_file.seek(0)
        json.dump(glossaryDictionary, add_file, indent=4, sort_keys=True)
        print("Data has been added to Chapter10/glossary.json")

def read():
    try:
        with open("Chapter10/glossary.json") as read_file:
            glossaryDictionary = json.load(read_file)
    except FileNotFoundError:
        print("The file doesn't exist or cannot be found.")
        print("Please make a different menu selection")      
    else: 
        for key, value in glossaryDictionary.items():
            print(key.title(), ": ",value.title())       
        
def get_key():
    term = input("Enter a python term: ")
    return term

def get_value():
    definition = input("Enter the definition for your term: ")
    return definition

choice=menu()
while choice != 4:
    if choice == 1:
        create(glossary)
    elif choice == 2:
        read()
    elif choice == 3:
        term=get_key()
        definition=get_value()
        new_glossary_entry={term:definition}
        append(new_glossary_entry)
    else:
        print("The option you selected is not available, please try again")        
    choice=menu()
