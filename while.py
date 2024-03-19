from statistics import mean 

total=0
counter=0

num=int(input("Please enter a number."))

while num !=-1:
    total += num
    counter+=1
    num=int(input("Please enter another number."))
    
    if num == -1:
        print(total)
        break

print(total/counter)







