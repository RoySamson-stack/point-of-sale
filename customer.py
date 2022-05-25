import re
import uuid

class Customer:
  def __init__(self):
    self.customer()
    
  def customer(self):
        while True:
          print("Select a Customer Operation.")
          print("1. All customer \n2. Add customer \n3. Update customer \n4. Delete customer \n5. Exit" )
          option = int(input("Enter your option"))

          if option == 1:
              all_customers()
          elif option == 2:
              add_customer()
          elif option == 3:
              update_customer()
          elif option == 4:
              delete_customer()
          elif option == 5:
              quit()
          else:  
              print("Invalid option")
              customer()
      
    #adding the customer to the customer list   
def all_customers():
  f = open("customer.txt", "r")
  file = f.readlines()
  
  for line in file:
    print(line)
        
def add_customer():
  myuuid = uuid.uuid4()
  name = input("Enter your name")
  address = input("Enter the address")
  phonenumber = input("Enter the phonenumber")
  order=[]
#try using the for loop to create an object to the next lines
  order.extend( [myuuid, name, address, phonenumber])
  with open("customer.txt", 'a') as f:
    f.write(str(order) + "\n")
    print("Customer has been added")
  
    
  #will try to add whereby a specific input field can be updated 
  #strip the line then split the name the change the name or specific input field  
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
  print(file)
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

 
  
#upddating the customer in the list

if __name__ == "__main__":
 Customer()