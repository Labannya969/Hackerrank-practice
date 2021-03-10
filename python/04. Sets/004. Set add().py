
# Enter your code here. Read input from STDIN. Print output to STDOUT
n= int(input())
s=set()
for i in range(1,n+1):
  country= input()
  s.add(country)
print(len(s))

