file = open("test.txt")

#Read all content of the file
#print(file.read())

#Read specific characters
#print(file.read(2))

#read one single line at a time read
#print(file.readline())
#print(file.readline())



for line in file:
    print(line)

file.close()