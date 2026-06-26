vegetables = ["tomatoes", "potatoes", "onions"]
vegetables.remove("onions")
vegetables.append("carrots")
vegetables.append("cucumbers")
vegetables.sort()

print(f"Updated Vegetable Inventory: {vegetables}")

if vegetables[0]=="carrots":
    print("Carrots are already in the list.")
elif vegetables[1]=="cucumbers":
    print("Cucumbers are already in the list.")