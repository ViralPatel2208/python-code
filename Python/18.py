string = input("Enter String : ")

word = [char for char in string]


print(word)
counter = 0
i = ""
for x in word:
    if x == "a" or x == "e" or x == "i" or x =="o" or x == "u":
        counter = counter + 1

print(counter)