from customer import *
from product import *




'''create a purchase wheeby it reads from the customer and pick the name and check is the user is in the customers list
if not in the list run add_customer function. if in the list, run an input for the user to enter what items they want to purchase and
also check if the product is in the list. then pick the line of the poroduct and strip the price using index and tunr in it into a integer number
then multiply it with the quantity or amount the user wants to give the total 

some after thought is then your can take the user address and ohone number by having an optin if the user wants deleivery or not then print the receipt
having all this information 
'''
def purchase():
  f = open("customer.txt", "r")
  ft = open("products.txt", "r")
  f_customer = f.readlines()  
  ft_product = ft.readlines()
  
  #question do we have to take the customer name from user
  for name in line:
    if name in line:
      print("Welcome to purchase")
      
      
      
purchase()      