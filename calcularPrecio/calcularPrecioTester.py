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
        
    def testMinTarifaFinDeSemana(self):
        tarifa = calcularPrecio.Tarifa(1, 0) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 27, 0, 4)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(73).quantize(Decimal('1.00')))

    def testMinTarifaDiaSemana(self):
        tarifa = calcularPrecio.Tarifa(0, 1) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 27, 0, 00)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(48).quantize(Decimal('1.00')))
        
    def testExceptionTarifaDiaSemana(self):
        tarifa = calcularPrecio.Tarifa(-0.01, 0) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 22, 1, 00)]
        self.assertRaises(Exception, calcularPrecio, tarifa, tiemporeserva)
        
    def testExceptionTarifaFinDeSemana(self):
        tarifa = calcularPrecio.Tarifa(0, -0.01) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 22, 1, 00)]
        self.assertRaises(Exception, calcularPrecio, tarifa, tiemporeserva)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()