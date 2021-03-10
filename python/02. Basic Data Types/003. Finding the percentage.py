n= int(input())
sum=0
line_holder = []
for i in range(0,n):
  line = input()
  line_holder.append(line)

name=input()
for line in line_holder:
  if name in line:
    line=line.split()
    new_items = [item for item in line if  item.isdigit()] #['52', '56', '60']
    
length=len(new_items)


p = [int(i) for i in new_items]
for j in p:
  sum+=j
avg=float(sum/length)
print("{:0.2f}".format(avg))


