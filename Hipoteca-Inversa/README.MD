# Proyecto Hipoteca Inversa en Python con practicas de Clean Code


## ¿Quién hizo esto?

Alejandro Gutierrez Vallejo
Andrea Márquez Sánchez

## ¿Qué es y para qué es?

Este proyecto fue creado con la intención de calcular una Hipoteca Inversa

## ¿Cómo lo hago funcionar?

- Prerrequisitos: Tener un editor de texto(Ejemplo: Visual Studio Code), Tener instalada la ultima version de python


## Estructura sugerida

- Carpeta src: Codigo fuente de la logica de la aplicación. Tiene subcarpetas por cada capa de la aplicacion
- Carpeta tests: Pruebas Unitarias 

Recuerde que cada carpeta de código fuente debe contener un archivo __init.py que permite que python
reconozca la carpeta como un Módulo y pueda hacer import

## Uso

Para ejecutar las pruebas unitarias, desde la carpeta src, use el comando

`
  Hipoteca-Inversa\src> python -m unittest discover ..\tests -p '*test*.py'
`
Para poder ejecutarlas desde la carpeta raiz, debe indicar la ruta de busqueda donde se encuentran los
módulos, incluyendo las siguientes lineas al inicio del módulo de pruebas

`
  import sys
  sys.path.append("src")
`