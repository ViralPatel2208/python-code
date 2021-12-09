def fib():
    
    n1 = 0
    n2 = 1
    nth =0
    print(n1)
    print(n2)
    while nth < 200:
        nth = n1+n2
        print(n2)
        n1= n2
        n2=nth
    
fib()
