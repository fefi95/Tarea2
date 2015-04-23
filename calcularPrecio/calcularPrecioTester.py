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

    def testminTarifatarifsemana(self):
        tarifa = calcularPrecio.Tarifa(1, 2) 
        tiemporeserva = [datetime(2015, 4, 22, 5, 50), datetime(2015, 4, 22, 6, 50)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(1.00).quantize(Decimal('1.00')))

    def testminReservaPosible(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(2015, 4, 22, 5, 50), datetime(2015, 4, 22, 6, 05)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(2.00).quantize(Decimal('1.00')))
    
    def testmaxReservaPosible(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(2015, 4, 22, 5, 50), datetime(2015, 4, 29, 5, 49)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(384).quantize(Decimal('1.00')))
    
    def testmaxfechaPosible(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(MAXYEAR, 4, 22, 5, 50), datetime(MAXYEAR, 4, 29, 5, 49)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(384).quantize(Decimal('1.00')))
    
    def testminfechaPosible(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(MINYEAR, 4, 22, 5, 50), datetime(MINYEAR, 4, 29, 5, 49)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(384).quantize(Decimal('1.00')))
    
    def testReservaMenor15(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(MINYEAR, 4, 22, 5, 50), datetime(MINYEAR, 4, 22, 6, 04)]
        with self.assertRaises(Exception) as context:
            calcularPrecio.calcularPrecio(tarifa, tiemporeserva)

        self.assertTrue("La reserva debe ser como minimo de quince (15) minutos" in context.exception)


    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()