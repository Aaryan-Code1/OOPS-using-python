t = tuple(input("Enter values: ").split())
l = list(t)

l[0] = input("Enter the first value: ")
t = tuple(l)

s = set(t)
s.add(input("Enter values to add: "))

print("Tuple:", t)
print("Set:", s)