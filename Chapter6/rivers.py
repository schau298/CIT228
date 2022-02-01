rivers={
    "Volga":["Russia"],
    "Rio de la Plata":["Brazil","Paraguay","Uruguay","Argentina"],
    "Yellow":["China"]
}

print("---------------------- Rivers & Countries ----------------")
for key, value in rivers.items():
    print(f"The {key.title()} river flows through {value}")

print("------------ River ------------------")
for key in rivers.keys():
    print(key.title())

print("------------------- Countries --------------------")
for value in rivers.values():
    print(value)