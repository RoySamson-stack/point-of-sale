def update_customer():
  print("1. Update name \n2. Update adress \n3. Update phonenumber \n4. Update all \n5. Exit")
  option = input("Kindly pick an option")
  if option == "1":
    for line in open("customer.txt", "r"):
            if re.search(name, line): 
  elif option == "2":
    address = input("Enter new address")
  elif option == "3":
    phonenumber = input("Enter the new phonenumber")    
  else:
    quit()  
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

