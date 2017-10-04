class area(object):

	def area(self,num1,num2,num3,num4):
		area=0
		if num1==1:
			area=self.cuadrado(num2)
		elif num1==2:
			area=self.rectangulo(num2,num3)
		elif num1==3:
			area=self.circulo(num2)

		else:
			area=self.trapecio(num2,num3,num4)

		return area

	def cuadrado(self,num1):

		return num1*num1

	def rectangulo(self,num1,num2):
		return num1*num2

	def circulo(self, radio):
		return 3.1416*(radio*radio)

	def trapecio(self,B,b,h):
		return ((B+b)/2)*h

