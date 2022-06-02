import re
from customer import *
from product import *


# option = input("Enter the option")

# def search_item():
#   items=input("Enter the product item") 
#   menu=[]
#   for line in open("products.txt", "r"):
#     if line.find(items):
#       words=line.split()
#       menu.append(words)            
#   print(words) 
  
  
#add validation and check if name is twice then use the id the get the customer details
def purchases():
  c = open("customer.txt", "r").readlines()
  p = open("products.txt", "r").readlines()
  name = input("Enter the customer name:").capitalize()
  names = " "
  for line in c:
    if re.search(name, line):
      words=line.split()
      names += str(words)
  print(names)
  '''getting the total '''
  id=input("Paste the customer id")
  matches=""
  for line in c:
    if id+"\n" in line:
      words=line.strip(line)
      print(words)
  #add stock
  product = input("Enter the product name").capitalize()
  quantity = input("Enter the quantity")
  products = ""
  order=""
  for line in p:
    if re.search(product, line):
      words=line.split()
      products += str(words) 
      price = words[4]
      stock = words[6]
      rmn_stock = int(stock) - int(quantity) 
      total = int(price)  * int(quantity)
      #after getting the total update the file on the stock
      print(price)
      print("Remaining stock" , int(rmn_stock))
      # products += 
      #get the whole line and then update the line 
      print("Total" , int(total))
    # print(products)\
  order += id + " " + " Customer name: " + name + " Products: " + product + " Quantity: " + str(quantity) + " Total: " + str(total)
  file = open("purchases.txt", "a")
  file.write(str(order) + "\n")    

 

   

if __name__=="__main__":
  purchases()