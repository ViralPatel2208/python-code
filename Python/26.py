str = input("Enter your str : ")

alpha = numbers = special =  0

for i in range(len(str)):
    if(str[i].isalpha()):
        alpha+=1
    elif(str[i].isdigit()):
        numbers+=1
    else :
        special+=1 

print(f"number of alphabets are : {alpha}")
print(f"number of digits are : {numbers}")
print(f"number of special character are : {special}")
