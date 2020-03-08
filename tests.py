#! /usr/bin/env python3

#IS211 Assignment 6 - tests

import conversions
import unittest

class KnownValues(unittest.TestCase):
#tests the functions in the conversions module
	knownvals = ((270.00, 518.00, 543.15),
				(200.00, 392.00, 473.15),
				(120.00, 248.00, 393.15),
				(0.00, 32.00, 273.15),
				(-273.15, -459.67, 0.00))

	def testCelsiusToKelvin(self):
	#tests convertCelsiusToKelvin from conversions.py
		for val in self.knownvals:
			c = val[0]
			k = val[2]
			expect = conversions.convertCelsiusToKelvin(c)
			self.assertEqual(expect, k, message = ('{} degrees K ' 'is not equal to {}' ' degrees K').format(c,k))
	
	def testCelsiusToFahrenheit(self):
	#tests convertCelsiusToFahrenheit from conversions.py
		for val in self.knownvals:
			c = val[0]
			f = val[1]
			expect = conversions.convertCelsiusToFahrenheit(c)
			self.assertEqual(expect, f, message = ('{} degrees F ' 'is not equal to {}' ' degrees F').format(c,f))

	def testFahrenheitToCelsius(self):
	#tests convertFahrenheitToCelsius from conversions.py
		for val in self.knownvals:
			f = val[1]
			c = val[0]
			expect = conversions.convertFahrenheitToCelsius(f)
			self.assertEqual(expect, c, message = ('{} degrees C ' 'is not equal to {}' ' degrees C').format(f, c))
		
	def testFahrenheitToKelvin(self):
	#tests convertFahrenheitToKelvin from conversions.py
		for val in self.knownvals:
			f = val[1]
			k = val[2]
			expect = conversions.convertFahrenheitToKelvin(f)
			self.assertEqual(expect, k, message = ('{} degrees K ' 'is not equal to {}' ' degrees K').format(f, k))

	def testKelvinToCelsius(self):
	#tests convertKelvinToCelsius from conversions.py
		for val in self.knownvals:
			k = val[2]
			c = val[0]
			expect = conversions.convertKelvinToCelsius(k)
			self.assertEqual(expect, c, message = ('{} degrees C ' 'is not equal to {}' ' degrees C').format(k, c))
		
	def testKelvinToFahrenheit(self):
	#tests convertKelvinToFahrenheit from conversions.py
		for val in self.knownvals:
			k = val[2]
			f = val[1]
			expect = conversions.convertKelvinTofahrenheit(k)
			self.assertEqual(expect, f, message = ('{} degrees F ' 'is not equal to {}' ' degrees F').format(k, f))
		

if __name__ == '__main__':
	unittest.main()
