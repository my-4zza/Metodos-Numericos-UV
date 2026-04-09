import sympy as sp               # Azael Pérez González
import numpy as np               # Agregado para el manejo de arreglos en la gráfica.
import matplotlib.pyplot as plt  # Agregado para generar las gráficas.

def graficar_resultados(g, x_ini, x_fin, iteraciones, errores):
    # Crea una figura con dos subgráficos (1 fila, 2 columnas).
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

    # Gráfica de la función.
    margen = abs(x_fin - x_ini) + 2 if x_ini != x_fin else 5
    x_vals = np.linspace(min(x_ini, x_fin) - margen, max(x_ini, x_fin) + margen, 400)
    y_vals = [g(val) for val in x_vals]
    
    ax1.plot(x_vals, y_vals, label='g(x)', color='blue')
    # Añadida la recta y=x para visualizar la intersección característica del punto fijo.
    ax1.plot(x_vals, x_vals, label='y = x', color='gray', linestyle=':') 
    
    ax1.axhline(0, color='black', linewidth=1)
    ax1.axvline(x_ini, color='red', linestyle='--', label=f'x_0 inicial ({x_ini:.4f})')
    ax1.axvline(x_fin, color='green', linestyle='--', label=f'Raíz aprox ({x_fin:.4f})')
    ax1.set_title("Gráfica de la Función g(x)")
    ax1.set_xlabel("x")
    ax1.set_ylabel("g(x)")
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
# ===========================
def punto_fijo():
    x = sp.Symbol('x')
    print("--- Método del Punto Fijo ---")
    print("Recuerda despejar 'x' de tu ecuación f(x) = 0 para obtener x = g(x).")
    
    g_str = input("Ingresa la función g(x): ")
    g_expr = sp.sympify(g_str)
    g = sp.lambdify(x, g_expr, 'math')

    # Punto inicial x_0.
    x_0 = float(input("Ingresa el punto inicial (x_0): "))
    
    # Se solicita el error absoluto.
    tol = float(input("Ingresa el error absoluto esperado: "))

    # Guardado del punto inicial para la gráfica.
    x_0_ini = x_0

    # Inicializa en infinito para garantizar la entrada al ciclo.
    error = float('inf')
    iteracion = 1

    # Almacenamiento de los datos a graficar.
    lista_iteraciones = []
    lista_errores = []

    # Actualización del encabezado con x_i+1.
    print(f"\n{'Iter':<5} | {'x_i+1':<15} | {'Error Abs':<15}")
    print("-" * 40)

    while error > tol:
        try:
            # Evaluar la función ingresada.
            x_1 = g(x_0)
        except Exception as e:
            print(f"\nOcurrió un error al evaluar la función: {e}")
            break
            
        # Cálculo del error absoluto directo y sin riesgo de dividir entre cero.
        error = abs(x_1 - x_0)
            
        print(f"{iteracion:<5} | {x_1:<15.5f} | {error:<15.5f}")
        
        # Guardado de los datos de la iteración actual.
        lista_errores.append(error)
        lista_iteraciones.append(iteracion)
        
        # Actualización de la variable para la siguiente iteración.
        x_0 = x_1
        iteracion += 1
        
        # Límite de seguridad para evitar bucles infinitos.
        if iteracion > 100:
            print("\nEl método diverge con este despeje o punto inicial.")
            break

    # Solo se imprime el resultado si realmente llegó a la tolerancia.
    if error <= tol:
        print(f"\nLa raíz aproximada es: {x_0:.7f}")
        
        # Llama a la función para graficar al terminar el cálculo.
        graficar_resultados(g, x_0_ini, x_0, lista_iteraciones, lista_errores)

if __name__ == "__main__":
    punto_fijo()