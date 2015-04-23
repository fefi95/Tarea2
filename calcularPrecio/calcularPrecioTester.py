'''
Created on 22/04/2015

@author: edwin
'''
import unittest
import calcularPrecio
from datetime import datetime

#Pruebas de la funcion calcularPrecio
class Test(unittest.TestCase):
        
    def testMinTarifaFinDeSemana(self):
        diasem = calcularPrecio.Tarifa(1, 0) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 27, 0, 4)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), 73.00)

    def testMinTarifaDiaSemana(self):
        diasem = calcularPrecio.Tarifa(0, 1) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 27, 0, 00)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), 48.00)
        
    def testMaxTarifaDiaSemana(self):
        diasem = calcularPrecio.Tarifa(2**50, 0) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 22, 1, 00)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), 2**50)
        
    def testMaxTarifaFinDeSemana(self):
        diasem = calcularPrecio.Tarifa(0, 9223372036854775807) 
        tiemporeserva = [datetime(2015, 4, 25, 0, 00), datetime(2015, 4, 25, 1, 00)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), 9223372036854775807)
        
    def testExceptionTarifaDiaSemana(self):
        diasem = calcularPrecio.Tarifa(-1, -1) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 22, 1, 00)]
        with self.assertRaises(Exception) as context:
            calcularPrecio.calcularPrecio(diasem, tiemporeserva)

        self.assertTrue("No se admiten tarifas negativas." in context.exception)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()