name=input("give file name")
fin=open(name, "r")#ANOIGOUME TO ARXEIO

#Αρχικοποιούμε τη λίστα με 20 άδειες λίστες.
lst=[]

for i in range(19):
    grammi=[]
    lst.append(grammi)
 #Διαβαζουμε το αρχειο και βαζουμε τις λεξεις στη λιστα lst. Απο καθε λεξη κραταμε μονο τα γραμματα.
    
for line in fin:
    for word in line.split():#Η συναρτηση split() χωριζει τις λεξεις αναλογα με τα κενα.
        word2=""
        for gramma in word:
            if gramma.isalpha():
                word2=word2+gramma
        mikos=len(word2)

        if mikos<20 and mikos>0:
            lst[mikos-1].append(word2)#η καθε λέξη αποθηκεύεται στην λιστα που ειναι στη θεση ιση με το μηκος -1.
        
for i in range(10):#θα ελέγξω τις μισες λίστες. Καθε λίστα στη θεση i θα την ελεγχω με τη λιστα που ειναι στη θεση pos γιατι το αθροισμα του μηκους τους ειναι 20
    pos=20-i-2
    while len(lst[i])>0 and len(lst[pos])>0:
        a=lst[i].pop(0)#στο α βαζουμε το στοιχείο που ειναι στην πρωτη θεση τησ λιστας i. και βγαινει απο τη λιστα
        b=lst[pos].pop(0)
        zeugari=a+" "+b
        print(zeugari)

fin.close()
    
    
        
        


