import random

# Agrupo las palabras por categoria usando diccionarios 

categories = {
    "Programacion": ["python", "variable", "bucle", "lista", "funcion"],
    "Frutas": ["manzana", "banana", "frutilla", "naranja", "cereza"],
    "Paises": ["argentina", "uruguay", "brasil", "chile", "espania"]
}

# Agrego antes del while total_score para que se acumule el puntaje total del jugador
total_score = 0

# Agrego la opcion de mostrar las categorias para que el jugador pueda elegir
while True:
    print("¡Bienvenido al Ahorcado!")
    print()
    print("\nCategorías disponibles:", ", ".join(categories.keys()))

    selection = input("\nElige una categoria : ").capitalize()
    print(f"\nElegiste la categoria: {selection}!")

    # Obtengo la lista de la categoria elegida
    original_list  = categories[selection]

    # Creo una lista con las palabras mezcladas para que no se repitan
    mixed_word = random.sample(original_list, len(original_list))

    # Simulo varias rondas seguidas 
    for word in mixed_word: 
        guessed = []
        attempts = 6

        # Agrego variable score para contabilizar los puntos
        score = 0
        print(f"\nNueva ronda!: Categoría {selection} ")

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
                print("\n¡Ganaste!")
                score += 6
                break

            print(f"Intentos restantes: {attempts}")
            print(f"Letras usadas: {', '.join(guessed)}")

            # Si es mayúscula la convierto en minúscula para no extender la condicion en (1)
            letter = input("Ingresá una letra: ").lower()

            # Corregimos el bug (1)
            if len(letter) > 1 or letter < "a" or letter > "z" :
                print("\nEntrada no válida!")
                continue

            if letter in guessed:
                print("\nYa usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("\n¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                print("\nEsa letra no está en la palabra.")
                score -= 1
            print()

        if attempts ==0:
            print(f"\n¡Perdiste! La palabra era: {word}")
            score = 0 

        print(f"\nEl puntaje del jugador es de : {score} puntos. ")

        # Acumulo puntajes por ronda pero igual mostramos el puntaje por cada una
        total_score += score

        #Pregunto si quiere seguir jugando en la misma categoria, sino sale del for 
        option = input("\n¿Quieres jugar la siguiente palabra de esta categoría? (si/no): ").lower()
        if option != "si":
            break
        
    print(f"\nTerminaste con las palabras de {selection}.")
    
    #Pregunto si quiere elegir otra categoria o prefiere terminar el juego
    go_back = input("\n¿Quieres elegir OTRA categoría? (si/no): ").lower()
    if go_back != "si":
        print("Fin del juego!")
        print(f"Puntaje total obtenido = {total_score}")
        break