fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    firstspace = line.find(' ')
    space = firstspace + 2
    secondspace = line.find(' ',space)
    print(line[firstspace+1:secondspace])
    count = count + 1



print("There were", count, "lines in the file with From as the first word")

#Another way to complete this exereise

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    count = count + 1
    print(words[1])

print("There were", count, "lines in the file with From as the first word")

