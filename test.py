import os
import customer,product
import re

PRODUCTS = []
CUSTOMERS = []
PURCHASES = []
# purchases class
class Purchase:

    def __init__(self,name,p_id,quantity,total):

        self.name = name
        self.p_id = p_id
        self.quantity = quantity
        self.total = total
    
    # magic method repr for representing objects
    def __repr__(self):
        return f"('{self.name}','{self.p_id}','{self.quantity}','{self.total}')"
# purchase menu

def purchase_menu():
    

    # creating options  
    while True:
        print("""
        Purchases Menu
        1. Make a purchase
        2. List all purchases
        3. Search for a purchase
        4. Quit
        """)  
        choice4 = int(input("Select Purchase option:"))  

        # choice 1
        if choice4 == 1:
            print()
            make_purchase()
            
        elif choice4 == 2:
            print()
            list_purchases()
        elif choice4 == 3:
            print()
            search_purchase()
        elif choice4 == 4:
            print()
            break
        else:
            print()
            print('Oops! Incorrect choice. Please try again! ')


# required functions

# function to make purchase 
def make_purchase():
    customer.all_customers()
    product.all_items()
    # enter customer id 
    customer_exists = False
    product_exists = False
    id = input("Enter customer id to purchase: ")
    # check if the customer id exists
    for line in open("customer.txt", "r"):
        if re.match(id, line):
            customer_exists = True
            name = line.split()
            name = name[2]
            print("Customer name is:  " , name)
            break
            # print("Customer exists")

    
    # check if product exists
    p_id = input("Enter product id to purchase: ") 
    for line in open("products.txt", "r"):
        if re.match(p_id, line):
            products = line.split()
            product_exists = True
            print(products)
    #         # print("Product exists")
      
    if customer_exists and product_exists:
        # make purchase
        quantity = int(input("Enter quantity of product to purchase: "))
        # check if amount is available
        for i in range(len(product.PRODUCTS)):
            if p_id == products[0]:
                name = products[2]
                stock = int(products[6])
                if stock >= quantity:
                    # update product amount
                    balance = stock - quantity
                    # print("Product available")
                    price = float(products[4])
                    total = price * quantity
                    output = Purchase(name,p_id, stock,total)
                    PURCHASES.append(output)
                    print("Purchase successfull!!!")
                    print()
                    print(PURCHASES)
                    # update_products()
                    while True:
                        print ("""
                        Choose purchase option:
                        1. Make another purchase
                        2. Checkout
                        3.Exit
                        """)
                        choice7 = int(input("Choose a purchase option: "))
                        if choice7 ==1:
                            make_purchase()
                        elif choice7 ==2:
                            checkout()
                            break
                        elif choice7 ==3:
                            print()
                            break
                        else:
                            print("Invalid option!!!")
                        
                # else:
                #     print("Quantity in stock is below " +str(quantity) + ' : ' +"quantity available:"+ str(stock) )
                #     make_purchase()
                #     break
  
    else:
        print("Invalid details!!!")
        
        

def handle_file():
    with open('purchase.txt','a')as fo:
        for p in PURCHASES:
            print(p.name+','+p.p_id+','+str(p.quantity)+','+str(p.total),file=fo)
            # break            

def checkout():
    total_purchase = 0
    for p in PURCHASES:
        # pur = p.split(',')
        cost = float(p.total)
        total_purchase += cost
    print()
    print("Total: "+ str(total_purchase))
    print("purchase complete")
    update_products()
    handle_file()


def update_products():
    for p in PURCHASES:
        # pur = p.split(',')
        product_id = p.p_id
        product_quantity = int(p.quantity)
        # print("quantity: "+ str(quantity))
        # open products file
        file = open('products.txt','r')
        temp = open('temp.txt','w')
        s = ' '
        while(s):
            s = file.readline()
            L = s.split(',')
            if len(s)>0:
                if (L[0]) == product_id:
                    name = L[1]
                    quantity = int(L[2])
                    price = L[3]
                    updated_q = quantity - p_quantity
                    temp.write(str(product_id)+','+ name+','+str(updated_q)+','+str(price))
                else:
                    temp.write(s)
        temp.close()
        file.close()
        os.remove('products.txt')
        os.rename('temp.txt','products.txt')
        print("Inventory updated")
        print("Stock remaining for " + name + ':' +str(updated_q))
                    
# function to list all purchases
def list_purchases():
    purchases = []
    purchases_list = []
    with open('purchases.txt','r') as f:
        for line in f.readlines():
            purchases.append(line)
     # remove \n
    for p in purchases:
        lists = p.replace('\n','')
        purchases_list.append(lists)
    print(purchases_list)
    
# function to search for a purchase with customer id or product id
def search_purchase():
    total = 0
    items_bought = 0
    # menu for search options
    while True:
        print("""
        
        Search options:
        1. Search by customer name
        2. Search by product id
        3. Exit
        """)
        choice5 = int(input("Select search option:")) 
        if choice5 ==1:
            fo = open('purchases.txt','r')
            name = input("Please enter customer name to search: ").capitalize()
            s = ' '
            while(s):
                s = fo.readline()
                L = s.split(',')
                if len(s)>0:
                    if (L[0]) == name:
                        # print(L)
                        p_id = L[1]
                        quantity = L[2]
                        price = float(L[3])
                        print( )
                        # Calculate total spend by customer
                        total += price
                        print("customer name: ",name)
                        print("Product id: ",p_id)
                        print("Quantity purchased: ",quantity)
                        print("Price: ",price)


                        # print(name ,pro_id,quantity,price)
            print('----------------')
            print("Total spent by " + name + ' : ' + str(total))
            break
                
    
        elif choice5 ==2:
            fo = open('purchases.txt','r')
            id = input("Please enter product id to search: ")
            s = ' '
            while(s):
                s = fo.readline()
                L = s.split(',')
                if len(s)>0:
                    if (L[1]) == id:
                        # print(L)
                        name = L[0]
                        quantity = int(L[2])
                        price = float(L[3])
                        print( )
                        # Calculate total spent on the product
                        total += price          
                        # items bought
                        items_bought += quantity
                        print("customer name: ",name)
                        print("product id: ",id)
                        print("Quantity purchased: ",quantity)
                        print("Price: ",price)

                        # print(name ,id,quantity,price)
             
            print('----------------')
            print("Total: " + str(total))
            print("No of products purchased:" + str(items_bought))

            
            
        elif choice5 == 3:
            print()
            break
        else:
            print()
            print('Oops! Incorrect choice. Please try again! ')


if __name__ == "__main__":
  purchase_menu()