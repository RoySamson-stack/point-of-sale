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
        quit()
  '''getting the total '''
  product = input("Enter the product name")
  quantity = input("Enter the quantity")
  products = ""
  for line in p:
    if re.search(product, line):
      words=line.split()
      products += str(words) 
      price = words[2]
      total = int(price)  * int(quantity)
      print(price)
      print(int(total))
  # print(products)    

 

   

if __name__=="__main__":
  purchases()