
import re
#try ny removing the old line and replacing it with the new line 
file = open("customer.txt", "r+")
#create a search function then the user tget the id and uses that 
def update():
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
            #searh for the ol name and remove 
        for line in file:
          old_name = search
          if line.__contains__(old_name):
            newlist = list(line)
            newline=list.replace(old_name, new_data)
            # f.remove(words)
            print(newline) 
              
  elif option == 2:
        name = input("Enter the name")
        for line in open("customer.txt", "r+"):
            if re.search(name, line):
              words=line.split()
              print(words)
              address = input("Enter/Copy and paste the address")
              word = str(words)
              new_address=input("Enter the new address")
              new_data=word.replace(address, new_address)
              print(new_data)

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
update()

