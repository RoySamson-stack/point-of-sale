def search_name():
    name=input("enter the letter (s): ")
    valid_names=[]
    for line in open("menu.txt", 'r'):
        if line.startswith(name.capitalize()):
            words=line.split()
            valid_names.append(words)
            
    print(valid_names)
search_name()    