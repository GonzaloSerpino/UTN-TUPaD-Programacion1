#Ejercicio 3)
#Inicializo las variables que van a contener los nombres de los pacientes para cada turno
lunes1 = "libre"
lunes2 = "libre"
lunes3 = "libre"
lunes4 = "libre"
martes1 = "libre"
martes2 = "libre"
martes3 = "libre"

nombre_operador = input("Ingrese el nombre del operador: ")
#Validacion nombre del operador
while nombre_operador.isalpha() == False or nombre_operador.isspace() == True:
    print("El nombre del operador no puede contener números o caracteres especiales. Por favor, ingrese un nombre válido.")
    nombre_operador = input("Ingrese el nombre del operador: ")
    
while True:
    print(" 1) Reservar turno \n 2) Cancelar turno (por nombre) \n 3) Ver agenda del dia \n 4) Ver resumen general \n 5) Cerrar sistema")
    
    opcion = input("Opcion: ")
    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 5:
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Opcion: ")
    opcion = int(opcion)
    
    if opcion == 1:
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        while dia.isdigit() == False or int(dia) < 1 or int(dia) > 2:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        dia = int(dia)

        paciente = input("Ingrese el nombre del paciente: ")
        while paciente.isalpha() == False or paciente.isspace() == True:
            print("El nombre del paciente no puede contener números o caracteres especiales. Por favor, ingrese un nombre válido.")
            paciente = input("Ingrese el nombre del paciente: ")
        
        #Valido que el paciente no tenga un turno reservado para ese dia.
        flag = True
        if dia == 1:
            for i in range(4):
                if paciente.lower() == lunes1 or paciente.lower() == lunes2 or paciente.lower() == lunes3 or paciente.lower() == lunes4:
                    print("El paciente ya tiene un turno reservado para ese día. No se pueden reservar múltiples turnos para el mismo paciente en el mismo día.")
                    flag = False
                    break
        elif dia == 2:
            for i in range(3):
                if paciente.lower() == martes1 or paciente.lower() == martes2 or paciente.lower() == martes3:
                    print("El paciente ya tiene un turno reservado para ese día. No se pueden reservar múltiples turnos para el mismo paciente en el mismo día.")
                    flag = False
                    break
                
        #Valido el dia elegido y luego valido los turnos disponibles para ese dia, asignando el paciente al primer turno disponible.
        if dia == 1 and flag == True:
            if lunes1 == "libre":
                lunes1 = paciente.lower()
                print(f"Turno reservado para {paciente}")
            elif lunes2 == "libre":
                lunes2 = paciente.lower()
                print(f"Turno reservado para {paciente}")
            elif lunes3 == "libre":
                lunes3 = paciente.lower()
                print(f"Turno reservado para {paciente}")
            elif lunes4 == "libre":
                lunes4 = paciente.lower()
                print(f"Turno reservado para {paciente}")
            else:
                print("No hay turnos disponibles para ese día.")
        elif dia == 2 and flag == True:
            if martes1 == "libre":
                martes1 = paciente.lower()
                print(f"Turno reservado para {paciente}")
            elif martes2 == "libre":
                martes2 = paciente.lower()
                print(f"Turno reservado para {paciente}")
            elif martes3 == "":
                martes3 = paciente.lower()
                print(f"Turno reservado para {paciente}")
            else:
                print("No hay turnos disponibles para ese día.")
        
    elif opcion == 2:
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        while dia.isdigit() == False or int(dia) < 1 or int(dia) > 2:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            dia = input("Elegir dia (1=Lunes, 2=Martes): ")
            
        paciente = input("Ingrese el nombre del paciente: ")
        while paciente.isalpha() == False or paciente.isspace() == True:
            print("El nombre del paciente no puede contener números o caracteres especiales. Por favor, ingrese un nombre válido.")
            paciente = input("Ingrese el nombre del paciente: ")
                
        if dia == 1:
            if paciente.lower() == lunes1:
                lunes1 = "libre"
                print(f"Turno cancelado para {paciente}")
            elif paciente.lower() == lunes2:
                lunes2 = "libre"
                print(f"Turno cancelado para {paciente}")
            elif paciente.lower() == lunes3:
                lunes3 = "libre"
                print(f"Turno cancelado para {paciente}")
            elif paciente.lower() == lunes4:
                lunes4 = "libre"
                print(f"Turno cancelado para {paciente}")
            else:
                print("No se encontró un turno reservado para ese paciente en ese día.")
        elif dia == 2:
            if paciente.lower() == martes1:
                martes1 = "libre"
                print(f"Turno cancelado para {paciente}")
            elif paciente.lower() == martes2:
                martes2 = "libre"
                print(f"Turno cancelado para {paciente}")
            elif paciente.lower() == martes3:
                martes3 = "libre"
                print(f"Turno cancelado para {paciente}")
            else:
                print("No se encontró un turno reservado para ese paciente en ese día.")
        
    elif opcion == 3:
        dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        while dia.isdigit() == False or int(dia) < 1 or int(dia) > 2:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            dia = input("Elegir dia (1=Lunes, 2=Martes): ")
        dia = int(dia)
        
        if dia == 1:
            print(f"Lunes - Turno 1: {lunes1}, Turno 2: {lunes2}, Turno 3: {lunes3}, Turno 4: {lunes4}")
        elif dia == 2:
            print(f"Martes - Turno 1: {martes1}, Turno 2: {martes2}, Turno 3: {martes3}")
            
    elif opcion == 4:
        count_lunes = 0
        count_martes = 0
        #Creo una matriz for para contar la cantidad de turnos ocupados en cada dia
        for i in range(2):
            if i == 0:
                for j in range(4):
                    if lunes1 != "libre":
                        count_lunes += 1
                    elif lunes2 != "libre":
                        count_lunes += 1
                    elif lunes3 != "libre":
                        count_lunes += 1
                    elif lunes4 != "libre":
                        count_lunes += 1
            elif i == 1:
                for j in range(3):
                    if martes1 != "libre":
                        count_martes += 1
                    elif martes2 != "libre":
                        count_martes += 1
                    elif martes3 != "libre":
                        count_martes += 1
                        
        print(f"Resumen general: \nLunes - Turno 1: {lunes1}, Turno 2: {lunes2}, Turno 3: {lunes3}, Turno 4: {lunes4} \nMartes - Turno 1: {martes1}, Turno 2: {martes2}, Turno 3: {martes3}")
        if count_lunes > count_martes:
            print("El día con más turnos ocupados es Lunes.")
        elif count_martes > count_lunes:
            print("El día con más turnos ocupados es Martes.")
        else:
            print("Ambos días tienen la misma cantidad de turnos ocupados.")

    elif opcion == 5:
        break