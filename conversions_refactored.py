#! /usr/bin/env python3

#IS211 Assignment 6 - refactored conversions

import unittest
from decimal import Decimal as deci

class ConversionNotPossible(Exception):
#class for conversion, not possible
	pass

KCDIF = deci('273.15')
KFDIF = deci('459.67')
NDIVF = deci('9') / 5
FDIVN = deci('5') / 9

F1 = {'cel': {'kel': (KCDIF, 1, 0), 'fah': (0, NDIVF, 32)},
	'kel': {'cel': (-KCDIF, 1, 0), 'fah': (0, NDIVF, -KFDIF)},
	'fah': {'cel': (-32, FDIVN, 0), 'kel': (KDIF, FDIVN, 0)},
	'mil': {'yar': (0, deci(1760), 0), 'met': (0, deci(1609.34), 0)},
	'yar': {'mil': (0, deci(.00056818), 0), 'met': (0, deci(.9144), 0)},
	'met': {'mil': (0, deci(.00062137), 0), 'yar': (0, deci(1.09361), 0)}
	}

def convert(fromUnit, toUnit, value):
#converts a given value to a different unit types value
	fU = fromUnit[:3].lower()
	tU = toUnit[:3].lower()
	value = deci(value)
	if fU == tU:
		return float(value)
	elif tU in F1[fU]:
		conversion = ((value + F1[fU][tU][0]) * (F1[fU][tU][1]) + (F1[fU][tU][2]))
		return round(float(conversion), 3)
	else:
		raise ConversionNotPossible

class ConversionTests(unittest.TestCase):
#tests the conversions for this module
	testvalues = [('Celsius', 'Kelvin', 100, 373.15),
			('Celsius', 'Fahrenheit', 300, 572.0),
			('Kelvin', 'Celsius', 273.15, 0),
			('Kelvin', 'Fahrenheit', 573.15, 572.0),
			('Fahrenheit', 'Celsius', 32, 0),
			('Fahrenheit', 'Kelvin', 32, 273.15),
			('Miles', 'Yards', 1, 1760),
			('Miles', 'Meters', .5, 804.67),
			('Yards', 'Miles', 5, 804.67),
			('Yards', 'Meters', 10, 9.144),
			('Meters', 'Yards', 5, 5.468),
			('Meters', 'Miles', 1000, .621)]
			
	def testConversions(self):
	#tests if the conversions run properly
		for i in self.testvalues:
			self.assertEqual(convert(i,[0], i[1], i[2], i[3])

	def testSingleUnit(self):
	#tests all conversions of a single unit type
		for c in F1:
			self.assertEqual(convert(c, c, 1.0), 1.0)

	def testIncompatibleUnits(self):
	#tests if exception is raised or not
		self.assertRaises(ConversionNotPossible, convert, 'Miles', 'Kelvin', 10)


if __name == '__main__':
	unittest.main()
