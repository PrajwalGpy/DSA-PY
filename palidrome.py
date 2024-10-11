lend = int(input("How many fibonacci yo whant"))
start = 0
second =1
print(start,second)
for i in range (lend):
    newfib = second + start
    print(newfib)
    start= second
    second = newfib
