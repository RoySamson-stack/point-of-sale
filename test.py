import re

def searchage():
  name = input("Ente rthe name you wan tot search")
  age = []
  f = open("customer.txt", "r+")
  file = f.readlines()
  for line in f:
      if re.search(name, line):
          name=line.split()

searchage()   
