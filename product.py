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
          
      
   #adding an item to the menu 
  def add_item():
    products = ""
    item = input("Enter the item to add to list")
    price = input("Enter the price")
    menu.extend([item," -- " ,price])
    with open("products.txt", "a") as f:
      f.write(str(menu))
      
  
  def delete_item():
    product=input("Enter the item name ")
    products = ""
    f = open("products.txt", "r+")
    file = f.readlines()
    for line in file:
     if re.search(product, line):
        words=line.strip(product)
        file.remove(words)  
        products.append(file)
        f.write(str(products)) 
    print(file)    
      
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
        