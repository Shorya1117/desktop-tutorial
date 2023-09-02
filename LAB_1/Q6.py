a=int(input("Enter the coefficient of x**2(with sign):"))
b=int(input("Enter the coefficent of x(with sign):"))
c=int(input("enter the constant value(with sign):"))
d=(b**2)-4*a*c
r_1= ((-b)+((d)**(1/2)))/(2*a)
r_2= ((-b)-((d)**(1/2)))/(2*a)
print("roots of your quadatic equation(",a,"x2+",b,"x+",c,") is",r_1,",",r_2)
