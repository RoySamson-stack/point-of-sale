# how many products sold  how many customers in saved 

f = open("customer.txt", "r")
p = open("products.txt", "r")

def count_customer():
  all_customers = len(f.readlines())
  print( "You have "  + str(all_customers )+ " customers")
  
def count_items():
  all_items = len(p.readlines()) 
  print("You have " + str(all_items) + " items")
  
def item_sort():
  with open('products.txt', 'r') as f:
    for line in sorted(f):
        print(line, end='')
  
  
  
#create a fucntion to get number of items sold  
count_customer() 
count_items()
item_sort()