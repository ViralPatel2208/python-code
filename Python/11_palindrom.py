
def split():

    word = input("Enter Name : ")
    char =  [char for char in word]
    print(char)
    rev = char[::-1]
    #print(rev)
    if char == rev :
        print("Enter word is Palindrom")
    else :
        print("Enter word is not palindrom")


def f2():

    split()

f2()

