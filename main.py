from customer import *
from product import *

class pointOfSale:
  def __init__(self, name, price=0, total=0):
    self.name = name
    self.total = total
    self.price = price
    self.shop()
    
    recieve = int(input("Input Money Recieve:\n"))
    print("Total:", self.total)
    print("Change:",recieve - self.total)
    print("*Thank You Come Again!!!*")
    quit()
    
    
    #making the user pick an option of the service that they want to receive
  def shop():
    print("Welcome to the shop**")
    print("1. Customer operations \n2. Product operations \n3.Purchase operations \n4. Exit")
    operation = input("Enter the operation")
    if operation == "1":
      customer()
    elif operation == "2":
      product()
    elif operation == "3":
      purchase()
    elif operation == '4':
      quit()
    else:
      print("Kindly enter a valid option")
      shop()  
        
        
  
if __name__ == "__main__":
  shop()
  #read from the file that is going to save the data
  
  
  
        