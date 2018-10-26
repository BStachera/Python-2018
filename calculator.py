def calc(x):
    return eval(x)

def zasady(a):
    role = ["Aby zakończyć wpisz: end","wpisuj zgodnie z programowaniem","baw się dobrze"]
    return role[a]
def spacje(spacje):
	space = ""
	for x in range(spacje):
		space += " "
	return space

print("\n{:=^10}".format(""),end="")
print(" HOW TO USE CALCULATOR ",end="")
print("{:=^10}\n".format(""),end="")
for i in range(0,3):
	print("{:<3}||".format(""),end="")
	print(zasady(i))
    
lop = True
while lop == True:
	x= input("")
	if x == "end":
		lop = False
	else:
		wynik = calc(x)
		y = int(len(str(wynik)))
		spacje = int((len("{0}Wynik: {1}{2}".format("| ",wynik," |"))))- 9 -int((len(str(y))))
		print (spacje)
		print ("{0}Wynik: {1}{2}".format("| ",wynik," |"))
		print ("| znaki: {0}{1}|".format(y,spacje(spacje)))

         
         
