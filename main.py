from customer import customer
from product import product
from purchase import main_purchases

def shop():
    while True:
        print(" 1. Customer Operations \n2. Product OPerations \n3. Purchase operation")
        print(" 2 : Product Operations")
        print(" 3 : Purchase Operations")

        option = int(input(" Enter your choice: \n"))

        if option == 1:
            customer()
            break
        elif option == 2:
            product()
            break
        elif option == 3:
            main_purchases()
            break
        else:
            print("Invalid option kindly enter again")
            shop()

if __name__ == "__main__":
    shop()