
values = [1, 2, "Saumya", 4, 5.766]
print(values)
print(values[0])  #1
print(values[3]) #4
print(values[-1])
print(values[1:3])
values.insert(4, "Singh")
print(values)
values.append("Test Automation Engineer")
print(type(values))
print(type(values[0]))

values[3] = "SAUMYA"



# Tuples is immutable and List in mutable
val = (1,2,"rahul", 4.5)
print(val)
print(type(val))
val[2] = "RAHUL"


a = {1: "Saumya", 2: "Test Automation Engineer", "3": 5}
print(a)
print(type(a))
print(a[3])