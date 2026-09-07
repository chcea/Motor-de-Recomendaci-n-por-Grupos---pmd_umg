"""
Motor de Recomendación por Grupos (Amigos en Común)
Proyecto de Matemáticas Discretas - Teoría de Conjuntos y Relaciones

Idea central: cada usuario se representa como un CONJUNTO de intereses.
Las recomendaciones se generan aplicando operaciones de conjuntos:
    - Intersección (&)  -> intereses/amigos en común
    - Unión (|)          -> todos los intereses combinados de un grupo
    - Diferencia (-)      -> lo que uno tiene y el otro no (para sugerir algo nuevo)
"""

# ---------------------------------------------------------
# 1. REPRESENTACIÓN DE USUARIOS COMO CONJUNTOS
# ---------------------------------------------------------
# Cada usuario es una clave del diccionario, y su valor es un SET de intereses.
# Usamos sets (no listas) porque no permiten duplicados y tienen operaciones
# matemáticas de conjuntos ya integradas en Python.

usuarios = {
    "Ana":    {"música", "fútbol", "cine", "lectura"},
    "Luis":   {"fútbol", "videojuegos", "cine", "programación"},
    "Marta":  {"música", "pintura", "lectura", "viajar"},
    "Carlos": {"programación", "videojuegos", "fútbol", "gaming"},
    "Sofía":  {"lectura", "música", "viajar", "cocina"},
}


# ---------------------------------------------------------
# 2. OPERACIONES BÁSICAS DE CONJUNTOS
# ---------------------------------------------------------

def interseccion(a: set, b: set) -> set:
    """Devuelve los elementos que están en AMBOS conjuntos (intereses en común)."""
    return a & b  # equivalente a a.intersection(b)


def union(a: set, b: set) -> set:
    """Devuelve todos los elementos combinados de ambos conjuntos, sin duplicados."""
    return a | b  # equivalente a a.union(b)


def diferencia(a: set, b: set) -> set:
    """Devuelve lo que tiene 'a' que 'b' NO tiene (posibles sugerencias nuevas)."""
    return a - b  # equivalente a a.difference(b)


# ---------------------------------------------------------
# 3. MOTOR DE RECOMENDACIÓN
# ---------------------------------------------------------

def calcular_afinidad(usuarios: dict) -> list:
    """
    Compara cada par de usuarios y calcula:
      - sus intereses en común (intersección)
      - qué tan "afines" son (tamaño de la intersección)
    Devuelve una lista ordenada de mayor a menor afinidad.
    """
    resultados = []
    nombres = list(usuarios.keys())

    # Comparamos cada usuario con cada uno de los demás (sin repetir parejas)
    for i in range(len(nombres)):
        for j in range(i + 1, len(nombres)):
            persona_a = nombres[i]
            persona_b = nombres[j]

            comunes = interseccion(usuarios[persona_a], usuarios[persona_b])
            nivel_afinidad = len(comunes)  # entre más intereses comunes, más afinidad

            resultados.append({
                "persona_a": persona_a,
                "persona_b": persona_b,
                "intereses_comunes": comunes,
                "afinidad": nivel_afinidad,
            })

    # Ordenamos de mayor a menor afinidad
    resultados.sort(key=lambda x: x["afinidad"], reverse=True)
    return resultados


def sugerir_nuevos_intereses(persona_a: str, persona_b: str, usuarios: dict) -> set:
    """
    Sugiere a 'persona_a' los intereses de 'persona_b' que 'persona_a' aún no tiene.
    Ejemplo de uso de la diferencia de conjuntos como "sistema de sugerencia".
    """
    return diferencia(usuarios[persona_b], usuarios[persona_a])


# ---------------------------------------------------------
# 4. EJECUCIÓN / DEMOSTRACIÓN
# ---------------------------------------------------------

if __name__ == "__main__":
    print("=" * 50)
    print("MOTOR DE RECOMENDACIÓN POR GRUPOS (AMIGOS EN COMÚN)")
    print("=" * 50)

    afinidades = calcular_afinidad(usuarios)

    print("\n--- Ranking de afinidad entre usuarios ---")
    for r in afinidades:
        print(f"{r['persona_a']} <-> {r['persona_b']}: "
              f"{r['afinidad']} interes(es) en común -> {r['intereses_comunes']}")

    print("\n--- Ejemplo de sugerencia de nuevos intereses ---")
    sugerencias = sugerir_nuevos_intereses("Ana", "Luis", usuarios)
    print(f"A Ana le podría interesar (basado en Luis): {sugerencias}")