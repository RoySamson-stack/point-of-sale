from customer import *

class pointOfSale:
  def __init__(self, name, price=0, total=0):
    self.name = name
    # self.orders = []
    self.total = total
    self.customer()
    # self.shop()
    self.price = price
    
    recieve = int(input("Input Money Recieve:\n"))
    print("Total:", self.total)
    print("Change:",recieve - self.total)
    print("*Thank You Come Again!!!*")
    quit()
    
  #create the customer operations, producst operations, purchase operations , exit 
  def shop():
    print("Welcome to the shop**")
    print("1. Purchase operations \n2. Customer operations \n3.Producst operations \4. Exit")
    operations = input("Enter the operation")
    if operation == "1":
      purchase()
    elif operation == "2":
      customer()
    elif operation == "3":
      products()
    elif operation == '4':
      quit()
    else:
      print("Kindly enter a valid option")
      shop()  
        
        
  
def main():
  a = pointOfSale("Roy")
  #read from the file that is going to save the data
  
  
main()  
  
        