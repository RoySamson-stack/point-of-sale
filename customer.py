import re

def customer():
 
  print("1. Add customer \n2. Update customer \n3. Delete customer \n4. Exit ")
  option = input("Enter the opton you want")
      
    #adding the customer to the customer list     
  def add_customer():
    name = input("Enter your name")
    address = input("Enter the address")
    phonenumber = input("Enter the phonenumber")
    order=[]
  #try using the for loop to create an object to the next lines
    order.extend( [name, address, phonenumber])
    with open("customer.txt", 'a') as f:
     f.write(str(order) + "\n")
     
     
  def delete_customer():
    name=input("Enter the name to search ")
    order = []
    f = open("customer.txt", "r+")
    file = f.readlines()
    for line in file:
      if re.search(name, line):
        words=line.strip(name)
        file.remove(words)  
        order.append(file)
        f.write(str(order)) 
    print(file)    

 
  if option == "1":
    add_customer()
  elif option == "2":
    update_customer()
  elif option == "3":
    delete_customer()
  else:
    quit()  
#upddating the customer in the list

if __name__ == "__main__":
  customer()