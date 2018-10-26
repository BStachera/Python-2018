 #Ternary
a = 3 if 3**2 > 9 else 14
print (a)
#loop 
#a = input("type something")

'''for x in range(0,len(a),1):
     if x%3 == 0:
         print(" ",a[x])
     elif x%3 == 1:
         print(2*" ",a[x])
     elif x%3 == 2:
         print(3*" ",a[x])
'''
for i in range(2):
     for j in range(3):
         print(j)

for i in range(1,11):
    print('{:<3}|'.format(i),end="")
    for j in range(1,11):
        print("{:>4} ".format(i*j),end="")
    if i == 1:
        print("\n{:-^53}".format(""),end="")
    print("")
    
print(len(" liczba znaków to:"))