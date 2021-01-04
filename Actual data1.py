import re

sum=0

f=open('Actual data1.txt')

for line in f:
    line=line.rstrip()
    sumlist=re.findall('[0-9]+',line)
    for number in sumlist:
        number=int(number)
        sum+=number

print(sum)
