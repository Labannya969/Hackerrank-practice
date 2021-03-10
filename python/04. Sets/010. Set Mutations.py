

# Enter your code here. Read input from STDIN. Print output to STDOUT
N=int(input())
sum=0
s=set(map(int, input().split()))
n=int(input())
for i in range(n) :
    choice=input().split()
    set2=set(map(int, input().split()))
    if (choice[0]=="intersection_update"):
      s.intersection_update(set2)
    elif choice[0]=="update":
      s.update(set2)
    elif choice[0]=="symmetric_difference_update":
      s.symmetric_difference_update(set2)
    elif choice[0]=="difference_update":
      s.difference_update(set2)
for i in s:
    sum=sum+i
print (sum)
