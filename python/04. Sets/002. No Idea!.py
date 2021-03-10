

# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
k=map(int,input().split())
a=set(map(int,input().split()))
b=set(map(int,input().split()))

print(sum((i in a) - (i in b) for i in k))

