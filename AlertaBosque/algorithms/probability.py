"""Punto 1. Distribuciones discretas y decisiones de respuesta."""
import math


def normalize(weights: dict) -> dict:
    """Retorna un diccionario nuevo cuyas probabilidades suman uno.

    Entrada: weights = {resultado: peso}.
    Salida: {resultado: probabilidad}, con las mismas claves.

    Tips:
    - Conserve las claves y su orden; no modifique weights.
    - Rechace pesos negativos, no finitos, diccionarios vacíos y suma cero.
    """
    # TODO: Add your code here
    
    total_weight = 0
    normalized_weights = {}
    if not weights: 
        raise ValueError("Diccionario vacío")
    for value in weights.values():
        if value < 0 or  not math.isfinite(value): 
            raise ValueError("Valor infinito o negativo")
        total_weight += value
    
    if total_weight == 0:
        raise ValueError("Peso total igual a 0")
    for id, value in weights.items():
        normalized_weights[id] = value/total_weight
        
    return normalized_weights
    # FIN DEL BLOQUE DEL ESTUDIANTE


def expected_utility(distribution: dict, utilities: dict) -> float:
    """Calcula sum_s P(s) U(s) para una acción.

    Entradas: distribution = {resultado: probabilidad} y
    utilities = {resultado: utilidad} para una sola acción.
    Salida: un número con la utilidad esperada.

    Tips:
    - distribution ya debe estar normalizada; no normalice utilidades.
    - Ambas tablas deben contener los mismos resultados posibles.
    """
    # Validación de las entradas; no modificar.
    if set(distribution) != set(utilities) or not distribution:
        raise ValueError("Probabilidades y utilidades deben tener las mismas claves")
    if any(not math.isfinite(p) or p < 0 for p in distribution.values()):
        raise ValueError("Distribución inválida")
    if not math.isclose(sum(distribution.values()), 1, abs_tol=1e-9):
        raise ValueError("La distribución debe sumar uno")
    if any(not math.isfinite(u) for u in utilities.values()):
        raise ValueError("Utilidades no finitas")
    # TODO: Add your code here
    expected_utility = 0
    for id, value in distribution.items():
        expected_utility +=  utilities[id]*value
    
    return expected_utility
    # FIN DEL BLOQUE DEL ESTUDIANTE


def best_action(distribution: dict, actions: dict) -> tuple[str, dict]:
    """Retorna (nombre de acción, utilidades esperadas por acción).

    Entradas: distribution = {resultado: probabilidad} y
    actions = {acción: {resultado: utilidad}}.
    Salida: (acción elegida, {acción: utilidad esperada}).

    Tips:
    - actions asocia cada acción con su tabla de utilidades.
    - Reutilice expected_utility y conserve la primera acción en los empates.
    """
    # Validación de las acciones; no modificar.
    if not actions:
        raise ValueError("Se requiere al menos una acción")
    # TODO: Add your code here
    
    best_action = ""
    best_expected_utility = -math.inf
    action_utilities = {}
    for id, action in actions.items():
        action_expected_utility = expected_utility(distribution,action)
        action_utilities[id] = action_expected_utility
        if action_expected_utility>best_expected_utility:
            best_action = id
            best_expected_utility = action_expected_utility
    return (best_action, action_utilities)


    # FIN DEL BLOQUE DEL ESTUDIANTE
