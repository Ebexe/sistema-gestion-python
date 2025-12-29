def obtener_score(fila):
    """
    Calcula el puntaje de crédito (0-100) aplicando penalizaciones.
    Entrada: Una fila del DataFrame (con Id_Trabajo, Tipo_Vivienda, Propósito, Edad).
    Salida: Entero (Score).
    """
    puntaje = 100
    
    # Regla A: Trabajo 
    if fila['Id_Trabajo'] == 'Desempleado/eventual':
        puntaje -= 30 
    elif fila['Id_Trabajo'] == 'Operativo/Técnico':
        puntaje -= 10
        
    # Regla B: Vivienda
    if fila['Tipo_Vivienda'] in ['Alquiler', 'Cedida/Gratis']:
        puntaje -= 20
        
    # Regla C: Propósito 
    if fila['Propósito'] in ['Vacaciones', 'Electrodomésticos', 'Otros/Varios']:
        puntaje -= 10
        
    # Regla D: Edad
    if fila['Edad'] < 25:
        puntaje -= 10

    return puntaje

def definir_etiqueta(puntos):
    """
    Clasifica el riesgo basado en el puntaje de corte (82).
    """
    if puntos < 82:
        return 'Deficiente'
    else:
        return 'Normal'