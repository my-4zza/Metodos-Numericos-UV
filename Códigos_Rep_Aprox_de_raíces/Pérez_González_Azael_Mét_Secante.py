import sympy as sp               # Azael Pérez González
import numpy as np               # Agregado para el manejo de arreglos en la gráfica.
import matplotlib.pyplot as plt  # Agregado para generar las gráficas.

def graficar_resultados(f, x_0_ini, x_1_ini, x_fin, iteraciones, errores):
    # Crea una figura con dos subgráficos (1 fila, 2 columnas).
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Cálculo del margen y rango dinámico para asegurar que todos los puntos clave sean visibles.
    min_x = min(x_0_ini, x_1_ini, x_fin)
    max_x = max(x_0_ini, x_1_ini, x_fin)
    margen = abs(max_x - min_x) * 0.5 + 2 if max_x != min_x else 5
    
    # Rango de valores en x para graficar la función.
    x_vals = np.linspace(min_x - margen, max_x + margen, 400)
    y_vals = [f(val) for val in x_vals]
    
    # Gráfica de la función.
    ax1.plot(x_vals, y_vals, label='f(x)', color='blue')
    ax1.axhline(0, color='black', linewidth=1) 
    ax1.axvline(x_0_ini, color='red', linestyle='--', label=f'x_0 inic ({x_0_ini:.4f})')
    ax1.axvline(x_1_ini, color='purple', linestyle='--', label=f'x_1 inic ({x_1_ini:.4f})')
    ax1.axvline(x_fin, color='green', linestyle='--', label=f'Raíz aprox ({x_fin:.4f})')
    ax1.set_title("Gráfica de la Función")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")
    ax1.legend()
    ax1.grid(True)

    # Gráfica del error.
    ax2.plot(iteraciones, errores, marker='o', color='orange', linestyle='-')
    ax2.set_title("Evolución del Error Absoluto")
    ax2.set_xlabel("Iteración")
    ax2.set_ylabel("Error Absoluto")
    ax2.grid(True)

    # Presentar las gráficas.
    plt.tight_layout()
    plt.show()
#================================
def secante():
    x = sp.Symbol('x')
    
    # Solicitar y evaluar la función ingresada.
    f_str = input("Ingresa la función f(x): ")
    f_expr = sp.sympify(f_str)
    f = sp.lambdify(x, f_expr, 'math')

    # Se requieren dos puntos iniciales para el método de la secante.
    x_0 = float(input("Ingresa el primer punto inicial (x_0): "))
    x_1 = float(input("Ingresa el segundo punto inicial (x_1): "))
    
    # Se solicita el error absoluto esperado.
    tol = float(input("Ingresa el error absoluto esperado: "))

    # Guardado de los límites iniciales para la gráfica.
    x_0_ini = x_0
    x_1_ini = x_1

    # Inicializa en infinito para garantizar la entrada al ciclo.
    error = float('inf') 
    iteracion = 1

    # Almacenamiento de los datos a graficar.
    lista_iteraciones = []
    lista_errores = []

    # Encabezado de la tabla de iteraciones.
    print(f"\n{'Iter':<5} | {'x_0':<10} | {'x_1':<10} | {'x_i+1':<15} | {'Error Abs':<15}")
    print("-" * 60)

    # Ciclo principal del método de la secante.
    while error > tol:
        # Se separan los componentes de la fórmula para evitar errores y mayor claridad.
        numerador = f(x_1) * (x_0 - x_1)
        denominador = f(x_0) - f(x_1)
        
        # Prevención de división por cero si ambos puntos evaluados son iguales.
        if denominador == 0:
            print("División por cero. El método falla.")
            break
            
        # Fórmula iterativa del método de la secante.
        x_i_plus_1 = x_1 - (numerador / denominador)
        
        # Cálculo del error absoluto respecto a la iteración anterior.
        error = abs(x_i_plus_1 - x_1)
        
        # Impresión de los resultados de la iteración actual.
        print(f"{iteracion:<5} | {x_0:<10.5f} | {x_1:<10.5f} | {x_i_plus_1:<15.5f} | {error:<15.5f}")
        
        # Guardado de los datos de la iteración actual para las gráficas.
        lista_errores.append(error)
        lista_iteraciones.append(iteracion)
        
        # Actualización de las variables, desplazando los puntos para la siguiente iteración.
        x_0 = x_1
        x_1 = x_i_plus_1
        iteracion += 1

    # Solo se imprime el resultado al terminar el cálculo.
    print(f"\nLa raíz aproximada es: {x_1:.7f}")
    
    # Llama a la función para graficar al terminar el cálculo.
    graficar_resultados(f, x_0_ini, x_1_ini, x_1, lista_iteraciones, lista_errores)

if __name__ == "__main__":
    secante()