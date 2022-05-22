class pointOfSale:
  def __init__(self, name, price=0, total=0):
    self.name = name
    # self.orders = []
    self.total = total
    self.customer()
    # self.shop()
    self.price = price
    
    recieve = int(input("Input Money Recieve:\n"))
    print("Total:", self.total)
    print("Change:",recieve - self.total)
    print("*Thank You Come Again!!!*")
    quit()
    
  # def get_name(self):
  #   return self.name
  def customer(self):
    print("Welcome to Onn the way supermarket")
    print("1. Bread 50 \n2.Eggs 15 \n3.Milk 55 \n4.Maize flour 120 \n5.Cash Out \n6.Exit")
    
    name = input("Input your name:")
    item = input("Enter the option")
    quantity = input("Enter the quantity")
    price = 0
    
    
    if item == 1:
      print("Bread 50")
      price = 50 
    elif item == 2:
      print("Eggs 15")
      price = 15  
    elif item == 3:
      print("Milk 55")
      price = 55
      
    total =  price * quantity
    print(total)
    
    def add_customer():
      with open("orders.txt", 'w') as f:
        f.writelines(f'Customer name is {name} who has bought {quantity} {item}s')
        
    def update_customer():
      print("Hello ")
      
      
      
    def delete_customer():
      customer_name = input("Enter the customer name:")
      file = open("orders.txt", "r")
      lines = file.readlines()
      file.close()
      file = open("order.txt", "w")
      for line in lines:
        print(type(customer_name), customer_name, type(line), line)
        if customer_name not in line:
          file.write(line)
      print()
        
       
    
def main():
  a = pointOfSale("Roy")
  #read from the file that is going to save the data
  
  
main()  
  
        