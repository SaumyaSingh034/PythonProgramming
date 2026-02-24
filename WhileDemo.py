count = 4


while count > 0:
    print(count)
    count = count-1

print("While loop execution is done")

# While loop using if statement and break and continue keyword
print("*******************************************************")
num = 9
while num >0:
    if(num == 5):
        num = num-1
        continue
    if(num == 1):
        break
    print(num)
    num = num -1

