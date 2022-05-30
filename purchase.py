import re
from customer import *
from product import *


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
    # print(products)
  order += name + " Products: " + product + " Quantity: " + str(quantity) + " Total: " + str(total)
  file = open("purchases.txt", "a")
  file.write(order)    

 

   

if __name__=="__main__":
  purchases()