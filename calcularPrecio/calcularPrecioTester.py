'''
Created on 21/04/2015

@author: stefani
'''
import unittest
import calcularPrecio
from datetime import datetime, MINYEAR, MAXYEAR
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
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), Decimal(2.00).quantize(Decimal('1.00')))
    
    def testmaxReservaPosible(self):
        diasem = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(2015, 4, 22, 5, 50), datetime(2015, 4, 29, 5, 49)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), Decimal(384).quantize(Decimal('1.00')))
    
    def testmaxfechaPosible(self):
        diasem = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(MAXYEAR, 4, 22, 5, 50), datetime(MAXYEAR, 4, 29, 5, 49)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), Decimal(384).quantize(Decimal('1.00')))
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()