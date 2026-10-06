class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def display(self):
        print("Value of a:", self.a)
        print("Value of b:", self.b)

obj = A(10, 20)
obj.display()