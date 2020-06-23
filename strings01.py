#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sample of string commands and methods in Python3
@author: alphonse
"""
print("Hello, World!")
string1 = "The Earth is round."
string2 = "Sun rises in the east."
string3 = string2[0:4]
print(string3)
print(string3 * 5)
print(string2.split(" "))
print(string2.count("t"))
print(string1.replace("Earth", "Ball"))
print(string2.find("east"))
string4 = str(45); print(string4)
print("earth" == "Earth")
print("round" is "round")
print("Sun" != "Son")

print('Testing a String')
print('-' * 20)
print('string1', string1) 
print("string1.startswith('t')", string1.startswith('t')) 
print("string1.startswith('T')", string1.startswith('T')) 
print("string1.endswith('d')", string1.endswith('d')) 
print('string2', string2)
print('string2.istitle()', string2.istitle())
print('string2[0].isupper()', string2[0].isupper()) 
print('string2[4:].islower()', string2[4:].islower()) 
print('string2.isalpha()', string2.isalpha())
print('string2[0:3].isalpha()', string2[0:3].isalpha())

print('String conversions')
print('-' * 20)
print('string1.upper()', string1.upper()) 
print('string2.lower()', string2.lower()) 
print('string1.title()', string1.title()) 
print('string2.swapcase()', string2.swapcase())