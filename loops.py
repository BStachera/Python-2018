 #Ternary
a = 3 if 3**2 > 9 else 14
print (a)
#loop 
a = input("type something")

for x in range(0,len(a),1):
     if x%3 == 0:
         print(" ",a[x])
     elif x%3 == 1:
         print(2*" ",a[x])
     elif x%3 == 2:
         print(3*" ",a[x])