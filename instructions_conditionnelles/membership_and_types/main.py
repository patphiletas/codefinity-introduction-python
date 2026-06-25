# Product details
description = "Imported honey, raw and unfiltered"
price = "5.99"
count = 120

contains_raw="raw" in description
#print(contains_raw)

contains_Imported="Imported" in description
#print(contains_Imported)

price_is_float=type(price)==float 
#print(price_is_float)

count_is_int=type(count)==int
#print(count_is_int)


print("Contains 'raw':", contains_raw)
print("Contains 'Imported':", contains_Imported)
print("Is price a float?:", price_is_float)
print("Is count an integer?:", count_is_int)