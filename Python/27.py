number = input("Enter number between 200 to 220 : ")
b = []
a = [char for char in number]

for i in a:
    i = int(i)

    if i%2 != 0:
        b.append(i)

print(b)
    