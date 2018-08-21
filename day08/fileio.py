infile = open("phones.txt","r")
# s = infile.read(10)
# s = infile.readline()
for line in infile:
    print(line)
infile.close()