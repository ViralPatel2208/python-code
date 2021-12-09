print("Enter numbers : and press 0 to EXIT")
number = 1
counter = 0
sum = 0

while number != 0:
    number = int(input(""))
    counter = counter + 1
    sum = sum + number

if counter == 0:
    print("please input number")
else:
    print(f"Avg : {sum/counter}\n Sum : {sum}")