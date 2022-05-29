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
            #searh for the ol name and remove 
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
              id=input("Copy and paste the id")
              for line in open("customer.txt", "r+"):
                if re.search(id, line):
                  word_s=line.split()
                  print(word_s)
              address = input("Enter/Copy and paste the address")
              word = str(words)
              new_address=input("Enter the new address")
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