class pointOfSale:
  def __init__(self, total, name,):
    self.name = name
    self.orders = []
    self.total = 0
    self.customer()
    self.shop()
    
    recieve = int(input("Input Money Recieve:\n"))
    print("Total:", self.total)
    print("Change:",recieve - self.total)
    print("*Thank You Come Again!!!*")
    quit()
    
  def get_name(self):
    return self.name
      
  def customer(self):
    print("Welcome to Onn the way supermarket")
    print("1. Bread 50 \n2.Eggs 15 \n3.Milk 55 \n4.Maize flour 120 \n5.Cash Out \n6.Exit")
    
    name = input("Input your name:")
    item = input("Enter the option")
    quantity = input("Enter the quantity")
    
    
    if item == 1:
      print("Bread 50")
      price = 50 
    elif item == 2:
      print("Eggs 15")
      price = 15  
    elif item == 3:
      print("Milk 55")
      price = 55
      
    total = price * quantity
    print(total)

      
  def shop(self):
    self.total = self.total + total
    print("All done")
   
  def order(self, order):
    if self.order > 0:
      self.orders.append(order)
      print("Order:", order)
    
def main():
  a = pointOfSale()
  
  
main()  
  
        