# f = open("customer.txt", "r")
# file = f.readlines()
 
# print ("List : " ,file) 
 
# res = [x for x in range(len(file)) if file[x] == 10] 
 
# print ("Indices at which element 10 is present: " + str(res))

for data in open("customer.txt", "r"):
        d=int(data['name'])
        if isinstance(d,tuple):
           if set(d).intersection(some_arr):
                print(data['id'])
        if d in some_arr:
              print(data['id'])