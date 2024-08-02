'''
year= int(input("enter year :" ))
if (year%400 ==0):
    print(year, "leap year")
else:
    if (year%100 !=0):
        if (year %4==0):          
            print(year, "leap year")
        else:
            print(year,"not leap")
    else:
        print(year,"not leap")
        
'''
'''
year= int(input("enter year :" ))

if (year%400):
    print(year, "is leap year")
elif (year%100 !=0 and year%4==0):
    print(year,"leap year")
else:
    print(year,"not leap year")

'''
year= int(input("enter year :" ))
if (year%400 or (year%100 !=0 and year%4==0)):
    print(year, "is leap year")
else:
    print(year,"not leap year")  
    
