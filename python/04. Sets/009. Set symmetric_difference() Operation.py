
# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1= set(map(int,input().split()))
n=int(input())
set2= set(map(int,input().split()))
count=0
sum=0
set3= set1.intersection(set2)
res1=set1.difference(set3)
res2=set2.difference(set3)

print(len(res1)+len(res2))

