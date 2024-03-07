class Trapeze:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def area(self):
        return (self.a + self.b) / 2 * (self.c**2 - ((self.b - self.a) / 2)**0.5)