number = int(input("Enter number : "))

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print("Not Prime Number")
            break
    else :
        print("Prime number")