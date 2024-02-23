# Todas las pruebas unitarias importan la biblioteca unittest
import unittest
# Las pruebas importan el modulo que va a realizar todo el trabajo
from Logica import *

# Debe existir por lo menos una clase que contenga las pruyebas unitarias
# descediente de unittest.TestCase
class HipotecaInversa(unittest.TestCase):
        
    # Cada prueba unitaria es un metodo la clase
    def test1(self):
        # DATOS DE ENTRADA
        valor_inmueble = 200000000
        edad = 70
        estado_civil = "viudo"
        tasa_interes = 3.8
        # Se calcula el tiempo restante de la persona en meses, teniendo en cuenta que la esperanza de vida son 80 años
        tiempo_restante = (80 - edad) * 12
        cuota =  63333.33
        resultado = Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def test2(self):
        # DATOS DE ENTRADA
        valor_inmueble = 50000000
        edad = 62
        estado_civil = "soltero"
        tasa_interes = 3.5
        # Se calcula el tiempo restante de la persona en meses, teniendo en cuenta que la esperanza de vida son 80 años
        tiempo_restante = (80 - edad) * 12
        cuota =  8101.85
        resultado = Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
        # Prueba que dos variables sean iguales
        self.assertEqual( cuota, round(resultado,2)  )

    def testCeroHipoteca(self):
        # DATOS DE ENTRADA
        valor_inmueble = 0
        edad = 82
        tasa_interes = 1.2
        # Se calcula el tiempo restante de la persona en meses, teniendo en cuenta que la esperanza de vida son 80 años
        tiempo_restante = (80 - edad) * 12
        #verifica si una función genera una excepción
        self.assertRaises(Exception, Calcular_Cuota_Mensual, valor_inmueble, tasa_interes, tiempo_restante)

    def testEdadOutOfRange(self):
        # DATOS DE ENTRADA
        valor_inmueble = 1000000000
        edad = 57
        tasa_interes = 3.5
        # Se calcula el tiempo restante de la persona en meses, teniendo en cuenta que la esperanza de vida son 80 años
        tiempo_restante = (80 - edad) * 12
        #verifica si una función genera una excepción
        self.assertRaises(Exception, Calcular_Cuota_Mensual, valor_inmueble, tasa_interes, tiempo_restante)

    def testCeroTasa(self):
        # DATOS DE ENTRADA
        valor_inmueble = 90000000
        edad = 65
        estado_civil = "casado"
        tasa_interes = 0
        # Se calcula el tiempo restante de la persona en meses, teniendo en cuenta que la esperanza de vida son 80 años
        tiempo_restante = (80 - edad) * 12
        #verifica si una función genera una excepción
        self.assertRaises(Exception, Calcular_Cuota_Mensual, valor_inmueble, tasa_interes, tiempo_restante)

# Ejecuta todos los test        
if __name__ == '__main__':
    unittest.main()