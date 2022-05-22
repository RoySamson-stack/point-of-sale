    
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
  name = input("Enter the name for the data you want to delete")
  with open('orders.txt') as books:
    lines = books.readlines()
  lines.sort()
  with open('orders.txt', 'w') as sortedbooks:
    sortedbooks.writelines(lines)
        
        
        
def delete_customer():
  name = input("Enter the name for the data you want to delete")
  with open("orders.txt", 'r') as f:
    data = f.readlines()
  with open("orders.txt", 'w') as f:
    for line in data:
      if line.remove("\n") == name:
        f.write(line)
 
 
update_customer()        