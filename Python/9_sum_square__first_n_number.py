number = int(input("Enter the value of yoy want to square of sum : "))

temp = 0

for i in range(1,number+1):
    sq = i*i
    sum = temp + sq
    temp = sum

print(temp)


