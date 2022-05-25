import re

def searchage():
  name = input("Enter the name you want to search")
  
  name_a = []
  newdata = ""
  f = open("customer.txt","r")
  file = f.readlines()
  for line in open("customer.txt", 'r'):
      if re.search(name, line):
          ages=line.split()
          name_a.append(ages)
  print(name_a)
  id = input("Enter the id to delete")       
  for line in file:
    if id+"\n" in line:
      #strip the line that has a match with the name theat has been entered
      words=line.strip(line)
      #removing the line completely from the file
      file.remove(id+"\n")
    if name in line:
      file.remove(line)
  print(file)
  for id in file:
    newdata += id

  f = open("customer.txt", "w")
  f.write(newdata)  
searchage()   
