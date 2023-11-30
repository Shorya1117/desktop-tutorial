# text=(input("enter the sentance:"))
# vowels="AEIOUaeiou"
# count=0
# for i in text:
#     if i in vowels:
#         count+=1
# print(count)
# count_1=0
# count_2=0
# count_3=0
# count_4=0
# count_5=0

# for i in text:
#     if i=='A' or i=="a":
#         count_1+=1
#     elif i=='e' or i=="E":
#         count_2+=1
#     elif i=='i' or i=='I':
#         count_3+=1
#     elif i=="o" or i=="O":
#         count_4+=1
#     elif i=="U" or i=="u":
#         count_5+=1

# a={"vowels"}
# a.append(count_1)
# a.append(count_2)
# a.append(count_3)
# a.append(count_4)
# a.append(count_5)
# a.sort()
# d={'vowels':}
# d["vowels"]=a


p=input("enter the paragraph:")
d={}
vowels="AEIOUaeiou"
for x in p:
    if x in vowels:
        d[x]=p.count(x)
print(d)
v=d.values()
print(v)