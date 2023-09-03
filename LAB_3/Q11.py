print("cheak the number is armstrong number is or not".title().center(50))
digit=(input("Enter the 3 digit number:"))
y=int(digit)
count=0
x=len(digit)
if y>=0:
  if x==1:
    print("Entered the three digit no.")
  elif (x==2):
    print("enter the 3 digit no.")
  elif (x==3):
    once=(y%10)
    tense=(y%100)//10
    hund=(y%1000)//100
    if y==((once**x)+(tense**x)+(hund**x)):
      print("Entered number is Armstrong number",y)
    else:
      print("this no. is not a armstrong no.")
  else:
    print("please try again")
else:
  print("enter the valid")