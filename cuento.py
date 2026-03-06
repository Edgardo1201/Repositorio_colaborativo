import random

fabulas = [
    "La liebre y la tortuga: La constancia y el esfuerzo vencen la arrogancia y la prisa.",
    "El pastor y el lobo: Si mientes muchas veces, nadie te creerá cuando digas la verdad.",
    "La hormiga y la cigarra: Hay que prepararse con tiempo y no dejar todo para después.",
    "El león y el ratón: Ningún acto de bondad es pequeño, todos podemos ayudar.",
    "La zorra y las uvas: A veces despreciamos lo que no podemos conseguir."
]

def mostrar_cuento():
    cuento = random.choice(fabulas)
    print("\n=== CUENTO / FÁBULA ALEATORIA ===")
    print(cuento)
