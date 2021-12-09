v = 2
while v == 2:
    print("convert fahrenheit to celsius then press 0 ")
    print("convert celsius to fahrenheit then press 1 ")
    value = int(input())
    if value== 0 :
        temp = int(input("Enter temprature value : "))
        c = (temp-32)*(5/9)
        print(c)
        v = int(input("want to continue code press 2 : "))
    elif value== 1:
        temp = int(input("Enter temprature value : "))
        f = ((9/5)*temp)+ 32
        print(f)
        v = int(input("want to continue code press 2 : "))
    else :
        print("Please enter valid input 0 or 1") 
        print()

print("Thank you")