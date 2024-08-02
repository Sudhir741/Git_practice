tower_height=442
bill_thickness= 0.11
days=1
current_height = 0
daily_bills = 1



while (current_height <= tower_height):
  
    current_height += daily_bills * bill_thickness
    
    daily_bills *= 2
       
    days +=1
    
print(daily_bills)
print(days)

