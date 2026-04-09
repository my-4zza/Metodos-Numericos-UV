import sympy as sp               # Azael Pérez González
import numpy as np               # Agregado para el manejo de arreglos en la gráfica.
import matplotlib.pyplot as plt  # Agregado para generar las gráficas.

def graficar_resultados(f, x_ini, x_fin, iteraciones, errores):
    # Crea una figura con dos subgráficos (1 fila, 2 columnas).
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Cálculo del margen y rango de valores en x para graficar la función.
    margen = abs(x_fin - x_ini) + 2 if x_ini != x_fin else 5
    x_vals = np.linspace(min(x_ini, x_fin) - margen, max(x_ini, x_fin) + margen, 400)
    y_vals = [f(val) for val in x_vals]
    
    # Gráfica de la función.
    ax1.plot(x_vals, y_vals, label='f(x)', color='blue')
    ax1.axhline(0, color='black', linewidth=1) 
    ax1.axvline(x_ini, color='red', linestyle='--', label=f'x_0 inicial ({x_ini:.4f})')
    ax1.axvline(x_fin, color='green', linestyle='--', label=f'Raíz aprox ({x_fin:.4f})')
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
# =================================
def newton_raphson():
    x = sp.Symbol('x')
    
    # Solicitar y evaluar la función ingresada.
    f_str = input("Ingresa la función f(x): ")
    f_expr = sp.sympify(f_str)
    f = sp.lambdify(x, f_expr, 'math')

    # Cálculo de la derivada de manera simbólica usando sympy.
    df_expr = sp.diff(f_expr, x)
    df = sp.lambdify(x, df_expr, 'math')

    # Muestra la derivada calculada al usuario.
    print(f"Derivada calculada por el sistema: {df_expr}")

    # Solicitud del punto inicial y tolerancia.
    x_0 = float(input("Ingresa el punto inicial (x_0): "))
    tol = float(input("Ingresa el error absoluto esperado: "))
    
    # Guardado del punto inicial para la gráfica.
    x_0_ini = x_0 

    # Inicialización de variables para el control del ciclo.
    iteracion = 1
    error = float('inf')
    
    # Almacenamiento de los datos a graficar.
    lista_iteraciones = []
    lista_errores = []

    # Encabezado de la tabla de iteraciones.
    print(f"\n{'Iter':<5} | {'x_i+1':<10} | {'Error Abs':<10}")
    print("-" * 40)

    # Ciclo principal del método de Newton-Raphson.
    while True:
        # Evaluación de la derivada en el punto actual.
        df_val = df(x_0)

        # Prevención de división por cero si la derivada es nula (punto de inflexión o mínimo/máximo local).
        if df_val == 0:
            print(f"\n[!] Advertencia: La derivada en x = {x_0} es cero.")
            print("[!] Aplicando un pequeño desplazamiento (+0.001) para continuar...")
            x_0 += 0.001  
            df_val = df(x_0) 

        # Fórmula principal del método de Newton-Raphson.
        x_i_plus_1 = x_0 - (f(x_0) / df_val)

        # Cálculo del error absoluto entre la iteración actual y la anterior.
        error = abs(x_i_plus_1 - x_0)

        # Impresión de datos según sea la primera iteración o las subsecuentes.
        if iteracion == 1:
            print(f"{iteracion:<5} | {x_i_plus_1:<10.5f} | {'-':<10}")
            lista_errores.append(0) # Guardado de los datos de la iteración actual.
        else:
            print(f"{iteracion:<5} | {x_i_plus_1:<10.5f} | {error:<10.5f}")
            lista_errores.append(error) # Guardado de los datos de la iteración actual.
            
        lista_iteraciones.append(iteracion) 

        # Condición de parada por tolerancia.
        if error < tol:
            break

        # Actualización de la variable para la siguiente iteración.
        x_0 = x_i_plus_1
        iteracion += 1

    # Solo se imprime el resultado al terminar el cálculo.
    print(f"\nLa raíz aproximada es: {x_i_plus_1:.7f}")
    
    # Llama a la función para graficar al terminar el cálculo.
    graficar_resultados(f, x_0_ini, x_i_plus_1, lista_iteraciones, lista_errores)

if __name__ == "__main__":
    newton_raphson()