import re
import string

def string_re():
  file = open("test.txt", "r")
  fr = file.readlines()
  name = input("Enter the name: ")
  for line in open("test.txt", "r"):
    if re.search(name, line):
      words=line.split()
      print(words)
      new_name = input("Enter the new name: ")
      old_name = words[2]
      line = " "
      old_line = line.join(words)
      new_line = old_line.replace(name, new_name)
      print(new_line)
      print(old_line)
      string = " " 
      new_file = string.join(fr)
      new_data = new_file.replace(name, new_name)
      print(new_file)
      print(new_data)
      
      with open("test.txt", "w") as f:
        f.write(new_data)
        
      
      
string_re()      