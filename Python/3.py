number = input("Enter any number: ")
sum = 0
for i in number:
    i = int(i)
    temp = i**len(number)
    sum = temp + sum
print(sum)
number = int(number) 
if number == sum :
    print("This number is Armstrong number")
else :
    print("This number is not Armstrong number")