import re

handle = open('text_actual.txt')
numlist = list()
for line in handle:
	foundnum=re.findall('[0-9]+', line)
	numlist=numlist+foundnum

total=0;
for num in numlist:
	total=total+int(num);
print total