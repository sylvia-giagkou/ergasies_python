import random

x=0
while x<=0:
    x=int(input("give X: "))

y=0
while y<=0:
    y=int(input("give y: "))


plithos=x*y#πληθος τετραγωνων

s=0

for ep in range(100):
    #Κατασκευη του πινακα.
    pinakas=[]
    count1=0# μετράει το πληθος των S
    count2=0# μετράει το πληθος των O


    for i in range(x):
        grammi=[]
        for j in range(y):

            if count1<(plithos/2):#Αν δεν εχουμε βάλει τα μισα S.
                pos=random.randint(0,1)#Διαλεγουμε τυχαια 0 ή 1.

                if pos==0 or count2==(plithos/2):#Αν πηραμε 0 ή εχουμε βαλει τα μισα Ο βαζουμε S.
                    grammi.append("S")
                    count1=count1+1
                else:
                    grammi.append("O")
                    count2=count2+1
            else:
                grammi.append("O")

        pinakas.append(grammi)
        

    #βρισκω τα οριζοντια SOS
    for i in range(x):
        for j in range(y-2):
            if pinakas[i][j]=="S" and pinakas[i][j+1]=="O" and pinakas[i][j+2]=="S":
                s=s+1

    #βρισκω τα καθετα SOS
    for j in range(y):
        for i in range(x-2):
            if pinakas[i][j]=="S" and pinakas[i+1][j]=="O" and pinakas[i+2][j]=="S":
                s=s+1
    #βρισκω τα διαγωνια SOS
    for i in range(x-2):
        for j in range(y-2):
            if pinakas[i][j]=="S" and pinakas[i+1][j+1]=="O" and pinakas[i+2][j+2]=="S":
                s=s+1

    #βρισκω τα αντιδιαγωνια SOS
    for i in range(x-2):
        for j in range(y):
            if(j>1):
                if pinakas[i][j]=="S" and pinakas[i+1][j-1]=="O" and pinakas[i+2][j-2]=="S":
                    s=s+1

average=float(s/100)
print(average)

    

    

    
                
                
        

    


        
                
                
                
                

