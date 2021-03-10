#list mutations
N=int(input())
s=[]
for i in range(N) :
    choice=input().split()
    if choice[0]=="append":
      s.append(int(choice[1]))
    elif choice[0]=="insert":
      s.insert(int(choice[1]),int(choice[2]))
    elif choice[0]=="sort":
      s.sort()
    elif choice[0]=="pop":
      s.pop()
    elif choice[0]=="reverse":
      s.reverse()
    elif choice[0]=="remove":
        s.remove(int(choice[1]))
    elif choice[0]=="print" :
      print(s)

      
      
