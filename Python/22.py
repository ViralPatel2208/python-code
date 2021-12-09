
print("all values are divisible by 2 and 7 in the range of 1 to 200")
number = []
for i in range(1,201):
    if i%2 == 0 and i%7 == 0 :
        number.append(i)

print(number)