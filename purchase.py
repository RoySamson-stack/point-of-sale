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
    
c = open("customer.txt", "r").readlines()
p = open("products.txt", "r").readlines()
pur_id = str(random.randint(1000, 9999))


def main_purchases():
  while True:
      print("1. Search Item \n2. Search purchases \n3. Make a purchase \n4. Exit")
      option = int(input("Enter an option from the above"))
     

      if option == 1:
        search_item()
      elif option == 2:
        search_purchases() 
      elif option == 3:
        make_purchases()
      elif option == 4:
        quit()  
          
    
def search_item():
  items=input("Enter the item to search") 
  menu=[]
  for line in open("products.txt", "r"):
    if re.search(items, line):
      words=line.split()
      menu.append(words)            
  print(words)  
         
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
      id_paste=input("Enter the customer id: " )
      matches=""
      names = ""
      
      for line in open("customer.txt", "r"):
          if re.search(id_paste, line):
              words=line.split()
              names += str(words)
              cus_id = int(words[0])
              
      if cus_id == int(id_paste):
          items = []
          all_total = []
          all_quantity = []
          receipt = ""
          countinue_buy = True
          while countinue_buy:
              item =  input("Enter the product id: ").upper()
              for line in open("products.txt", "r"):
                  if re.search(item, line):
                      words=line.split()
                      print(words[2])
                      quantity = int(input("Enter the quantity:\n"))
                      price = words[4]
                      stock = words[6]
                      if int(stock) >= int(quantity):
                          item_name = words[2]
                          total =  int(price) * int(quantity)
                          items.append(item_name)
                          all_total.append(total)
                          all_quantity.append(quantity)
                          print(items)
                          print(all_total)
                          print(total)
                          
                          print("")
                          option = input("Enter Y to continue shopping and N to cashout ").upper()
                          
                          if option == "Y":
                              countinue_buy
                          elif option == "N":   
                              item_total = sum(all_total)
                              print(item_total)
                              print("total:",   item_total)
                              if (int(total) > 0):
                                          recieve = int(input("Input Money Recieve:\n"))
                                          change = recieve - item_total
                                          receipt += ("**Receipt**" + "\n" +  "*Items*" + "\n" + str(items) + " = " + str(quantity) + "\n" + "Total:" + str(item_total) + "\n" + "Chanege:" + str(change))
                                          print(receipt)
                                          print("*****Thank You Come Again!!!*****")
                              countinue_buy = False            
                              
                      elif stock <= quantity:
                          print("The order cannot be completed quantity is too high")  
                          make_purchase()           #             quit()
                                      
      elif cus_id != int(id_paste):
          print("There is not search id kindly try again")   


        
      new_order = Purchases(pur_id,  cus_id, items, all_total, all_quantity)#add all quantity 
      final_order=""
      final_order += str(new_order)
      file = open("purchases.txt", "a")
      file.write(str(final_order) + "\n")    

 
#use replace for the updating of the quanti
   

if __name__=="__main__":
  main_purchases()