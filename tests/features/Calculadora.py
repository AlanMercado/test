import math
class Calculadora():
    def __init__(self):
        self.resultado = 0

    def obtener_resultado(self):
        return self.resultado

    def suma(self,num1,num2):
        self.resultado = num1 + num2

    def resta(self, num1, num2):
        self.resultado = num1 - num2

    def multiplicacion(self, num1, num2):
        self.resultado = num1 * num2

    def divicion(self, num1, num2):
        self.resultado = num1 / num2

    def potencia(self, num1, num2):
    	self.resultado = pow(num1, num2)

    def raiz(self, num1):
    	self.resultado = math.sqrt(num1)

    def edad(self,num1):

		if type(num1) is str:
			self.resultado= "no valido"

		elif num1<0:

			self.resultado = "no existes"

		elif num1<13 and num1>=0:

			self.resultado = "eres nino"

		elif num1>=13 and num1<18:
			self.resultado = "eres adolecente"

		elif num1>=18 and num1<65:
			self.resultado = "eres adulto"

		elif num1>=65 and num1<120:
			self.resultado = "eres adulto mayor"

		else:
			self.resultado = "eres mumm-ra"

    def area(self,num1,num2,num3,num4):
		area=0
		if num1==1:
			self.resultado =self.cuadrado(num2)
		elif num1==2:
			self.resultado =self.rectangulo(num2,num3)
		elif num1==3:
			self.resultado =self.circulo(num2)

		else:
			self.resultado =self.trapecio(num2,num3,num4)

		return area

    def cuadrado(self,num1):

		return num1*num1

    def rectangulo(self,num1,num2):
		return num1*num2

    def circulo(self, radio):
		return 3.1416*(radio*radio)

    def trapecio(self,B,b,h):
		return ((B+b)/2)*h
