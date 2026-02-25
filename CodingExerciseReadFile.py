with open('file1.txt') as file:
    for line in file.readlines():
        print(line, end="")

count = 0
with open('file1.txt') as file:
    for line in file.readlines():
        count = count+1
    print("{} {}".format("Total number of lines:",count))
