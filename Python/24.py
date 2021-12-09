#print("Enter natural numbers : press 0 to exit")
even= 0
odd = 0
#number = 1 

#while number != 0:
#    number = int(input())
#    if number%2 == 0:
#        even+= 1 

#    else:
#        odd+= 1

#print(f"there are {even} even numbers ")
#print(f"there are {odd} odd numbers")

print("Enter natural numbers : ")
t = input()
a = tuple(int (x) for x in t.split())

print(a)

for i in a:
    i = int(i)
    if i%2 == 0:
        even+=1
    else:
        odd+=1

print(f"there are {even} even numbers ")
print(f"there are {odd} odd numbers")
    
