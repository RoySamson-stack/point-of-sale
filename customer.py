import re

def customer():
 
  print("1. Add customer \n2. Update customer \n3. Delete customer \n4. Exit ")
  option = input("Enter the option you want")
      
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
    
    
  #will try to add whereby a specific input field can be updated   
  def update_customer():
    # print("1. Update name \n2. Update adress \n3. Update phonenumber \n4. Update all \n5. Exit")
    # option = input("Kindly pick an option")
    # if option == "1":
    #   new_name = input("Enter the new name")  
    # elif option == "2":
    #   address = input("Enter new address")
    # elif option == "3":
    #   phonenumber = input("Enter the new phonenumber")    
    # else:
    #   quit()  
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
        #striing the line with the name
        words=line.strip(line)
        #removing the line thta has a match of the name entered
        file.remove(name+"\n")
      if name in line:
        file.remove(line)
        #here we append the new data that has been entered and putting it in a list
        file.append(str(order))
    print(file)
    for name in file:
      newdata += name
  #writing the new data to the file
    f = open("customer.txt", "w")
    f.write(newdata)


  def delete_customer():
    name=input("Enter the name to search ").strip()
    newdata = ""
    f = open("customer.txt", "r+")
    file = f.readlines()
    for line in file:
      if name+"\n" in line:
        #strip the line that has a match with the name theat has been entered
        words=line.strip(line)
        #removing the line completely from the file
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