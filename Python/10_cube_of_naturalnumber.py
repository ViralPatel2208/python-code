number = int(input("Enter the value : "))

temp = 0

if number < 0 :
    print("Please enter valid natural number :)")

else :
    for i in range(1,number+1):
        sq = i*i*i
        sum = sq + temp 
        temp = sum
    
    print(temp)