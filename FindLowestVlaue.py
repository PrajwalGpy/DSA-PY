import random as rand

listvalue = []
for i in range(20):
    listvalue.append(rand.randint(1,100))
    

print(listvalue)

low = listvalue[0]
for i in listvalue:
  
    if low >= i :
        low = i 

print("lowerst value",low)        
    
