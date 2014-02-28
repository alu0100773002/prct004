#!/usr/bin/python
#!encoding: UTF-8

numero = int( raw_input('Introduzca un número: '))

for potencia in [2,3,4,5]:
  print '%d elevado a %d es %d' % (numero, potencia, numero**potencia)
  
#Eleva el número que metemos por teclado a 2, 3, 4 y 5.