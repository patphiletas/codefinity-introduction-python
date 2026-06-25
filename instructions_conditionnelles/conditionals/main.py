# Input variables
product_type = "Dairy"  
day_of_week = "Wednesday"

#if product_type =="Fruits" and day_of_week=="Monday":
 #   print(f"10% discount on {product_type} today")
#elif product_type=="Vegetables" and day_of_week=="Tuesday":
 #   print(f"15% discount on {product_type} today")
#elif product_type=="Dairy" and day_of_week=="Wednesday":
 #   print(f"20% discount on {product_type} today")
#elif product_type=="Other":
 #   print("No discount available")
#else:
 #   print("No special discounts today")

if product_type =="Fruits" and day_of_week=="Monday":
    print(f"10% discount on fruits today!")
elif product_type=="Vegetables" and day_of_week=="Tuesday":
    print(f"15% discount on vegetables today!")
elif product_type=="Dairy" and day_of_week=="Wednesday":
    print(f"20% discount on dairy today!")
elif product_type=="Other":
    print("No discount available.")
else:
    print("No special discounts today.")