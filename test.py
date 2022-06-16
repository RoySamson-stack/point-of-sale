import re
def replace():
    file = open("customer.txt", "r").readlines()
    name = input("enter new name: ").lower().capitalize()
    for i in file:
        if re.search(name, i):
            spl = i.split()
            print(spl)
replace()