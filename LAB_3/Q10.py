x=float(input("Enter the first number="))
y=float(input("Enter the second number="))
z=float(input("Enter the third number="))
if x>=0 and y>=0 and z>=0:
    if x>y and x>z:
        print(x,"is the largets number")
    if y>x or y>z:
        print(y,"is the largest number")
    else:
        print(z,"is the largets number")
elif x<0 and y<0 and z<0:
    if x>y and x>z:
        print(x,"is the largets number")
    if y>x or y>z:
        print(y,"is the largest number")
    else:
        print(z,"is the largets number")
else:
    print("Enter the right number,Please")