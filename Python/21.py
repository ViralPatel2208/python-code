print("Enter 3 sides of a triangle whose sum of both sides is greater than 3rd side.")
x=float(input("Enter 1st side. "))
y=float(input("Enter 2nd side. "))
z=float(input("Enter 3rd side. "))
if(x==y):
    if(x==z):
        print("The triangle is equilateral triangle.")
    else:
        print("The triangle is isosceles triangle.")
else:
    print("The triangle is scalene triangle.")