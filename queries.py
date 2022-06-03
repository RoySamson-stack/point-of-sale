# how many products sold  how many customers in saved 

f = open("customer.txt", "r")
p = open("products.txt", "r")
def count_customer():
  all_customers = len(f.readlines())
  print( "You have "  + str(all_customers )+ " customers")
  
def count_items():
  all_items = len(p.readlines()) 
  print("You have " + str(all_items) + " items")
  
count_customer() 
count_items()