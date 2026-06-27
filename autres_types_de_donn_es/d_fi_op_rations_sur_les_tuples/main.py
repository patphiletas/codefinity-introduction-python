# Current inventory on shelf
shelf = ("apples", "oranges", "bananas", "apples", "grapes", "bananas", "apples")

if "grapes" in shelf:
    grape_count=shelf.count("grapes")

if "apples" in shelf:
    apple_count=shelf.count("apples")

if "oranges" in shelf:
    orange_index=shelf.index("oranges")

if "bananas" in shelf:
    banana_index=shelf.index("bananas")

print(f"Number of Apples: {apple_count}")
    
print(f"First Banana Index: {banana_index}")

if apple_count<5:
    print("Apples need to be restocked.")
else:
    print("Apples are sufficiently stocked.")

if grape_count<=1:
    print("Grapes need to be restocked.")
else:
    print("Grapes are sufficiently stocked.")

if "oranges" in shelf:
    print(f"Oranges are at index: {orange_index}")
else:
    print("Oranges are out of stock.")

