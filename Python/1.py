def facto():
    n = int(input("Enter your number: ")) 
    fac = 1 
    
    if n==1:
        print("factorial is",n)
    elif n== 0:
        print("Factorial of 0 is 1")
    else :
        for i in range(2,n+1):
            fac=fac*i
        print(f"factorial of {n} is : {fac}")
        
facto()