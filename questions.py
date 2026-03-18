import random

# Agrupamos las palabras por categoria

categories = {
    "Programacion": ["python", "variable", "bucle", "lista", "funcion"],
    "Frutas": ["manzana", "banana", "frutilla", "naranja", "cereza"],
    "Paises": ["argentina", "uruguay", "brasil", "chile", "españa"]
}

# Agrego la opcion de mostrar las categorias para que el jugador pueda elegir

print("¡Bienvenido al Ahorcado!")
print()

print("Categorías disponibles:", ", ".join(categories.keys()))
selection = input("Elige una categoria : ").capitalize()
word= random.choice(categories[selection])
print(f"Elegiste la categoria {selection}!")

guessed = []
attempts = 6

# Agrego variable puntaje para contabilizar los puntos
score = 0

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print("¡Ganaste!")
        score += 6
        break

    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    # Si es mayúscula la convierto en minúscula para no extender la condicion en (1)
    letter = input("Ingresá una letra: ").lower()

    # Corregimos el bug (1)
    if len(letter) > 1 or letter < "a" or letter > "z" :
        print("Entrada no válida!")
        continue

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")
        score -= 1

    print()

else:
    print(f"¡Perdiste! La palabra era: {word}")
    score = 0 

print(f"El puntaje del jugador es de : {score} puntos. ")