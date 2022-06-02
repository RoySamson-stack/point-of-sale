#for the update part I ma going to create a file where the new data will be saved.
import re

def delete_customer():
  name = input("Enter the name you want to search")
  name_a = ""
  newdata = ""
  p = open("products.txt", "r").readlines()
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
      print(words)
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
  
delete_customer()  