total_items = [

       {"name": "water",
        "price": 2.00,
        "department": "liquid/beverages"},

       {"name": "orange juice",
      "price": 4.00,
      "department": "liquid/beverages"},

         {"name":"strawberry ",
         "price": 6.50,
         "department":"fruits"},

         {"name":"milk",
        "price": 5.00,
        "department":"liquid/beverages"}

]
for index, item in enumerate(total_items):
      print(index, ":", (item)["name"])
      total_items[0]["name"]
print("Welcome to the store.")
cart=[]
cost=0
choice=int(input("Choose your item(s)"))
cart.append(total_items[choice])
print(f"You added {total_items[choice]['name']} into your cart")
cost += total_items[choice]["price"]


while True:
      checkout=input("Do you wish to continue shopping?(yes/no)")
      if checkout=="yes":
             choice= int(input("What else would you like to buy"))
      cart.append(total_items[choice])
      print(f"You added {total_items[choice]['name']} into your cart")
      cost += total_items[choice]["price"]
            
      if checkout=="no":
          break

for item in cart: 
              print(f"${int(item['price'])}")
print(f"Total: ${cost}")
   
             
         
      
   