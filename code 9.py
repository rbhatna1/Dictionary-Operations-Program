def space(): #To make it look good and have proper demarcations
    print()
    print("**********************************************************")
    print()

def frequency(str1):
    dict1={}
    words=str1
    for a in words:
        if a[0].lower() in dict1.keys():
            dict1[a[0].lower()]+=1
        else:
            dict1[a[0].lower()]=1
    print("The dictionary is",dict1)

def wostarting(str1):
    Dict={}
    words=str1.split()
    for a in words:
        if a in Dict.keys():
            y=Dict.get(a[0].lower())
            y.append(a)
            Dict[a[0].lower()]=y
        else:
            Dict[a[0].lower()]=[a]
    print("The dictionary is",Dict)

def printing(dict1):
    key=dict1.keys()
    value=dict1.values()
    lenght=len(dict1)
    print("The keys of dictionary are as follows:",end=" ")
    for a in key:
        print(a,end=" ")
    print()
    print("The keys of values are as follows:",end=" ")
    for a in value:
        print(a,end=" ")
    print()
    print("The lenght of the dictionary is:",lenght)
    
choice=0

while choice!=4:
    print("Choose from one of the folowing options")
    print("1)Choose 1 for the find the frequency of the elements in the string")
    print("2)Choose 2 for the dictinary in which values are keys are based on the starting elements")
    print("3)Choose 3 for the keys,values and lenght of the dictionary")
    print("4)Choose option 4 to exit the code")
    choice=int(input("enter the choice"))
    
    if choice==1:
        space()
        strm=str(input("Enter the string"))
        print(frequency(strm))
        space()
        
    elif choice==2:
        space()
        strm=str(input("Enter the string"))
        wostarting(strm)
        space()
        
    elif choice==3:
        space()
        dict=eval(input("Enter the dictionary"))
        printing(dict)
        space()