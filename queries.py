# how many products sold  how many customers in saved 

f = open("customer.txt", "r")
p = open("products.txt", "r")

def queries():
  print('''
      ---Query menu----
      1. Count customers 
      2. Count products 
      3. Items sorted 
      4. Customer sorted 
      5. Main menu
  ''')
  option = int(input("Enter the option: "))

  if option == 1:
    count_customer()
  elif option == 2:
    count_items()
  elif option == 3:
    item_sort()
  elif option == 4:
    customer_sort()  
  elif option == 5:
    from main import shop
    shop() 
  else:
    print("KIndly enter a valid option")   
    queries()   

def count_customer():
  all_customers = len(f.readlines())
  print( "You have "  + str(all_customers) + " customers")
  
def count_items():
  all_items = len(p.readlines()) 
  print("You have " + str(all_items) + " items")
  
def item_sort():
  with open('products.txt', 'r') as f:
    for line in sorted(f):
        print(line, end='')
        
def customer_sort():
    with open('customer.txt', 'r') as f:
      for line in sorted(f):
        print(line, end='') 
  
  
if __name__ == "__main__":  
  queries()