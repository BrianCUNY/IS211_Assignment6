#! /usr/bin/env python3

#IS211 Assignment 6 - conversions

from decimal import Decimal as deci

def convertCelsiusToKelvin(degrees):
#converts celsius to kelvin
	degrees = str(degrees)
	convert = (deci(degrees) + deci('273.15'))
	return (float(convert))

def convertCelsiusToFahrenheit(degrees):
#converts celsius to fahrenheit
	degrees = str(degrees)
	convert = (deci(degrees) / deci('5') * 9) + 32
	return (float(convert))

def convertFahrenheitToCelsius(degrees):
#converts fahrenheit to celsius
	degrees = str(degrees)
	convert = ((deci(degrees) - 32) * 5) / deci('9')
	return (float(convert))

def convertFahrenheitToKelvin(degrees):
#converts fahrenheit to kelvin
	degrees = str(degrees)
	convert = ((deci(degrees) + deci('459.67')) * 5 / deci('9'))
	return (float(convert))

def convertKelvinToCelsius(degrees):
#converts kelvin to celsius
	degrees = str(degrees)
	convert = (deci(degrees) - deci('273.15'))
	return (float(convert))

def convertKelvinToFahrenheit(degrees):
#converts kelvin to fahrenheit
	degrees = str(degrees)
	convert = (((deci(degrees) * 9) / deci('5')) - deci('459.67'))
	return (float(convert))
