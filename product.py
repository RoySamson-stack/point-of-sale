import re
from menu import *

def product():
  
  #printing the option from which a user picks 
  print("1. Search item \n2. Add item \n3. Update item \n4. Delete item \n5. Exit ")
  option = input("Enter the opton you want")
  
  #reading the menu and printing it to the terminal for the user to see
  for line in open("products.txt", "r"):
    print(str(line))
   
   
   #searching function for a user to input keywords
   
  def search_item():
    items=input("Enter the product name") 
    menu=[]
    for line in open("products.txt", "r"):
      if line.find(items):
        words=line.split()
        menu.append(words)            
    print(words)     
          
  def update_customer():
    name=input("Enter the name to search ").strip()
    new_name = input("Enter the name update to update ")
    address = input("Enter the address update")
    phonenumber = input("Enter the phonenumber update")
    newdata = ""
    order=[]
    f = open("products.txt", "r+")
    file = f.readlines()
    order.extend( [new_name, address, phonenumber])
    for line in file:
      if name+"\n" in line:
        words=line.strip(line)
        file.remove(name+"\n")
      if name in line:
        file.remove(line)
        file.append(str(order))
    print(file)
    for name in file:
      newdata += name

    f = open("products.txt", "w")
    f.write(newdata)


   #adding an item to the menu 
  def add_item():
    products = ""
    item = input("Enter the item to add to list")
    price = input("Enter the price")
    menu.extend([item," -- " ,price])
    with open("products.txt", "a") as f:
      f.write(str(menu))
      
  
  def delete_customer():
    name=input("Enter the name to search ").strip()
    newdata = ""
    f = open("products.txt", "r+")
    file = f.readlines()
    for line in file:
        if name+"\n" in line:
          words=line.strip(line)
          file.remove(name+"\n")
        if name in line:
          file.remove(line)
    print(file)
    for name in file:
        newdata += name

    f = open("products.txt", "w")
    f.write(newdata)     
      
  if option == "1":
    search_item()
  elif option == "2":
    add_item()
  elif option == "3":
    update_item()
  elif option == "4":
    delete_item()  
  elif option == "5":
    quit()      
  else:
    print("Please enter a valid option")              
       
   
if __name__ == "__main__":
  product()
        