print("Cik labo?")

labs=0
labs1=0
labs2=0
count=0
N = int(input("N = "))
M1=int(input("M1 = "))
M2=int(input("M2 = "))
user1a = int(input("a = "))
user1b = int(input("b = "))
mylist= []
for cheack in range(1,N+1):
    if cheack%M1==0 or cheack%M2==0:
          mylist.append(cheack)
          labs+=1
    # else:
    #  print("Vērtības ir vairāk, neka žitonu skaits")

# print(labs)
for i in range(user1a,user1b+1):
    if i in mylist:
     mylist.remove(i)
     labs-=1
print(labs)

user2a = int(input("a = "))
user2b = int(input("b = "))
for i in range(user2a,user2b+1):
    if i in mylist:
     mylist.remove(i)
     labs-=1
print(mylist)
print(f"Atlikusi",labs," žetonu")