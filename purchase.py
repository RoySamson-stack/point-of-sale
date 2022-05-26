import re

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
  #   # else:
  #   #   print("The name is not in the customer list")  
  #   #   quit()
  # print(names)
  product = input("Enter the product name")
  quantity = input("Enter the quantity")
  products = ""
  for line in p:
    if re.search(product, line):
      words=line.split()
      products += str(words) 
      price = words[2]
      print(int(price))
      total = price  + int(quantity)
      print(str(total))
  print(str(products))    
    # else:
    #   print("The item is not in the list")  
    #   quit()


 

   

if __name__=="__main__":
  purchases()