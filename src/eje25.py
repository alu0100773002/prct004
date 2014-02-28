#!/usr/bin/python
#!encoding: UTF-8
from math import *

a = float(raw_input('Valor de a: '))
b = float(raw_input('Valor de b: '))
c = float(raw_input('Valor de c: '))

if a == 0:
  if b == 0:
    if c == 0:
      print 'La ecuación no tiene solucion'
    else:
       print 'La ecuación tiene infinitas soluciones'
  else:
    x = -c / b
    print 'La solucion de la ecuacion es: x=4%.3f' % x
else:
  x1 = (-b + sqrt(b**2 - 4*a*c)) / (2 * a)
  x2 = (-b - sqrt(b**2 - 4*a*c)) / (2 * a)
  print 'Las ecuaciones de la ecuación son: x1=%4.3f y x2=%4.3f' % (x1,x2)
  
  #La diferencia entre este y el 24 es que aquí preguntamos por los iguales a 0 y en el 24 por los distintos