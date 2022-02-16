filename="Chapter10/learning_python.txt"
#10-1
with open(filename) as pythonFile:
    myPython=pythonFile.read()
print("-------------------Output from read()----------------")
print(myPython)

print("--------------Output from for loop inside with.....open---------")
with open(filename) as pythonFile:
    for line in pythonFile:
        print(line)
print("------------------Output from readlines()-------------")
with open(filename) as pythonFile:
    myPython=pythonFile.readlines()

print("Original sentences=", myPython)
for line in myPython:
    print(line)

#10-2
print("-----------Replacing Python with C#----------")
with open(filename) as pythonFile:
    for line in pythonFile:
        print("Original: ", line)
        print("Modified: ", line.replace("Python", "C#"))