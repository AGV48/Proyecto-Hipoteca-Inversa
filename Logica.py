# Calcula el valor de las cuotas mensuales que el banco pagaría por una hipoteca inversa de una vivienda
#valor: valor de la propiedad
#tasa: tasa de intereses mensual, expresado como porcentaje (multiplicada por 100)
#tiempo_restante: tiempo de vida estimado de la persona


def Calcular_Cuota_Mensual(valor, interes, tiempo_restante):
    # Divide el porcentaje de la tasa por 100 para que quede en decimales
    porcentaje_tasa = interes / 100

    # Verifica que el valor de la propiedad no sea igual a 0
    if valor == 0:
        raise Exception("ERROR: no se puede realizar una hipoteca inversa sin una vivienda propia")
    # Verifica que la edad del usuario no esté por debajo del limite
    if tiempo_restante > 216:
        raise Exception("ERROR: el usuario no cumple con la edad minima (62 años) para realizar el procedimiento")
    if porcentaje_tasa == 0:
        raise Exception("ERROR: la tasa de la hipoteca inversa no puede ser cero")

    
    # Calcula el valor de la cuota mensual
    cuota_mensual = (valor * porcentaje_tasa) / tiempo_restante
    return cuota_mensual
