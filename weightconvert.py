weight = float(input("Enter your Weight : "))
unit = input("Enter the unit (KG or G)")

if unit == "KG" or weight == "kg":
    weight = weight * 1000
    print(weight)
elif unit == "G" or weight == "g" :
    weight = weight /1000
    print(weight)


