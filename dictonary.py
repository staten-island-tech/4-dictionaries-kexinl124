def store():
   print("welcome to my store")
choice=0   
cart=[]

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

   while choice != "done":
      input("Keep shopping. When done say done:")
      cart.append("item")

