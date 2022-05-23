# import re
# from array import array   
  
# def delete_customer():
#   name=input("Enter the name to search ")
#   order =[]
#   f = open("customer.txt", "r+")
#   ft = open("test.txt", "r+")
#   file_t = ft.readlines()
#   file = f.readlines()
#   file.clear()
#   for line in file:
#     if re.search(name, line):
#       words=line.strip(name)
#       file.remove(words)  
#       order.append(file)
#       f.write(str(order)) 
#   print(file)     
     
# def update_customer():
#   name=input("Enter the name to search ")
#   name_update=input("Enter new name")
#   order = {}
#   f = open("customer.txt", "r+")
#   file = f.readlines()
#   for line in file:
#     if re.search(name, line):
#       words=line.strip(name_update)
#       file.replace(words)  
#       order.update({name:name_update})
#       f.write(str(order)) 
#   print(words)     
                    
# # update_customer()   
# delete_customer()        
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


delete_customer()