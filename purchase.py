import re
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
  for line in p:
    if re.search(product, line):
      words=line.split()
      products += str(words) 
      price = words[5]
      stock = words[7]
      rmn_stock = int(stock) - int(quantity) 
      total = int(price)  * int(quantity)
      #after getting the total update the file on the stock
      print(price)
      print("Remaining stock" , int(rmn_stock))
      print("Total" , int(total))
    print(products)
  
  # print(products)    

 

   

if __name__=="__main__":
  purchases()