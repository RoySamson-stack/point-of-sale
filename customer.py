import re
import uuid
import fileinput
import random
import string


CUSTOMERS=[]
  

  
  
class Customer:
  def __init__(self,id=None,  name=None, address=None,phonenumber=None):
    self.id = id
    self.name = name 
    self.address = address
    self.phonenumber = phonenumber
    # self.customer()

  def __str__(self):
      return f'{self.id} -- {self.name} -- {self.address} -- {self.phonenumber}'
 

    
def customer():
  
      while True:
        print("Select a Customer Operation.")
        print('''
          ----Customer menu-----    
          1. All customer 
          2. Add customer 
          3. Update customer 
          4. Delete customer
          5. Search customer 
          6. Main menu
        ''' )
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
            search_customer()
        elif option == 6:
          from main import shop
          shop()    
        else:  
            print("Invalid option")
            customer()
      
    #adding the customer to the customer list   
def all_customers():
  f = open("customer.txt", "r").readlines()
  file = open("customer.txt", "a")
  for line in f:
    print(line)
    CUSTOMERS.append(line)
  customer()
    
def search_customer():
  id=input("Enter the customer name to search") 
  ids=[]
  for line in open("customer.txt", "r"):
    if re.search(id, line):
      words=line.split()
      ids.append(words)        
      print(words)   
        
def add_customer():
  # print (random)
  id = str(random.randint(1000, 9999))
  name = input("Enter your name").lower().capitalize()
  address = input("Enter the address").lower().capitalize()
  phonenumber = input("Enter the phonenumber")
  new_Customer = Customer(id, name, address, phonenumber)
 
  order=""
  order += str(new_Customer)
  #  str(myuuid) +  " -- "+ name + " -- " + address+ " -- "+  phonenumber 
  with open("customer.txt", 'a') as f:
    f.write(str(order) + "\n")
    print(f"Customer{id} -- {name} been added")
  
  customer()
  #will try to add whereby a specific input field can be updated 
  #strip the line then split the name the change the name or specific input field  
def update_customer():
  print("1. Name update \n2. Address update \n3. Phonenumber update \n4. Back to customer menu \n5. Exit")
  option=int(input("Enter the option you want pt update"))
  f = open("customer.txt", "r").readlines()
  # file = open("customer.txt", "w")
  if option == 1:
        file = open("customer.txt", "r")
        fr = file.readlines()
        id = input("Enter the customer id: ")
        for line in open("customer.txt", "r"):
          if re.search(id, line):
            words=line.split()
            print(words)
            new_name = input("Enter the new name: ")
            old_name = words[2]
            string = " " 
            new_file = string.join(fr)
            new_data = new_file.replace(old_name, new_name)
            # print(new_file)
            # print(new_data)
            
            with open("customer.txt", "w") as f:
              f.write(new_data)
              print("customer updated")
        customer()
              
  elif option == 2:
      file = open("customer.txt", "r")
      fr = file.readlines()
      id = input("Enter the customer id: ")
      for line in open("customer.txt", "r"):
        if re.search(id, line):
          words=line.split()
          print(words)
          new_address = input("Enter the new address: ")
          old_address = words[4]
          string = " " 
          new_file = string.join(fr)
          new_data = new_file.replace(old_address, new_address)
          # print(new_file)
          # print(new_data)
          
          with open("customer.txt", "w") as f:
            f.write(new_data)
            print("address updated")
          customer()
            
  elif option == 3:
      file = open("customer.txt", "r")
      fr = file.readlines()
      id = input("Enter the customer id: ")
      for line in open("customer.txt", "r"):
        if re.search(id, line):
          words=line.split()
          print(words)
          new_number = input("Enter the new number: ")
          old_number = words[6]
          string = " " 
          new_file = string.join(fr)
          new_data = new_file.replace(old_number, new_number)
          # print(new_file)
          # print(new_data)
          
          with open("customer.txt", "w") as f:
            f.write(new_data)
            print("phonenumber updated")
            customer()
  elif option == 4:
      customer()
  elif option == 5:
      quit()
  else:
      print("Kindly enter a valid option")
      update()                      
        

def delete_customer():

  newdata = ""
  f = open("customer.txt","r").readlines()

  id = input("Enter the id to delete")       
  for line in f:
    if id+"\n" in line:
      #strip the line that has a match with the name theat has been entered
      words=line.strip(line)
      #removing the line completely from the file
      f.remove(id+"\n")
    if id in line:
      f.remove(line)
  print("Successfully deleted")    
  # print(f)
  
  for id in f:
    newdata += id

  f = open("customer.txt", "w")
  f.write(newdata)
  


#upddating the customer in the list

if __name__ == "__main__":
 customer()