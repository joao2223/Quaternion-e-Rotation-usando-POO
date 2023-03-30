import math
#classe dos quartenions, como no arquivo anterior
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
        "    x.__neg__() <==> -x"
        return Quaternion(-self.r, -self.i, -self.j, -self.k)

    def __add__(self, other):
        "    x.__add__(y) <==> x+y"
        other = Quaternion(other)
        return Quaternion(self.r + other.r,
                          self.i + other.i,
                          self.j + other.j,
                          self.k + other.k)

    def __mul__(self, other):
        "    x.__mul__(y) <==> x*y"
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
        "    x.__abs__() <==> abs(x)"
        return math.sqrt(self.r*self.r +
                         self.i*self.i +
                         self.j*self.j +
                         self.k*self.k)

    def __radd__(self, other):
        "    x.__radd__(y) <==> y+x"
        return self + other

    def __div__(self, other):
        "    x.__div__(y) <==> x/y"
        other = Quaternion(other)
        return self * other.__inv__()
    def __rdiv__(self, other):
        "    x.__rdiv__(y) <==> y/x"
        return Quaternion(other) * self.conjugate() / (abs(self) ** 2)

    def __sub__(self, other):
        "    x.__sub__(y) <==> x-y"
        return self + (-other)

    def __rsub__(self, other):
        "    x.__rsub__(y) <==> y-x"
        return other + (-self)
       
    def __inv__(self):
       
        return Quaternion(self.r/(self.r*self.r + self.i*self.i + self.j*self.j + self.k*self.k),-self.i/(self.r*self.r + self.i*self.i + self.j*self.j + self.k*self.k),-self.j/(self.r*self.r + self.i*self.i + self.j*self.j + self.k*self.k),-self.k/(self.r*self.r + self.i*self.i + self.j*self.j + self.k*self.k))


       
    def __eq__(self, other):
        "    x.__eq__(y) <==> x==y"
        other = Quaternion(other)
        return (self.r == other.r and self.i == other.i and
                self.j == other.j and self.k == other.k)
    def __ne__(self, other):
        "    x.__ne__(y) <==> x!=y"
        return not (self == other)

    def __str__(self):
        "    x.__str__() <==> str(x)"
        return "(%g,%g,%g)" % (self.i, self.j, self.k)


    def __complex__(self):

        return complex(self.r, self.i)

    def rot(self):
     #Um método foi adcionado, para auxiliar na hora de guardar os dados da nova rotação"
        return (self.i,self.j,self.k)

   


class RotateCube(Quaternion):
	def __init__(self,a,vx,vy,vz):
		self.a = a
		self.vx = vx
		self.vy = vy
		self.vz = vz
		self.v = Quaternion(0,vx,vy,vz)
		self.a = math.radians(self.a)
		self.n = math.sin(self.a/2)/abs(self.v)
		self.r = Quaternion(math.cos(self.a/2),self.n*vx,self.n*vy,self.n*vz)
	def Rot(self):
        #Aqui defini duas variavei globais, afim de muda-las e permanecer com a mudanca"
		global cont
		global coord
		# se o contador for igual a 0, significa que ainda não houve rotação, entao usamos o valor inicial dado das coordenadas
		if  cont == 0:
			 coord = [(1, 1, 1), (1, 1,-1), (1, -1, 1), (-1, 1, 1),
(1, -1, -1), (-1, 1, -1), (-1, -1, 1),(-1, -1, -1)]
        #passando o ângulo a para radianos
		self.a = math.radians(self.a)
		print('As coordenadas do cubo rotacionado são:')

        #Para cada ponto  das coordenadas do cubo, calculamos o seu novo ponto, chamado de self.plinha
		for i in range(len(coord)):
			p = Quaternion(0,coord[i][0],coord[i][1],coord[i][2])
			self.plinha = self.r * p * self.r.__inv__()
			self.plinha = Quaternion(self.plinha)
			coord[i] = self.plinha.rot()
			print(self.plinha)
		cont += 1
		return 
b = 0
cont = 0
# Usamos um while para possibilitar que o usuario rotacione o cubo varias vezes
while b != 2:
	print("Digite o angulo de rotação:")
	a = int(input())
	print('Digite a coordenada x do eixo de rotação')
	vx = int(input())
	print('Digite a coordenada y do eixo de rotação')
	vy = int(input())
	print('Digite a coordenada z do eixo de rotação')
	vz = int(input())
	z = RotateCube(a,vx,vy,vz)
	z.Rot()
	print("Digite 1 para continuar ou 2 para sair")
	b = int(input())
