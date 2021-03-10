# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
  a=int(input())
  set1= set(map(int,input().split()))
  b=int(input())
  set2= set(map(int,input().split()))
  z=set1.issubset(set2)
  print(z)
