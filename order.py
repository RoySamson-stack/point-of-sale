
    
#   #we are going to print the order of the person by name or the index of the person in the order line 
# def order(): 
#   order = {}
#   order_no = ("Enter the order number")
#   for line in open("orders.txt", "r"):
#     if order_no ==     
    
with open('orders.txt') as books:
    lines = books.readlines()
lines.sort()
with open('books.txt', 'w') as sortedbooks:
    sortedbooks.writelines(lines)