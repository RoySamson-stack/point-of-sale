from menu import *

def purchase():
  
  
  #printing the option from which a user picks 
  print("1. Add item \n2. Update item \n3. Delete item \n4. Exit ")
  option = input("Enter the opton you want")
  
  #reading the menu and printing it to the terminal for the user to see
  for line in open("menu.txt", "r"):
    print(line)
   
   
   
   #adding an item to the menu 
  def add_item():
    menu = []
    item = input("Enter the item to add to list")
    price = input("Enter the price")
    menu.extent([item," -- " ,price])
    with open("menu.txt", "a") as f:
      f.write(str(menu))
      
      
  if option == "1":
    add_item()
  elif option == "2":
    update_item()
  elif option == "3":
    delete_option()
  elif option == "4":
    quit()
  else:
    print("Please enter a valid option")              
       
   
if __name__ == "__main__":
  purchase()
        