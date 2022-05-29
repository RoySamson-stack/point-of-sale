import re
import uuid

class Customer:
  def __init__(self,id=None,  name=None, address=None,phonenumber=None):
    self.id = id
    self.name = name 
    self.address = address
    self.phonenumber = phonenumber
    # self.customer()

  def __str__(self):
      return f'{self.id}-- {self.name} -- {self.address} -- {self.phonenumber}'


  
def customer():
      while True:
        print("Select a Customer Operation.")
        print("1. All customer \n2. Add customer \n3. Update customer \n4. Delete customer \n5. Exit" )
        option = int(input("Enter your option"))

        if option == 1:
            all_customers()
            break
        elif option == 2:
            add_customer()
            break
        elif option == 3:
            update_customer()
            break
        elif option == 4:
            delete_customer()
            break
        elif option == 5:
            quit()
        else:  
            print("Invalid option")
            customer()
      
    #adding the customer to the customer list   
def all_customers():
  f = open("customer.txt", "r").readlines()
  
  for line in f:
    print(line)
        
def add_customer():
  id = str(uuid.uuid4())
  name = input("Enter your name").capitalize()
  address = input("Enter the address").capitalize()
  phonenumber = input("Enter the phonenumber")
  new_Customer = Customer(id, name, address, phonenumber)
 
  order=""
  order += str(new_Customer)
  #  str(myuuid) +  " -- "+ name + " -- " + address+ " -- "+  phonenumber 
  with open("customer.txt", 'a') as f:
    f.write(str(order) + "\n")
    print(f"Customer{id} -- {name} been added")
  
    
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
  f = open("customer.txt", "r+").readlines()
  print(f)
  order.extend( [new_name, address, phonenumber])
  for line in f:
    if name+"\n" in line:
      #striing the line with the name
      words=line.strip(line)
      #removing the line thta has a match of the name entered
      f.remove(name+"\n")
    if name in line:
      f.remove(line)
      #here we append the new data that has been entered and putting it in a list
      f.append(str(order))
  print(file)
  for name in f:
    newdata += name
#writing the new data to the file
  f = open("customer.txt", "w")
  f.write(newdata)


def delete_customer():
  name = input("Enter the name you want to search")
  name_a = ""
  newdata = ""
  f = open("customer.txt","r").readlines()
  for line in open("customer.txt", 'r'):
      if re.search(name, line):
          names=line.split()
          name_a += str(names)
  print(name_a)
  id = input("Enter the id to delete")       
  for line in f:
    if id+"\n" in line:
      #strip the line that has a match with the name theat has been entered
      words=line.strip(line)
      #removing the line completely from the file
      f.remove(id+"\n")
    if name in line:
      f.remove(line)
  print("Successfully deleted")    
  print(f)
  for id in f:
    newdata += id

  f = open("customer.txt", "w")
  f.write(newdata)
  
#upddating the customer in the list

if __name__ == "__main__":
 customer()