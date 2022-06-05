import re

def purchasetest():
    f = open("customer.txt", "r").readlines()
    p = open("products.txt", "r").readlines()
    
    customer_id = input("Enter the customer id: ")
    for line in f:
        if re.search(customer_id, line):
            words=line.split()
            name = words[1]
            print(name)
            
    while True:        
        product = input(f"{name} enter the products to purchase: ")
        quantity = input("Enter the amount you want: ")    
        for line in p:
            if re.search(product, line):
                words=line.split()
                item_name = words[2]  
                item_price = words[4]
                print(item_name + " " + item_price)
            
purchasetest()           