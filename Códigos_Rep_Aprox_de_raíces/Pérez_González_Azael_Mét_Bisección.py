import sympy as sp               # Azael Pérez González
import numpy as np               # Agregado para el manejo de arreglos en la gráfica.
import matplotlib.pyplot as plt  # Agregado para generar las gráficas.

def graficar_resultados(f, x_0_ini, x_1_ini, iteraciones, errores):
    # Crea una figura con dos subgráficos (1 fila, 2 columnas).
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Gráfica de la función.
    x_vals = np.linspace(x_0_ini - 1, x_1_ini + 1, 400)
    y_vals = [f(val) for val in x_vals]
    
    ax1.plot(x_vals, y_vals, label='f(x)', color='blue')
    ax1.axhline(0, color='black', linewidth=1) 
    ax1.axvline(x_0_ini, color='red', linestyle='--', label=f'x_0 inicial ({x_0_ini})')
    ax1.axvline(x_1_ini, color='green', linestyle='--', label=f'x_1 inicial ({x_1_ini})')
    ax1.set_title("Gráfica de la Función")
    ax1.set_xlabel("x")
    ax1.set_ylabel("f(x)")
    ax1.legend()
    ax1.grid(True)

    # Se omite la primera iteración ya que no hay error calculado aún.
    iters_validas = iteraciones[1:]
    errores_validos = errores[1:]

    # Gráfica del error.
    ax2.plot(iters_validas, errores_validos, marker='o', color='orange', linestyle='-')
    ax2.set_title("Evolución del Error Absoluto")
    ax2.set_xlabel("Iteración")
    ax2.set_ylabel("Error Absoluto")
    ax2.grid(True)

    # Presentar las gráficas.
    plt.tight_layout()
    plt.show()
# ====================================
def biseccion():
    x = sp.Symbol('x')
    
    # Solicitar y evaluar la función ingresada.
    f_str = input("Ingresa la función f(x): ")
    f_expr = sp.sympify(f_str)
    f = sp.lambdify(x, f_expr, 'math')

    # Límites iniciales x_0 y x_1.
    x_0 = float(input("Ingresa el límite inferior (x_0): "))
    x_1 = float(input("Ingresa el límite superior (x_1): "))
    
    # Se solicita el error absoluto.
    tol = float(input("Ingresa el error absoluto esperado: "))

    # Guardado de los límites iniciales para la gráfica.
    x_0_ini = x_0
    x_1_ini = x_1

    # Verificación del teorema de Bolzano (cambio de signo).
    if f(x_0) * f(x_1) >= 0:
        print("Error: f(x_0) y f(x_1) deben tener signos opuestos para garantizar una raíz.")
        return

    x_i_plus_1_old = 0
    
    # Inicializa en infinito para garantizar la entrada al ciclo.
    error = float('inf') 
    iteracion = 1

    # Almacenamiento de los datos a graficar.
    lista_iteraciones = []
    lista_errores = []

    # Encabezado de la tabla de iteraciones.
    print(f"\n{'Iter':<5} | {'x_0':<10} | {'x_1':<10} | {'x_i+1':<10} | {'Error Abs':<10}")
    print("-" * 55)

    # Ciclo principal del método de bisección.
    while True:
        # Cálculo del punto medio.
        x_i_plus_1 = (x_0 + x_1) / 2.0
        
        # Cálculo del error absoluto directo a partir de la segunda iteración.
        if iteracion > 1:
            error = abs(x_i_plus_1 - x_i_plus_1_old)

        if iteracion == 1:
            print(f"{iteracion:<5} | {x_0:<10.5f} | {x_1:<10.5f} | {x_i_plus_1:<10.5f} | {'-':<10}")
            # Guardado de los datos de la iteración actual.
            lista_errores.append(0) 
        else:
            print(f"{iteracion:<5} | {x_0:<10.5f} | {x_1:<10.5f} | {x_i_plus_1:<10.5f} | {error:<10.5f}")
            # Guardado de los datos de la iteración actual.
            lista_errores.append(error) 

        lista_iteraciones.append(iteracion) 

        # Condición de parada por tolerancia.
        if error < tol and iteracion > 1:
            break

        # Actualización de los intervalos según el cambio de signo.
        if f(x_0) * f(x_i_plus_1) < 0:
            x_1 = x_i_plus_1
        elif f(x_0) * f(x_i_plus_1) > 0:
            x_0 = x_i_plus_1
        else:
            break 

        # Actualización de la variable para la siguiente iteración.
        x_i_plus_1_old = x_i_plus_1
        iteracion += 1

    # Solo se imprime el resultado al terminar el cálculo.
    print(f"\nLa raíz aproximada es: {x_i_plus_1:.7f}")

    # Llama a la función para graficar al terminar el cálculo.
    graficar_resultados(f, x_0_ini, x_1_ini, lista_iteraciones, lista_errores)

if __name__ == "__main__":
    biseccion()