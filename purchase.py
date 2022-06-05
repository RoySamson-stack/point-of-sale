import re
from customer import *
from product import *
import random
import string



class Purchases():
  def __init__(self,pur_id,  cus_id, item_name, price, quantity ):
    self.pur_id = pur_id
    self.cus_id = cus_id
    self.item_name = item_name
    self.price = price 
    self.quantity = quantity
    
    
  def __str__(self):
    return f'{self.pur_id} -- {self.cus_id} -- {self.item_name} -- {self.price} -- {self.quantity}'  
    
print("1. Search purchases \n2. Purchase operations \n3. Exit")
option = int(input("Enter an option from the above"))
c = open("customer.txt", "r").readlines()
p = open("products.txt", "r").readlines()


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
  # name = input("Enter the customer name:").capitalize()
  id_paste=input("Enter the customer id: " )
  matches=""
  names = " "
  for line in c:
    if re.search(id_paste, line):
      words=line.split()
      names += str(words)
      cus_id = int(words[0])
  '''getting the total '''
 
  #making the validation for the id
  if cus_id == int(id_paste):
      pur_id = str(random.randint(1000, 9999))
      item_name = input("Enter the product name").capitalize()
      quantity = str(input("Enter the quantity"))
      order=""
      receipt = ""
      for line in p:
        if re.search(item_name, line):
          words=line.split()
          order += str(words)
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
            receipt += ("**Receipt**" + "\n" +  "*Items*" + "\n" + item_name + " = " + str(quantity) + "\n" + "Total:" + str(total) + "\n")
            print(receipt)
          elif stock <= quantity:
            print("The order cannot be completed quantity is too high")  
            make_purchases()
  elif cus_id != int(id_paste):
    print("There is not search id kindly try again")   
    #check if the customer order is above the
  

        
  new_order = Purchases(pur_id,  cus_id, item_name, price, quantity ) 
  final_order=""
  final_order += str(new_order)
  file = open("purchases.txt", "a")
  file.write(str(final_order) + "\n")    

 

   

if __name__=="__main__":
  main_purchases()