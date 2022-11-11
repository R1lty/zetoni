print("Cik labo?")

labs=0
count=0
mylist= []

N = int(input("N = "))
M1=int(input("M1 = "))
M2=int(input("M2 = "))
step=int(input("G = "))

for cheack in range(1,N+1):
    if cheack%M1==0 or cheack%M2==0:
        mylist.append(cheack)
        labs+=1
while step>count:
    usera=int(input("a = "))
    userb=int(input("b = "))
    for i in range(usera,userb+1):
        if i in mylist:
            mylist.remove(i)
            labs-=1
    print(mylist)
    print(f"Atlikusi",labs," žetonu")
    count+=1
