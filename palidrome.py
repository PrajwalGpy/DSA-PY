num =int(input("Enerte the how many numbers you whant"))

first = 0
second = 1
print(first)
print(second)
for i in range(num):
    newPali = first + second
    print(newPali)
    first =  second
    second = newPali
    
