name=input("give name of file you want to read: ")
fin=open(name,"r")

lst=[]

for line in fin:
    for word in line:
        for letter in word:
            anti=chr(128-ord(letter))#με την ord παίρνουμε τον ascii χαρακτήρα καθε γραμματος και με την chr παιρνουμε τον αντικατοπτρικο χαρακτηρα.
            lst.append(anti)


lst.reverse()#αντιστρέφει τα στοιχεία της λίστας
keimeno=""

for i in range(len(lst)):#παίρνουμε τα στοιχεία της λίστας και τα ενώνουμε σε ενα string.
    keimeno=keimeno+lst[i]

print(keimeno)

fin.close()
