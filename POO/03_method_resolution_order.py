class A:
    def hablar(self):
        print("Hablando desde A")

class F:
    def hablar(self):
        print("Hablando desde F")

class B(A):
    def hablar(self):
        print("Hablando desde B")

class C(F):
    def hablar(self):
        print("Hablando desde C")

class D(B, C):
    def hablar(self):
        print("Hablando desde D")

d = D()
print(D.mro())
d.hablar()