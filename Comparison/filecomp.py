import difflib

f1 = open("F:\\Personal\\file1.txt","rb")
f2 = open("F:\\Personal\\file2.txt","rb")

file1 = f1.read().strip()
file2 = f2.read().strip()

fileOne = file1.splitlines()
fileTwo = file2.splitlines()

# remove the dup lines
nodup_lines = [line for line in fileTwo if line not in fileOne]

# join using newline character
newFileTwo = '\n'.join(nodup_lines)

# write file
outFile = open("F:\\Personal\\diff1.txt","w")
outFile.write(newFileTwo)
outFile.close()