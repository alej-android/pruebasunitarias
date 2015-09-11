import unittest

class TestCalculadora(unittest.TestCase):

	def setUp(self):
		self.cal = Calculadora() 

	def test_sumar_de_2_mas_2(self):
		calc = Calculadora()
		resultado = calc.suma(2,2)
		self.assertEqual(4, resultado)

	def test_sumar_de_3_mas_3(self):
		calc = Calculadora()
		resultado = calc.suma(3,3)
		self.assertEqual(6, resultado)

	def test_sumar_de_5_mas_5(self):
		calc = Calculadora()
		resultado = calc.suma(5,5)
		self.assertEqual(10, resultado)

	
	def test_resta_de_8_menos_4(self):
		calc = Calculadora()
		resultado = calc.resta(8,4)
		self.assertEqual(4, resultado)



class Calculadora():
	def suma(self, num1, num2):
		return num1+num2

	def resta(self, num1, num2):
		return num1-num2

if __name__=="__main__":
	unittest.main()
