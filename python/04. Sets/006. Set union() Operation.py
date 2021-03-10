# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
s1 = set(map(int,input().split()))
n = input()
s2 = set(map(int, input().split()))

result = s1.union(s2)

print(len(result))
