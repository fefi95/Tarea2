'''
Created on 21/04/2015

@author: stefani
'''
import unittest
import calcularPrecio
from datetime import datetime
from decimal import Decimal
#Pruebas de la funcion calcularPrecio
class TestcalcularPrecio(unittest.TestCase):

    def testminTarifaDiaSemana(self):
        diasem = calcularPrecio.Tarifa(1, 2) 
        tiemporeserva = [datetime(2015, 4, 22, 5, 50), datetime(2015, 4, 22, 6, 50)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), Decimal(1.00).quantize(Decimal('1.00')))

    def testminReservaPosible(self):
        diasem = calcularPrecio.Tarifa(2, 2) 
        tiemporeserva = [datetime(2015, 4, 22, 5, 50), datetime(2015, 4, 22, 6, 06)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), Decimal(0.53).quantize(Decimal('1.00')))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()