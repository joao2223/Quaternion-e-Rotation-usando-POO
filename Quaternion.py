import math

class Quaternion(object):
 
    def __init__(self, r= 0, i=0, j=0, k=0):
       
        if type(r) == type(self):
            self.r = r.r
            self.i = r.i
            self.j = r.j
            self.k = r.k
        elif type(r) == complex:
            self.r = r.real
            self.i = r.imag
            self.j = 0
            self.k = 0
        else:
            self.r = r
            self.i = 0
            self.j = 0
            self.k = 0

        # imaginary _i_ component
        if type(i) == type(self):
            self.r -= i.i
            self.i += i.r
            self.j += i.k
            self.k -= i.j
        elif type(i) == complex:
            self.r -= i.imag
            self.i += i.real
        else:
            self.i += i

        # imaginary _j_ component
        if type(j) == type(self):
            self.r -= j.j
            self.i -= j.k
            self.j += j.r
            self.k += j.i
        elif type(r) == complex:
            self.j += j.real
            self.k += j.imag
        else:
            self.j += j

        # imaginary _k_ component
        if type(k) == type(self):
            self.r -= k.k
            self.i += k.j
            self.j -= k.i
            self.k += k.r
        elif type(r) == complex:
            self.j -= k.imag
            self.k += k.real
        else:
            self.k += k


    def __neg__(self):
        "    x.__neg__() <==> -x  Mudar o sinal de um quaternion"
        return Quaternion(-self.r, -self.i, -self.j, -self.k)

    def __add__(self, other):
        "    x.__add__(y) <==> x+y  Soma de dois quaternions "
        other = Quaternion(other)
        return Quaternion(self.r + other.r,
                          self.i + other.i,
                          self.j + other.j,
                          self.k + other.k)

    def __mul__(self, other):
        "    x.__mul__(y) <==> x*y  Multiplicaçao entre dois quaternions "
        other = Quaternion(other)
        return Quaternion(self.r*other.r-
self.i*other.i-self.j*other.j-self.k*other.k,
                          self.r*other.i+self.i*other.r+self.j*other.k-self.k*other.j,
                          self.r*other.j+self.j*other.r+self.k*other.i-self.i*other.k,
                          self.r*other.k+self.k*other.r+self.i*other.j-self.j*other.i)


    def __rmul__(self, other):
        "    x.__rmul__(y) <==> y*x"
        other = Quaternion(other)
        return other*self

    def __abs__(self):
        "    x.__abs__() <==> abs(x) Módulo de um quaternion"
        return math.sqrt(self.r*self.r +
                         self.i*self.i +
                         self.j*self.j +
                         self.k*self.k)

    def __radd__(self, other):
        "    x.__radd__(y) <==> y+x"
        return self + other

    def __div__(self, other):
        "    x.__div__(y) <==> x/y  Divisão entre quaternions"
        other = Quaternion(other)
        return self * other.__inv__()
    def __rdiv__(self, other):
        "    x.__rdiv__(y) <==> y/x"
        return Quaternion(other) * self.conjugate() / (abs(self) ** 2)

    def __sub__(self, other):
        "    x.__sub__(y) <==> x-y  Subtração entre quaternions"
        return self + (-other)

    def __rsub__(self, other):
        "    x.__rsub__(y) <==> y-x"
        return other + (-self)
       
    def __inv__(self):
       "  x.__inv__() <==> x^-1  Calcula o inverso de um quaternion"
        return Quaternion(self.r/(self.r*self.r + self.i*self.i + self.j*self.j + self.k*self.k),-self.i/(self.r*self.r + self.i*self.i + self.j*self.j + self.k*self.k),-self.j/(self.r*self.r + self.i*self.i + self.j*self.j + self.k*self.k),-self.k/(self.r*self.r + self.i*self.i + self.j*self.j + self.k*self.k))


       
    def __eq__(self, other):
        "    x.__eq__(y) <==> x==y  Verifica se dois quaternions sao iguais "
        other = Quaternion(other)
        return (self.r == other.r and self.i == other.i and
                self.j == other.j and self.k == other.k)
    def __ne__(self, other):
        "    x.__ne__(y) <==> x!=y  Verifica se dois quaternions sao diferentes"
        return not (self == other)

    def __str__(self):
        "    x.__str__() <==> str(x)  retorna o quaternion escrito na forma a + bi + cj + dk"
        return "%+g%+g*i%+g*j%+g*k" % (self.r, self.i, self.j, self.k)


    def __complex__(self):
        """    x.__complex() -> complex

    Retorna a parte complexa do quaternion
"""
        return complex(self.r, self.i)

    def conjugate(self):
     " x.conjugate() <=> a - bi - cj - dk  Método que calcula o conjugado"
        return Quaternion(self.r, -self.i, -self.j, -self.k)

