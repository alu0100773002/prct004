#!/usr/bin/python
#!encoding: UTF-8
from math import *

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))

if (a == 0):
  x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
  x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
  print 'Las ecuaciones de la ecuación son: x1=%4.3f y x2=%4.3f' % (x1,x2)
else:
  if b != 0:
    print 'La solución de la ecuación es: x=%4.3f' % x
  else:
    if c != 0:
      print 'La ecuación no tiene solución'
    else:
      print 'La ecuación tiene infinitas soluciones'