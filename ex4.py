import random
name=input("give file name: ")
fin=open(name, "r")#Ανοίγουμε το αρχείο

#Διαβαζουμε το αρχειο και βαζουμε τις λεξεις στη λιστα lst. Απο καθε λεξη κραταμε μονο τα γραμματα.

lst=[]
for line in fin:
    for word in line.split():#Η συναρτηση split() χωρίζει τις λέξεις ανάλογα με τα κενά.
        word2=""
        for gramma in word:
            if gramma.isalpha():
                word2=word2+gramma
        lst.append(word2)


#Φτιάχνω τη λίστα lst2 που περιέχει τις τριάδες.
lst2=[]
for i in range(len(lst)-2):#Σταματάμε δύο λέξεις νωρίτερα από το τέλος για να φτιάξουμε την τελική τριάδα.
    triada=[]
    for j in range(3):
        triada.append(lst[i+j])
    lst2.append(triada)

pos=random.randint(0,len(lst2)-1)#θεση μιας τυχαιας τριαδας
keimeno=lst2[pos][1]+" "+lst2[pos][2]+" "#Το κειμενο που θα τυπωθει στο τελος και περιλαμβανει την 2η και 3η λεξη της πρωτης τυχαιας τριαδας.
lexeis=2#πληθος λεξεων κειμενου.
found=1

while found==1 and lexeis<200:#Οσο βρισκει τριάδα και οι λέξεις του κειμένου ειναι λιγότερες από 200.
    found=0
    i=0
    while found==0 and i<len(lst2):#Οσο δεν έχουμε βρει μια τριάδα και δεν εχει τελειώσει η λίστα των τριάδων.

        if lst2[i][0]==lst2[pos][1] and lst2[i][1]==lst2[pos][2]:#Ελεγχουμε αν ταιριαζουν η δυο τελευταιες λεξεις της τριαδας που ηδη εχουμε διαλεξει με τις δυο πρωτες της i.
            keimeno=keimeno+lst2[i][2]+" "#προσθετουμε στο είμενο την τρίτη λεξη της i τριαδας.
            lexeis=lexeis+1
            found=1

            del lst2[pos]#σβήνουμε την προηγούμενη τριαδα.
            if i>pos:#Αν το i ειναι μεγαλύτερο απο το pos επειδη σβησαμε το pos το i ειναι μια θεση λιγοτερη στη λιστα.
                pos=i-1
            else:
                pos=i

        else:
            i=i+1
print(keimeno)


fin.close()
