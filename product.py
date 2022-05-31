import re
from product import *
from customer import *
import uuid


PRODUCTS=[]
class Product:
  def __init__(self,id=None, item=None, price=None, stock=None):
    self.id = id
    self.item = item 
    self.price= price
    self.stock =  stock
    
  def __str__(self):
      return f'{self.id} -- {self.item} -- {self.price} -- {self.stock}'

def product():
  #printing the option from which a user picks 
  print("1. Search item \n2. Add item \n3. Update item \n4. Delete item \n5. Exit ")
  option = input("Enter the option you want")
  
  for line in open("products.txt", "r"):
    print(str(line))
  while True:
    if option == "1":
      search_item()
      break
    elif option == "2":
      add_item()
      break
    elif option == "3":
      update_item()
      break
    elif option == "4":
      delete_item() 
      break 
    elif option == "5":
      quit()      
    else:
      print("Please enter a valid option")
      product()              
        
def all_items():
  f = open("products.txt", "r").readlines()
  file = open("products.txt", "a")
  for line in f:
    print(line)
    PRODUCTS.update({line})  
   #searching function for a user to input keywords
def search_item():
  items=input("Enter the item to search") 
  menu=[]
  for line in open("products.txt", "r"):
    if re.search(items, line):
      words=line.split()
      menu.append(words)            
  print(words)  
  
  #function to add items to the item list   
def add_item():
  id = str(uuid.uuid4())
  item = input("Enter the item to add to list")
  price = input("Enter the price")
  stock = input("Enter the stock")
  product_details = Product(id, item, price, stock)
  PRODUCTS.append(str(product_details))

  with open("products.txt", "a") as f:
    f.write(str(PRODUCTS) + "\n")
    
  #function to update an item in the list        
def update_item():
  item=input("Enter the item to search ").strip()
  new_item = input("Enter the item name update ")
  price = input("Enter the price update")
  stock = input("Enter the Stock update")
  newdata = ""
  order=[]
  f = open("products.txt", "r+")
  file = f.readlines()
  order.extend( [new_item, price])
  for line in file:
    if item+"\n" in line:
      words=line.strip(line)
      file.remove(item+"\n")
    if item in line:
      file.remove(line)
      file.append(str(order))
  print(file)
  for item in file:
    newdata += item

  f = open("products.txt", "w")
  f.write(newdata)


  #adding an item to the menu 
def delete_item():
  item=input("Enter the item to search ").strip()
  newdata = ""
  f = open("products.txt", "r+")
  file = f.readlines()
  for line in file:
      if item+"\n" in line:
        words=line.strip(line)
        file.remove(item+"\n")
      if item in line:
        file.remove(line)
  print(file)
  for item in file:
      newdata += item

  f = open("products.txt", "w")
  f.write(newdata)     
    
  
   
if __name__ == "__main__":
 product()
        