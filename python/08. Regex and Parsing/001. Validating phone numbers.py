# Enter your code here. Read input from STDIN. Print output to STDOUT
import re

n = int(input())
pattern = re.compile(r'^[7-9]\d{9}$')

for i in range(n):
    k=input()

    if pattern.match(k):
        print('YES')
    else:
        print('NO')
