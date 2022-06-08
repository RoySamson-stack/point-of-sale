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
    return f'Purchase id: {self.pur_id} -- Customer id: {self.cus_id} -- items purchased: {self.item_name} -- Price of the items: {self.price} -- quantity of the items: {self.quantity}'  
    
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
          
# def view_items():
      
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
      pur_line = " "
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
                      replace_q = " "
                      new_q = replace_q.join(words)          
                      print(new_q)
                      print(words[2])
                      quantity = int(input("Enter the quantity:\n"))
                      price = words[4]
                      stock = words[6]
                      if int(stock) >= int(quantity):
                          item_name = words[2]
                          total =  int(price) * int(quantity)
                          rem_stock = int(stock) - int(quantity)
                          rem_q = new_q.replace(stock, str(rem_stock))
                          print(rem_q)
                          items.append(item_name)
                          all_total.append(total)
                          all_quantity.append(quantity)
                          print(items)
                          print(all_total)
                          print(total)
                          new_line = pur_line.join(p)
                          new_file = new_line.replace(stock, str(rem_stock))
                          # print(new_file)
                          option = input("Enter Y to continue shopping and N to cashout ").upper()
                          
                          if option == "Y":
                              countinue_buy
                          elif option == "N":   
                              item_total = sum(all_total)
                              print(item_total)
                              print("total:",   item_total)
                              if (int(total) > 0):
                                          receive = int(input("Input Money received:\n"))
                                          if receive >= total:
                                            change = receive - item_total
                                            receipt += ("\t **Receipt**" + "\n \t" +  "*Items*" + "\n \t" + str(items) + " = " + str(quantity) + "\n \t" + "Total:" + str(item_total)  +"\n \t" + "Change:" + str(change))
                                            print(receipt)
                                            print("*****Thank You Come Again!!!*****")
                                          elif receive < total:
                                            print("Money is too little to comlete purchase")  
                              countinue_buy = False            
                              
                      elif stock <= quantity:
                          print("The order cannot be completed quantity is too high")  
                          make_purchase()           #             quit()
                                      
      elif cus_id != int(id_paste):
          print("There is no such id kindly try again")   


      with open("products.txt", "w") as f:
        f.write(new_file)  
      new_order = Purchases(pur_id,  cus_id, items, all_total, all_quantity)#add all quantity 
      final_order=""
      final_order += str(new_order)
      file = open("purchases.txt", "a")
      file.write(str(final_order) + "\n")    

 
   

if __name__=="__main__":
  main_purchases()