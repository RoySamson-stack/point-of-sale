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
     
  def update_customer():
    name=input("Enter the name to search ").strip()
    new_name = input("Enter the name update to update ")
    address = input("Enter the address update")
    phonenumber = input("Enter the phonenumber update")
    newdata = ""
    order=[]
    f = open("customer.txt", "r+")
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

    f = open("customer.txt", "w")
    f.write(newdata)


  def delete_customer():
    name=input("Enter the name to search ").strip()
    newdata = ""
    f = open("customer.txt", "r+")
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

    f = open("customer.txt", "w")
    f.write(newdata)   

 
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