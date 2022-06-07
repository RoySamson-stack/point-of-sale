import re
from product import *
from customer import *
import uuid
import random 
import string

random = ''.join([random.choice(string.ascii_letters
            + string.digits) for n in range(4)])
  
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
    PRODUCTS.append(line)  
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
  order = ""
  id = random
  item = input("Enter the item to add to list")
  price = input("Enter the price")
  stock = input("Enter the stock")
  print(item, "added to list ")
  product_details = Product(id, item, price, stock)
  order += str(product_details)
  
  PRODUCTS.append(str(product_details))

  with open("products.txt", "a") as f:
    f.write(str(order) + "\n")
    
  #function to update an item in the list        
def update_item():
  print("1. Name update \n2. Price update \n3. Quantity update \n4. Update all \n5. Exit")
  option=int(input("Enter the option you want pt update"))
  f = open("products.txt", "r").readlines()
  # file = open("products.txt", "w")
  if option == 1:
      file = open("products.txt", "r")
      fr = file.readlines()
      id = input("Enter the customer id: ")
      for line in open("products.txt", "r"):
        if re.search(id, line):
          words=line.split()
          print(words)
          new_name = input("Enter the new name: ")
          old_name = words[2]
          string = " " 
          new_file = string.join(fr)
          new_data = new_file.replace(old_name, new_name)
          # print(new_file)
          # print(new_data)
          
          with open("products.txt", "w") as f:
            f.write(new_data)
        
              
  elif option == 2:
      file = open("products.txt", "r")
      fr = file.readlines()
      id = input("Enter the customer id: ")
      for line in open("products.txt", "r"):
        if re.search(id, line):
          words=line.split()
          print(words)
          new_price = input("Enter the new price: ")
          old_price = words[4]
          string = " " 
          new_file = string.join(fr)
          new_data = new_file.replace(old_price, new_price)
          # print(new_file)
          # print(new_data)
          
          with open("products.txt", "w") as f:
            f.write(new_data)

  elif option == 3:
      file = open("products.txt", "r")
      fr = file.readlines()
      id = input("Enter the customer id: ")
      for line in open("products.txt", "r"):
        if re.search(id, line):
          words=line.split()
          print(words)
          new_quantity = input("Enter the new quantity: ")
          old_quantity = words[6]
          string = " " 
          new_file = string.join(fr)
          new_data = new_file.replace(old_quantity, new_quantity)
          # print(new_file)
          # print(new_data)
          
          with open("products.txt", "w") as f:
            f.write(new_data)
            
  elif option == 4:
          name=input("Enter the name to search ").strip()
          for line in open("products.txt", "r+"):
            if re.search(name, line):
              words=line.split()
              print(words)
          id=input("Enter the id to search ").strip()
          for line in open("products.txt", "r+"):
            if re.search(id, line):
              words=line.split()
              print(words)
          new_name = input("Enter the name update to update ")
          address = input("Enter the address update")
          phonenumber = input("Enter the phonenumber update")
          newdata = ""
          # file = open("products.txt", "r+")
          order=[]
          f = open("products.txt", "r+").readlines()
          print(f)
          order.extend( [new_name, address, phonenumber])
          for line in f:
            if name+"\n" in line:
              #striing the line with the name
              words=line.strip(line)
              #removing the line that has a match of the name entered
              f.remove(name+"\n")
            if name in line:
              f.remove(line)
              #here we append the new data that has been entered and putting it in a list
              f.append(str(order))
          print(f)
          for name in f:
            newdata += Customer(id, new_name, address, phonenumber)
        #writing the new data to the file
          f = open("products.txt", "w")
          f.write(newdata)     
  elif option == 5:
    quit()                     
  else:
    print("Enter a valid answer")


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
  print(item, "has been deleted from list")
  for item in file:
      newdata += item

  f = open("products.txt", "w")
  f.write(newdata)     
    
  
   
if __name__ == "__main__":
 product()
        