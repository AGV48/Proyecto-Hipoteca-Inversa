# Se importa el modulo donde se realizarán los procesos
from Logica import *

# Se le da una bienvenida al usuario y se le muestra un menú con las opciones
def Bienvenida():
    print("-------------------------------------------")
    print("    BIENVENIDO A EL BANCO MAS LADRÓN   ")
    print("¿Qué deseas hacer?")
    print(" 1. Obtener una hipoteca inversa \n 0. Salir")
    opcion = int(input("Elija una opción: "))
    print("--------------------------------------")
    # Se llama a la siguiente función y se le pasa como parametro la opción que el usuario eligió
    return desiciones(opcion)

def desiciones(opcion):
    # Se hace uso del metodo try para lanzar una excepción si algo falla
    try:
        # Se usa el ciclo while para verificar cual opción escogio el usuario
        while opcion != 0:
            # Se verifica si la opción escogida por el usuario no está definida
            if opcion < 0 or opcion > 1:
                print("------------------------------------------------------------------")
                print("                  EL BANCO MAS LADRÓN            ")
                print("La opción ingresada no es correcta, intente de nuevo")
                print("-------------------------------------------------------------------")
                # Se llama nuevamente al metodo de Bienvenida para reiniciar el proceso
                Bienvenida()
            # Se verifica si el usuario quiere calcular una hipoteca inversa
            if opcion == 1:
                print("---------------------------------------------------------------------")
                print("                     EL BANCO MAS LADRÓN                 ")
                print("DATOS PERSONALES")
                # Se obtienen los datos de entrada
                valor_inmueble = float(input("Por favor ingrese el valor de la vivienda: "))
                edad = int(input("Por favor ingrese su edad actual: "))
                estado_civil = input("Por favor ingrese su estado civil: ")
                tasa_interes = float(input("Ingrese la tasa de interes: "))
                print("-------------------------------------------------------------------------")
                # Se calcula el tiempo restante de la persona en meses, teniendo en cuenta que la esperanza de vida son 80 años
                tiempo_restante = (80 - edad) * 12

                # Se calcula el valor de cada cuota de la hipoteca inversa
                resultado = Calcular_Cuota_Mensual(valor_inmueble, tasa_interes, tiempo_restante)
                # Se muestra el resultado
                print(f"El valor de cada cuota de la hipoteca inversa es de: {round(resultado,2)}")
                return
        # Se le da al usuario un mensaje de despedida al usuario cuando finaliza todo el proceso
        print("------------------------------------------------------------------")
        print("                  EL BANCO MAS LADRÓN            ")
        print("Gracias por visitarnos, vuelva pronto")
        print("-------------------------------------------------------------------")
    # Se lanza un mensaje de error cuando algo falla
    except:
        print("------------------------------------------------------------------")
        print("                  EL BANCO MAS LADRÓN            ")
        print("Hubo un error, intentalo nuevamente")
        print("-------------------------------------------------------------------")
        Bienvenida()

# Se llama la funcion para dar inicio al programa
Bienvenida()