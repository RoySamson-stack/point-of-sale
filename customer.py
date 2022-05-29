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
  print("1. Name update \n2. Address update \n3. Phonenumber update \n4. Update all \n5. Exit")
  option=int(input("Enter the option you want pt update"))
  f = open("customer.txt", "r").readlines()
  if option == 1:
        search=input("Enter the name to search (copy the id)")
        for line in open("customer.txt", "r"):
          if re.search(search, line):
            name_search=line.split()
            print(name_search)
        id = input("Paste the id")
        for line in open("customer.txt", "r+"):
          if re.search(id, line):
            old_name = search
            f = open("customer.txt", "r+")
            words=line.split()
            print(words)
            word = str(words)
            # id = input("Enter the id to delete")                   
            new_name=input("Enter the new name")
            new_data=word.replace(old_name, new_name)
            # print(str(new_data))
            file.writelines(new_data)
            #search for the line name and remove 
        for line in file:
          old_name = search
          if line.__contains__(old_name):
            newlist = list(line)
            newline=list.replace(old_name, new_data)
            # f.remove(words)
            print(newline) 
              
  elif option == 2:
        f = open("customer.txt", "r+")
        name = input("Enter the name (copy the id)")
        for line in open("customer.txt", "r+"):
            if re.search(name, line):
              words=line.split()
              print(words)
              #asking user for id to get the correct user to avoid updating wrong user
              id=input("Copy and paste the id")
              for line in open("customer.txt", "r+"):
                if re.search(id, line):
                  word_s=line.split()
                  print(word_s)
              address = input("Enter/Copy and paste the address")
              word = str(words)
              new_address=input("Enter the new address")
              #repace the old address with the new address
              new_data=word.replace(address, new_address)
              print(new_data)
              f.writelines(new_data)

  elif option == 3:
        new_info = ""
        name = input("Enter the name")
        for line in open("customer.txt", "r+"):
            if re.search(name, line):
              words=line.split()
              print(words)
              phonenumber = input("Enter/Copy and paste the phonenumber")
              word = str(words)
              new_phonenumber=input("Enter the new address")
              new_data=word.replace(phonenumber, new_phonenumber)
              # print(new_data)
              with open("customer.txt", "a") as f:
                new_info += str(new_data)
                f.writelines(new_info)
  elif option == 4:
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
              #removing the line that has a match of the name entered
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
  elif option == 5:
    quit()                     
  else:
    print("Enter a valid answer")

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