l1=int(input("enter the first side of tringle(cm):"))
l2=int(input("enter the second side of tringle(cm):"))
l3=int(input("enter the third side of tringle(cm):"))
s = (l1+l2+l3)/2
area = (s*(s-l1)*(s-l2)*(s-l3))**(1/2)
print("Area of tringlr is",area,"cm*cm")