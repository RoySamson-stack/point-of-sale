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
    items=input("Enter the product item") 
    menu=[]
    for line in open("products.txt", "r"):
      if line.find(items):
        words=line.split()
        menu.append(words)            
    print(words)  
    
    #function to add items to the item list   
  def add_item():
    products = ""
    item = input("Enter the item to add to list")
    price = input("Enter the price")
    menu.extend([item," -- " ,price])
    with open("products.txt", "a") as f:
      f.write(str(menu))
      
   #function to update an item in the list        
  def update_item():
    item=input("Enter the item to search ").strip()
    new_item = input("Enter the item update to update ")
    price = input("Enter the address update")
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
  def delete_customer():
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
        