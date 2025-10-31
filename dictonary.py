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
   print(index, ":", (item)["name"],item["price"])

   print(f"Welcome to the store. Here are the items{total_items}")
   cart=[]
   choice=0
   total_cost=0
   choice=input("Choose your item(s)")
   
   checkout=input("Do you wish to continue shopping?(yes/no)")

   while checkout!="no":
        if choice==len(total_items):
          cart.append(input(choice))
          total_cost+=total_items[choice]["price"]
          print(f"You added {cart} into your cart")
          checkout=input("Do you wish to continue shopping?(yes/no)")
   else:
         print("Sorry, we do not have that item")
   if checkout == "No":
         break
   for item in cart: 
    print(f"{item['name']} ${item['price']}")
    print(f"Total: ${total_cost}")
   
             
         
      
   