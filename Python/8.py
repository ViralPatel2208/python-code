def fib():
    
    n1 = 0
    n2 = 1
    nth = int(input("Enter nth number : "))
    if nth < 0:
        print("negative number fibonacci not possible")
    elif nth == 1:
        print("fibonaci value is : 0")
    else :
        for i in range(2,nth):
            nth = n1+n2
            n1= n2
            n2=nth
        print(f"nth position fibonacci number is {n2}")
    
fib()