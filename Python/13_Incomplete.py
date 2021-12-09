def remove():

    string = input("Enter string : ")
    #str = [char for char in string]
    #print(str)

    rm = str(input("which postion of character you want to remove : "))

    i = ''

    for j in range(len(string)):
        if rm < i:
            i = i + string[j]
        eif j == rm:
            continue
        else :
            print("N")


    print(i)    
remove()