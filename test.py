import re

class Purchases:
  
    def __init__(self, pur_id, cus_id, item_name, price, quantity):
        self.pur_id = pur_id
        self.cus_id = cus_id
        self.item_name = item_name
        self.price = price
        self.quantity = quantity


    def __str__(self):
      return f'{self.pur_id} -- {self.cus_id} -- {self.item_name} -- {self.price} -- {self.quantity}'  
  
  
def make_purchase():
        id_paste=input("Enter the customer id: " )
        matches=""
        names = ""
        
        for line in open("customer.txt", "r"):
            if re.search(id_paste, line):
                words=line.split()
                names += str(words)
                cus_id = int(words[0])
                
        if cus_id == int(id_paste):       
            items = []
            all_total = []
            receipt = ""
            countinue_buy = True
            while countinue_buy:
                item =  input("Enter the product id: ").upper()
                for line in open("products.txt", "r"):
                    if re.search(item, line):
                        words=line.split()
                        print(words[2])
                        quantity = int(input("Enter the quantity:\n"))
                        price = words[4]
                        stock = words[6]
                        if int(stock) >= int(quantity):
                            item_name = words[2]
                            total =  int(price) * int(quantity)
                            items.append(item_name)
                            all_total.append(total)
                            print(items)
                            print(all_total)
                            print(total)
                            
                            option = input("Enter the option: ").upper()
                            
                            if option == "Y":
                                countinue_buy
                            elif option == "N":   
                                item_total = sum(all_total)
                                print(item_total)
                                print("total:",   item_total)
                                if (int(total) > 0):
                                            recieve = int(input("Input Money Recieve:\n"))
                                            change = recieve - item_total
                                            receipt += ("**Receipt**" + "\n" +  "*Items*" + "\n" + items + " = " + str(quantity) + "\n" + "Total:" + str(item_total) + "\n" + "Chanege:" + str(change))
                                            print(receipt)
                                            print("*****Thank You Come Again!!!*****")
                                countinue_buy = False            
                                
                        elif stock <= quantity:
                            print("The order cannot be completed quantity is too high")  
                            make_purchase()           #             quit()
                                        
        elif cus_id != int(id_paste):
            print("There is not search id kindly try again")   
        #check if the customer order is above the


if __name__ == "__main__":
    make_purchase()
