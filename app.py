import sys

def seleccionar_prueba():
    print("--- Asistente de Selección de Prueba Estadística ---")
    print("Responda las preguntas con 'si' o 'no'.")
    
    # 1. Objetivo principal: Relación vs Comparación de grupos
    objetivo = input("¿El objetivo es comparar grupos (medias/medianas) o buscar relación/predicción entre variables? (comparar/relacionar): ").lower()
    
    if objetivo == "relacionar":
        # Ruta para pruebas de relación/correlación/regresión
        print("\n--- Ruta de Relación ---")
        tipo_variable = input("¿Son ambas variables cuantitativas/continuas? (si/no): ").lower()
        
        if tipo_variable == "si":
            lineal = input("¿Se asume una relación lineal perfecta y normalidad bivariada estricta? (si/no): ").lower()
            if lineal == "si":
                print("\n-> Prueba recomendada: Correlación de Pearson o Regresión Lineal Simple (si se quiere predecir).")
            else:
                print("\n-> Prueba recomendada: Correlación de Spearman (más flexible, busca relación monótona).")
        else:
            print("\n-> Prueba recomendada: Correlación de Spearman (si al menos una es ordinal) o Chi-cuadrada (si ambas son categóricas).")
            
    elif objetivo == "comparar":
        # Ruta para pruebas de comparación de grupos
        print("\n--- Ruta de Comparación de Grupos ---")
        independencia = input("¿Las muestras son independientes (grupos distintos) o relacionadas (mismo sujeto antes/después)? (independientes/relacionadas): ").lower()
        
        if independencia == "relacionadas":
            # Ruta para muestras relacionadas
            normalidad = input("¿La diferencia entre los pares de datos sigue una distribución normal? (si/no): ").lower()
            if normalidad == "si":
                print("\n-> Prueba recomendada: t de Student para muestras relacionadas (paramétrica).")
            else:
                print("\n-> Prueba recomendada: Wilcoxon (no paramétrica, rangos signados).")
                
        elif independencia == "independientes":
            # Ruta para muestras independientes
            num_grupos = input("¿Cuántos grupos independientes se comparan? (2 o 3+): ").lower()
            
            if num_grupos == "2":
                normalidad = input("¿Los datos de ambos grupos siguen una distribución normal y tienen varianzas homogéneas? (si/no): ").lower()
                if normalidad == "si":
                    print("\n-> Prueba recomendada: t de Student para muestras independientes (paramétrica).")
                else:
                    print("\n-> Prueba recomendada: U de Mann-Whitney (no paramétrica, usa rangos).")
                    
            elif num_grupos == "3+":
                normalidad_varianzas = input("¿Los datos siguen normalidad y tienen homogeneidad de varianzas (homocedasticidad)? (si/no): ").lower()
                if normalidad_varianzas == "si":
                    print("\n-> Prueba recomendada: ANOVA de un factor (paramétrica).")
                else:
                    print("\n-> Prueba recomendada: Kruskal-Wallis (no paramétrica, usa rangos).")
            else:
                print("Número de grupos no reconocido.")
        else:
            print("Tipo de independencia no reconocido.")
    else:
        print("Objetivo no reconocido.")

if __name__ == "__main__":
    seleccionar_prueba()
