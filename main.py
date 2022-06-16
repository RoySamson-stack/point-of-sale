from customer import customer
from product import product
from purchase import main_purchases
from queries import queries

def shop():
    while True:
        print('''
                ----Main menu----
                1. Customer Operations 
                2. Product OPerations 
                3. Purchase operation 
                4. Queries 
                5. Exit
        ''')
    

        option = int(input(" Enter your choice: \n"))
        #getting the option and using an if else to help in navigation
        if option == 1:
            customer()
            break
        elif option == 2:
            product()
            break
        elif option == 3:
            main_purchases()
            break
        elif option == 4:
            queries()
        elif option == 5:
          quit()  
        else:
            print("Invalid option kindly enter again")
            shop()

if __name__ == "__main__":
    shop()