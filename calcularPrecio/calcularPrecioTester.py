'''
Created on 22/04/2015

@author: edwin
'''
import unittest
import calcularPrecio
from datetime import datetime

#Pruebas de la funcion calcularPrecio
class Test(unittest.TestCase):

    def testminTarifaDiaSemana(self):
        diasem = calcularPrecio.Tarifa(1, 1) 
        tiemporeserva = [datetime(2015, 4, 22, 5, 50), datetime(2015, 4, 22, 6, 50)]
        self.assertEquals(calcularPrecio.calcularPrecio(diasem, tiemporeserva), 1.00)



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()