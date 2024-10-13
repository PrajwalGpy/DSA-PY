import random as rand
my_array = [64, 34, 25, 12, 22, 11, 90, 5]
for i in range(20):
    numbers = rand.randint(1,20)
    my_array.append(numbers)



import time

n= len(my_array)
satrt = time.time()
for i in range(n-1):
    for j in range(n-i-1):
        if my_array[j]>my_array[j+1]:
            my_array[j],my_array[j+1] = my_array[j+1],my_array[j]

end = time.time()
print("total time taken ",end-satrt)
print("sorted value is e : ",my_array)
 
