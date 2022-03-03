
from itertools import zip_longest

class Polynominal:
    def __init__(self,*coeffs):
        self.coeffs = coeffs

        def __str__(self):
            return "This is a polynominal class"

        def __add__(self, other):
         p1 = self.coeffs[::]
         p2 = other.coeffs[::]
         res = [sum(t) for t in zip_longest(p1, p2, fillvalue=0)]
         return Polynominal(*res)


p1= Polynominal (4,2,0,1)
p2= Polynominal (2,0,1,4)
p3=Polynominal (...)

print (p1)
print (p3)

