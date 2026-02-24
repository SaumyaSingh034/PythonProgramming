greetings = "Good Morning"

if greetings == "Morning":
    print("condition matches")
    print("Hey this is second line")
else:
    print("condition do not matches")
    print("Hey this is third line")
print("if else conditions is completed")



#for loop
obj = [2,3,4,5,6,7,8,9]

for i in obj:
    print(i*2)

    # sum of first 5 natural numbers 1+2+3+4+5 = 15
sum = 0;
for x in range(1,6):
    sum += x
print("------------------------------------")
print(sum)

print("------------------------------------")
#Jump 2 iterations
for x in range(1,10,2):
    print(x)

print("------------------------------------")
#Skipp first index
for m in range(10):
    print(m)