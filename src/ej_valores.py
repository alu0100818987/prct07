#! /usr/bin/python

import ej_PI3

valores = (1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7, 1e8)
#El maximo elemento de la t_upla 1e8, cuando es 1e9 ya falla.
#En notacion cientifica 100000000 = 1e8
for valor in range valores(valor):
  y = ej_PI3.h(int (valor))
  print y