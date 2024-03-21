# EXCEPCIONES
class Hipoteca_Exception(Exception):
    """ 
    Custom exception for property value above maximum, below minimum and zero

    Excepción personalizada para el valor de la propiedad por encima del máximo, 
    por debajo del mínimo y cero
    """
class Edad_Minima_Exception(Exception):
    """ 
    Custom exception for age below minimum

    Excepción personalizada para la edad por debajo del mínimo
    """
class Tasa_Exception(Exception):
    """ 
    Custom exception for interest rate above maximum, below minimum and zero

    Excepción personalizada para tasa de interés por encima del máximo, 
    por debajo del mínimo y cero
    """
class Negative_Exception(Exception):
    """ 
    Custom exception for negative values

    Excepción personalizada para valores negativos
    """

# CONSTANTES
# Maximun age allowed
ESPERANZA_VIDA_HOMBRES = 84
ESPERANZA_VIDA_MUJERES = 86

# Minimun age allowed
EDAD_MINIMA = 62

# Minimum age allowed in months
MAXIMO_TIEMPO_RESTANTE = 252

# Months of the year
MESES_AÑO = 12

# Minimum property value
VALOR_MINIMO_INMUEBLE = 10000000

# Maximun and minimun intrest rate allowed
INTERES_MINIMO = 6
INTERES_MAXIMO = 43

# Calcula el valor de las cuotas mensuales que el banco pagaría por una hipoteca inversa de una vivienda
#valor: valor de la propiedad
#interes: tasa de intereses mensual, expresado como porcentaje (multiplicada por 100)
#tiempo_restante: tiempo de vida estimado de la persona

class Calcular_Hipoteca_Inversa:
    def Calcular_Cuota_Mensual(valor_inmueble: float, interes: float, tiempo_restante: int):
        """
            Calculate the monthly payment for a reverse mortgage

            Calcula la cuota a pagar por una hipoteca inversa

            Parameters
            ----------

            valor_inmueble : float
                property value / valor del inmueble

            interes : float
                must not be zero or less than
                INTERES_MINIMO / Tasa minima de interes, valor positivo mayor que INTERES_MINIMO
                and must not be zero or greater than
                INTERES_MAXIMO / Tasa minima de interes, valor positivo mayor que INTERES_MAXIMO
            
            tiempo_restante : int
                Remaining life of the person in months / Tiempo de vida restante de la persona en meses

            Returns
            -------
            payment : float
                Monthly payment calculated. Not rounded / Pago mensual calculado. El resultado no esta redondeado
            
            Raises
            ------
            HipotecaException
                When the property value is zero or less than the value defined in VALOR_MINIMO_INMUEBLE

            EdadMinimaException
                When the person's age is below the value defined in EDAD_MINIMA

            TasaException
                When the interest rate is higher or lower than the value defined in INTERES_MINIMO, INTERES_MAXIMO

            NegativeException
                When any value is zero 
        """
        # Divide el porcentaje de la tasa por 100 para que quede en decimales
        porcentaje_tasa = interes / 100
        # Verifica que el valor de la propiedad no sea menor al minimo
        if valor_inmueble < VALOR_MINIMO_INMUEBLE:
            raise Hipoteca_Exception("ERROR: no se puede realizar una hipoteca inversa con una propiedad menor a 10.000.000")
        # Verifica que la edad del usuario no esté por debajo del limite
        if tiempo_restante > MAXIMO_TIEMPO_RESTANTE:
            raise Edad_Minima_Exception("ERROR: el usuario no cumple con la edad minima (62 años) para realizar el procedimiento")
        # Verifica que ningun valor sea negativo
        if valor_inmueble < 0 or interes < 0 or tiempo_restante < 0:
            raise Negative_Exception("ERROR: no pueden haber valores negativos")
        # Verifica que la tasa de interes no sea 0, ó que no este por debajo del valor minimo
        if interes < INTERES_MINIMO:
            raise Tasa_Exception("ERROR: la tasa de interes de la hipoteca inversa no puede ser cero, ni tampoco puede ser menor al 6%")
        # Verifica que la tasa de interes no supere el maximo
        if interes > INTERES_MAXIMO:
            raise Tasa_Exception("ERROR, la tasa de una hipoteca inversa no puede ser mayor al 43%")
        
        # Calcula el valor de la cuota mensual
        cuota_mensual = (valor_inmueble * porcentaje_tasa) / tiempo_restante
        return cuota_mensual

    def Logica_test(valor_inmueble: float, edad: int, estado_civil: str, edad_conyugue: int, sexo_conyugue: str, tasa_interes: float):
        # Se calcula el tiempo restante de la persona en meses, teniendo en cuenta que la esperanza de vida de los hombres es de 84 años y de las mujeres es de 86 años
        if sexo_conyugue == "hombre" or sexo_conyugue == "masculino" or estado_civil == "viuda" or estado_civil == "soltera" or estado_civil == "divorciada":      
            tiempo_restante = (ESPERANZA_VIDA_MUJERES - edad) * MESES_AÑO
            tiempo_restante_conyugue = (ESPERANZA_VIDA_HOMBRES - edad_conyugue) * MESES_AÑO
        else:
            tiempo_restante = (ESPERANZA_VIDA_HOMBRES - edad) * MESES_AÑO
            tiempo_restante_conyugue = (ESPERANZA_VIDA_MUJERES - edad_conyugue) * MESES_AÑO
        # Se pregunta si la persona no tiene conyugue, para así calcular la hipoteca inversa solo con él/ella
        if estado_civil == "viudo" or estado_civil == "soltero" or estado_civil == "divorciado" or estado_civil == "viuda" or estado_civil == "soltera" or estado_civil == "divorciada":
            return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
        # Se pregunta si la persona tiene conyugue, para así calcular cual de los dos vivirá más
        elif estado_civil == "casado" or estado_civil == "casada":
            if tiempo_restante > tiempo_restante_conyugue and edad >= EDAD_MINIMA:
                return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
            else:
                if tiempo_restante > tiempo_restante_conyugue and edad >= EDAD_MINIMA:
                    return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
                else:
                    if tiempo_restante > tiempo_restante_conyugue and edad_conyugue >= EDAD_MINIMA:
                        return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante_conyugue)
                    else:
                        return Calcular_Hipoteca_Inversa.Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
