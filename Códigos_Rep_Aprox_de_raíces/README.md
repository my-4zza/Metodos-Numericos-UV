# Códigos de Aproximación de Raíces

AUTOR: AZAEL PÉREZ GONZÁLEZ

Este directorio contiene las implementaciones en Python de cinco algoritmos clásicos para encontrar raíces de ecuaciones no lineales. Estos códigos son parte del reporte de prácticas de la experiencia educativa de Métodos Numéricos.

## Contenido del Directorio

Los archivos comprenden los 5 métodos abordados en el curso, tanto métodos cerrados como abiertos:

* **`Pérez_González_Azael_Mét_Bisección.py`**: Implementa el **Método de Bisección** (método cerrado). Divide repetidamente a la mitad un intervalo inicial, donde la función cambia de signo.
* **`Pérez_González_Azael_Mét_Falsa_Pos.py`**: Implementa el **Método de la Falsa Posición** (método cerrado). Utiliza una línea recta entre las evaluaciones de los límites para encontrar una intersección más rápida que la bisección.
* **`Pérez_González_Azael_Mét_New_Raph.py`**: Implementa el **Método de Newton-Raphson** (método abierto). Requiere un solo punto inicial y calcula la derivada de la función ingresada automáticamente utilizando cálculo simbólico.
* **`Pérez_González_Azael_Mét_Punto_Fijo.py`**: Implementa el **Método del Punto Fijo** (método abierto). Evalúa iterativamente un punto en una función despejada g(x) hasta converger.
* **`Pérez_González_Azael_Mét_Secante.py`**: Implementa el **Método de la Secante** (método abierto). Una alternativa a Newton-Raphson que utiliza dos puntos iniciales para aproximar la derivada, evitando su cálculo analítico.

## Características

Todos los programas de esta carpeta comparten la siguiente estructura de funcionamiento:
1.  **Entrada dinámica:** Solicitan al usuario la función matemática (en formato de texto), los valores iniciales y la tolerancia del error absoluto esperado.
2.  **Traza de ejecución:** Imprimen en la consola una tabla iterativa detallada con los valores calculados paso a paso y la evolución del error.
3.  **Análisis visual:** Al finalizar el cálculo, despliegan una ventana con dos gráficas (generadas con `matplotlib`):
    * El comportamiento de la función f(x) o g(x), mostrando visualmente los puntos iniciales y la raíz aproximada.
    * La curva de caída del error absoluto a lo largo de las iteraciones.

## Dependencias Necesarias

Para ejecutar cualquiera de estos códigos, el entorno de Python debe contar con las siguientes librerías:
* `sympy`
* `numpy`
* `matplotlib`
