import re
from customer import *
from product import *

print("1. Search purchases \n2. Purchase operations \n3. Exit")
option = int(input("Enter an option from the above"))

def main_purchases():
  if option == 1:
    search_purchases()
  elif option == 2:
    make_purchases() 
  elif option == 3:
    quit()
       
def search_purchases():
  id = input("Enter the purchase id") 
  order=[]
  for line in open("purchases.txt", "r"):
    if re.search(id, line):
      words=line.split()
      order.append(words)        
  print(words)   
  
#add validation and check if name is twice then use the id the get the customer details
def make_purchases():
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
  #check if the customer order is above the
  product = input("Enter the product name").capitalize()
  quantity = str(input("Enter the quantity"))
  order=""
  receipt = ""
  for line in p:
    if re.search(product, line):
      words=line.split()
      order += str(words)
      # print(order)    
      price = words[4]
      stock = words[6]
      if int(stock) >= int(quantity):
        print(order)
        rmn_stock = int(stock) - int(quantity) 
        total = int(price)  * int(quantity)
        print("Purchase successful")
          #after getting the total update the file on the stock
        print(price)
        print("Remaining stock" , int(rmn_stock))
        # products += 
        #get the whole line and then update the line 
        print("Total" , int(total))
      # print(products)\
        receipt += ("**Receipt**" + "\n" +  "*Items*" + "\n" + product + " = " + str(quantity) + "\n" + "Total:" + str(total) + "\n")
        print(receipt)
      elif stock <= quantity:
        print("The order cannot be completed quantity is too high")  
        make_purchases()
    
  order += id + " " + " Customer name: " + name + " Products: " + product + " Quantity: " + str(quantity) + " Total: " + str(total)
  file = open("purchases.txt", "a")
  file.write(str(order) + "\n")    

 

   

if __name__=="__main__":
  main_purchases()