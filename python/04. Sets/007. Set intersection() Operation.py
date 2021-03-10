# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
set1= set(map(int,input().split()))
n=int(input())
set2= set(map(int,input().split()))
set3= set1.intersection(set2)
print(len(set3))
