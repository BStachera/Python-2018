def calc(x):
    return eval(x)

def zasady(a):
    role = ["Aby zakończyć wpisz: end","wpisuj zgodnie z programowaniem","baw się dobrze"]
    return role[a]

def klatka(wynik,znak):
    text = ""
    dlugosc = len(str(wynik))+11
    if znak == " " and dlugość >= 190:
        for j in range(0,190):
            text += znak
    else:       
        if dlugosc >= 216:
            for j in range(0,216):
                text += znak
        else:
            for j in range(0,dlugosc):
                text += znak
	 return text

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
        print (klatka(wynik,"-"))
		print("{0}Wynik: {1}{2}".format("| ",wynik," |"))
		print (klatka(wynik,"-"))
		print("| znaki: {0}{1}|".format(len(str(wynik)), klatka(wynik," ")))
		print (klatka(wynik,"-"))
         
         
