import re
from product import *
from customer import *
import uuid
import random 
import string


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
  print('''
      ---Product menu----
      1. Search item
      2. Add item
      3. Update item
      4. Delete item 
      5.Main menu
      6. Exit
  ''')
  option = int(input("Enter the option you want"))
  
  for line in open("products.txt", "r"):
    print(str(line))
  while True:
    if option == 1:
      search_item()
      break
    elif option == 2:
      add_item()
      break
    elif option == 3:
      update_item()
      break
    elif option == 4:
      delete_item() 
      break 
    elif option == 5:
      from main import shop
      shop()  
    elif option == 6:
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
  items=input("Enter the item id: ")
  menu=[]
  for line in open("products.txt", "r"):
    if re.search(items, line):
      words=line.split()
      id = words[0]
      if int(items) == int(id):
        print(words)
      elif int(items) != int(id):
        print("Product does not exist")  
  product()      
  
  #function to add items to the item list   
def add_item():
  order = ""
  id = str(random.randint(1000, 9999))
  item = input("Enter the item to add to list").upper().replace(" ", "")
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
  print("1. Name update \n2. Price update \n3. Quantity update \n4. Back to Product  menu")
  option=int(input("Enter the option you want pt update"))
  f = open("products.txt", "r").readlines()
  # file = open("products.txt", "w")
  if option == 1:
      file = open("products.txt", "r")
      fr = file.readlines()
      id = input("Enter the product id: ")
      for line in open("products.txt", "r"):
        if re.search(id, line):
          words=line.split()
          print(words)
          new_name = input("Enter the new name: ").lower().capitalize().replace(" ", "")
          old_name = words[2]
          string = " " 
          new_file = string.join(fr)
          new_data = new_file.replace(old_name, new_name)
          # print(new_file)
          # print(new_data)
          
          with open("products.txt", "w") as f:
            f.write(new_data)
            print("Product updated")
          product()
        
              
  elif option == 2:
      file = open("products.txt", "r")
      fr = file.readlines()
      id = input("Enter the product id: ")
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
            print("Price updated")
          product()  

  elif option == 3:
      file = open("products.txt", "r")
      fr = file.readlines()
      id = input("Enter the product id: ")
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
            print("Quantity updated")
          product()  
            
  elif option == 4:
    product()
  elif option == 5:
    quit()
  else:
    print("KIndly enter a valid option")    
  

  #adding an item to the menu 
def delete_item():
  
  newdata = ""
  f = open("products.txt","r").readlines()

  id = input("Enter the id to delete")       
  for line in f:
    if id+"\n" in line:
      #strip the line that has a match with the name theat has been entered
      words=line.strip(line)
      #removing the line completely from the file
      f.remove(id+"\n")
    if id in line:
      f.remove(line)
  print("Successfully deleted")    
  # print(f)
  
  for id in f:
    newdata += id

  f = open("products.txt", "w")
  f.write(newdata)    
    
  
   
if __name__ == "__main__":
 product()
        