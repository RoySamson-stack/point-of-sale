import re   
  
def delete_customer():
  name=input("Enter the name to search ")
  order = []
  f = open("orders.txt", "r+")
  file = f.readlines()
  for line in file:
    if re.search(name, line):
      words=line.strip(name)
      file.remove(words)  
      order.append(file)
      f.write(str(order)) 
  print(file)     
     
def update_customer():
  name=input("Enter the name to search ")
  name_update=input("Enter new name")
  order = []
  f = open("orders.txt", "r+")
  file = f.readlines()
  for line in file:
    if re.search(name, line):
      words=line.replace(name, name_update)
      # file.remove(words)  
      order.append(file)
      f.truncate()
      f.write(str(order)) 
  print(words)     
                    
      
delete_customer()        