sen = input("Enter String : ")
 
word = sen.split()

print(word)
nw_str = ""

for i in range(len(word)):
    if i%2 != 0:
        nw_str = nw_str + word[i] + " "

print(nw_str)

