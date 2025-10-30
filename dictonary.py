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
   print(index, ":", (item)["name"],(item)["price"],(item)["department"])
   

   cart=[]
   choice=0
   total_cost=0

   print("Welcome to store")
   while choice != "done":
      choose=(item)["name","price"]
      choose=input("Choose what you want. When done say done:")
      cart.append(choose)
      print(f"You added {cart} into your cart")
      if choice == "done":
        print(f"Ok, you finish shopping. Here is your total cost{total_cost}")












""" class Calculator():
   def add(x,y):
      print(x+y)
      return x+y
   def add_many(list):
      print(sum(list))
      return(sum(list))
   def subtract(list):
      return list
Calculator.add(15,5) """
""" class Hero:
   def_init_(self,name,money,inventory):
    self.name=name
    self.money=money
    self.inventory=inventory
   def buy(self,item):
     self.inventory.append(item)
     print(f"{self.name} purchased {item} and has {self.item}")
Nathan=Hero("Nathan",0,["Pencil"])
print(Nathan._dict_)
Nathan.buy("Xi Yang") """
