n = int(input("Enter a limit: "))
l = []

for i in range(n):
    x = int(input("Enter number: "))
    if x % 2 == 0:
        l.append(x)

print("Even numbers:", l)
