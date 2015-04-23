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
        tiemporeserva = [datetime(2015, 4, 22, 5, 50), datetime(2015, 4, 22, 6, 5)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(2.00).quantize(Decimal('1.00')))
    
    def testmaxReservaPosible(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(2015, 4, 22, 5, 50), datetime(2015, 4, 29, 5, 50)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(384).quantize(Decimal('1.00')))
    
    def testmaxfechaPosible(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(MAXYEAR, 12, 24, 5, 50), datetime(MAXYEAR, 12, 31, 5, 49)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(384).quantize(Decimal('1.00')))
    
    def testminfechaPosible(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(MINYEAR, 1, 1, 5, 50), datetime(MINYEAR, 1, 8, 5, 49)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(384).quantize(Decimal('1.00')))
    
    def testReservaMenor15(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(MINYEAR, 4, 22, 5, 50), datetime(MINYEAR, 4, 22, 6, 4)]
        with self.assertRaises(Exception) as context:
            calcularPrecio.calcularPrecio(tarifa, tiemporeserva)

        self.assertTrue("La reserva debe ser como minimo de quince (15) minutos" in context.exception)

    def testReservaMayor7(self):
        tarifa = calcularPrecio.Tarifa(2, 3) 
        tiemporeserva = [datetime(2015, 2, 20, 15, 50), datetime(2015, 2, 27, 15, 51)]
        with self.assertRaises(Exception) as context:
            calcularPrecio.calcularPrecio(tarifa, tiemporeserva)

        self.assertTrue("La reserva no debe ser mayor a siete (7) dias." in context.exception)

    def testMaxTarifaMinReserva(self):
        tarifa = calcularPrecio.Tarifa(2**28, 3**27) 
        tiemporeserva = [datetime(2004, 4, 22, 5, 50), datetime(2004, 4, 22, 6, 5)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal(2**28).quantize(Decimal('1.00')))

    def testMaxTarifaMaxReserva(self):
        tarifa = calcularPrecio.Tarifa(2**28, 3**27) 
        tiemporeserva = [datetime(2004, 4, 5, 5, 50), datetime(2004, 4, 12, 5, 50)]
        self.assertEquals(calcularPrecio.calcularPrecio(tarifa, tiemporeserva), Decimal((2**28)*24*5+(3**27*24*2)).quantize(Decimal('1.00')))

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()