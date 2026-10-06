d = {}
n = int(input("Enter number of contacts: "))

for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    d[name] = phone

print("Telephone Directory:", d)