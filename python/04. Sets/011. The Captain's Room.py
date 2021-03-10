

# Enter your code here. Read input from STDIN. Print output to STDOUT
d=input()
a=map(int,input().split())
s1=set() #all unique room number
s2=set()  #all unique room number occur more than once
for i in a:
    if i in s1:
        s2.add(i)
    else:
        s1.add(i)
s3=s1.difference(s2)

print(s3.pop())
