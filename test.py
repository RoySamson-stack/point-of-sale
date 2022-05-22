    
# def update_customer():
#   with open("orders.txt", "r") as up_cus:
#       lines = up_cus.readlines()
#   lines.sort()
#   with open("orders.txt", "w") as sortedorder:
#       sortedorder.writelines(lines)   
      
      
# update_customer()  
#this is the wotking function for customer    
# def add_customer():
#   order = []
#   name = input("Enter your name")
#   item = input("Enter the item name")
#   quantity = input("Enter the quaamtity of the item that you want to purchase")
#   #try using the for loop to create an object to the next lines
#   order.extend([name, item, quantity])
#   with open("orders.txt", 'a') as f:
#     f.write(str(order) + "\n")
      
      
  ##use replace for the update    

def update_customer():
  item = input("Enter the product name to update")
  order = []
  with open("orders.txt", "r+") as f:
    order.append(item)
    f.append(str(order))
  print(order)
  
  
def delete_customer():
  lines = []
# read file
with open(r"orders.txt", 'r') as fp:
    # read an store all lines into list
    lines = fp.readlines()

# Write file
with open(r"orders.txt", 'w') as fp:
    # iterate each line
    for number, line in enumerate(lines):
        # delete line 5 and 8. or pass any Nth line you want to remove
        # note list index starts from 0
        if number not in [4, 7]:
            fp.write(line)
# add_customer()        
# delete_customer()       
update_customer()