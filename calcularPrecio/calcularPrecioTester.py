'''
Created on 22/04/2015

@author: edwin
'''
import unittest
import calcularPrecio
from datetime import datetime

#Pruebas de la funcion calcularPrecio
class Test(unittest.TestCase):

    def testMinTarifaSemanaCompleta(self):
        diasem = calcularPrecio.Tarifa(1, 0) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 22, 1, 00)]
        self.assertRaises(calcularPrecio.calcularPrecio(diasem, tiemporeserva), 1.00)
        
    def testMinTarifaFinDeSemana(self):
        diasem = calcularPrecio.Tarifa(1, 0) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 27, 0, 00)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), 72.00)

    def testMinTarifaDiaSemana(self):
        diasem = calcularPrecio.Tarifa(0, 1) 
        tiemporeserva = [datetime(2015, 4, 22, 0, 00), datetime(2015, 4, 27, 0, 00)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), 48.00)
        

        






if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()