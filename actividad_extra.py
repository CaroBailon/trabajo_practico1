# Creo la tabla de posiciones usando diccionarios y tuplas para almacenar los equipos y sus puntos
standings_table = {}

# Creo el menu interactivo

while True:
    print("\nTORNEO DE FÚTBOL:")
    print("\t1. Agregar equipo")
    print("\t2. Registrar resultado")
    print("\t3. Mostrar tabla")
    print("\t4. Eliminar equipo")
    print("\t5. Salir")

# Pido al usuario que elija una opción del menú
    option = input("Elige una opción: ")
    
    # Implemento las opciones 
    if option == "1":
        print("Elegiste: Agregar equipo")

        # Creo un nuevo equipo
        new_team = input("\n\tIngrese el nombre del equipo: ").capitalize()

        # Verifico si el equipo ya esta creado
        if new_team in standings_table :
            print(f"\n\tError!. El equipo {new_team} ya está inscripto.")
        else:
            standings_table[new_team]=0
            print(f"\n\tEl equipo {new_team} ha sido agregado a la tabla de posiciones.")

    elif option == "2":
        print("Elegiste: Registrar resultado")
        
        # Recibo la informacion del partido
        local = input("\n\tIngrese el nombre del equipo local: ").capitalize()
        visitor = input("\n\tIngrese el nombre del equipo visitante: ").capitalize()

        # Verifico que ambos equipos existan en la tabla de posiciones
        if local not in standings_table or visitor not in standings_table:
            print("\n\tError!. Ambos equipos deben estar inscriptos en la tabla de posiciones.")
            continue 

        # Pido el marcador
        marker = input("\n\tIngrese el marcador del partido (formato: local - visitante): ")
        try:

            # Separo el marcador en goles locales y visitantes usando split y convierto a enteros para poder comparar
            goals = marker.split(" - ") 
            goals_local = int(goals[0])
            goals_visitor = int(goals[1])
        except:
            print("\n\tError! Formato de marcador inválido. Usar 'goles - goles'.")
            continue

        # Actualizo la tabla de posiciones según el resultado del partido
        if goals_local > goals_visitor:
            standings_table[local] += 3
            print(f"\n\tGanó {local}. +3 puntos.")
        elif goals_visitor > goals_local:
            standings_table[visitor] += 3
            print(f"\n\tGanó {visitor}. +3 puntos.")
        else:
            standings_table[local] += 1
            standings_table[visitor] += 1
            print("\n\tEmpate. +1 punto para cada uno.")
        
    elif option == "3":
        print("Elegiste: Mostrar tabla")

        # Muestro la tabla de posiciones ordenada por puntos de mayor a menor
        # Verifico si hay equipos (para que no salga una tabla vacía)
        if not standings_table:
            print("\n\tLa tabla está vacía. Agregue equipos primero!")
        else:
            ordered_table = sorted(standings_table.items(), key=lambda item: item[1], reverse=True)

            print("Tabla de posiciones: ")
            print(f"\t{'Equipo':<15} {'Puntos':<10}") 
            print("\t" + "-" * 26)
            
            # Muestro la lista con los equipos ordenados por puntos
            for equipo, puntos in ordered_table:
                print(f"\t{equipo:<15} {puntos:<10}")
        
    elif option == "4":
        print("Elegiste: Eliminar equipo")
        
        #Pido el nombre del equipo a eliminar
        team_to_delete = input("\n\tIngrese el nombre del equipo a eliminar: ").capitalize()
        
        # Verifico si existe el equipo en el torneo
        if team_to_delete in standings_table:
            del standings_table[team_to_delete]
            print(f"\n\tEl equipo '{team_to_delete}' fue eliminado del torneo.")
        else:
            print(f"\n\tError! El equipo '{team_to_delete}' no se encuentra en la tabla.")

    elif option == "5":
        print("Saliendo del programa.")
        break

    else:
        print("Opción no válida, intenta de nuevo.")