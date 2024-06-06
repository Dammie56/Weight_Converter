weight = int(input("weight: "))
unit = input("(L)bs or (K)g: ")
if unit.upper() == "L":
    print("you weigh", weight * 0.45, "pounds")
elif unit.upper() == "K":
    print("you weigh", weight / 0.45, "kilogram")
