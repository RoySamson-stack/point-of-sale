from customer import *
from product import *

  #making the user pick an option of the service that they want to receive
def shop():
    print("Welcome to the shop**")
    print("1. Customer operations \n2. Product operations \n3.Purchase operations \n4. Exit")
    operation = input("Enter the operation")
    if operation == "1":
      Customer()
    elif operation == "2":
      Product()
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
  
  
  
        