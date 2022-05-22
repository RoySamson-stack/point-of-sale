def customer():
 
  print("1. Add customer \n2. Update customer \n3. Delete customer \n4. Exit ")
  option = input("Enter the opton you want")
      
    #adding the customer to the customer list     
  def add_customer():
    
    order = []
    name = input("Enter your name")
    item = input("Enter the item name")
    quantity = input("Enter the quaamtity of the item that you want to purchase")
  #try using the for loop to create an object to the next lines
    order.extend([name, item, quantity])
    with open("orders.txt", 'a') as f:
     f.write(str(order) + "\n")

 
  if option == "1":
    add_customer()
    quit()
  elif option == 2:
    update_customer()
  elif option == 3:
    delete_customer()
  else:
    quit()  
#upddating the customer in the list

if __name__ == "__main__":
  customer()