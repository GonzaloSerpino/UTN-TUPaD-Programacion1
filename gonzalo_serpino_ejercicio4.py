#Ejercicio 4)
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 
forzar_seguidas = 0
flag_bloqueo = False

nombre_agente = input("Ingrese el nombre del agente: ")
#Validacion nombre del agente
while nombre_agente.isalpha() == False or nombre_agente.isspace() == True:
    print("El nombre del agente no puede contener números o caracteres especiales. Por favor, ingrese un nombre válido.")
    nombre_agente = input("Ingrese el nombre del agente: ")
    
while tiempo > 0 and energia > 0 and cerraduras_abiertas < 3 and flag_bloqueo == False:
    print(" 1) Forzar Cerradura \n 2) Hackear Panel \n 3) Descansar")
    opcion = input("Opcion: ")
    while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 3:
        print("Opción inválida. Por favor, ingrese una opción válida.")
        opcion = input("Opcion: ")
    opcion = int(opcion)
    
    if opcion == 1:
        energia -= 20
        tiempo -= 2       
        if forzar_seguidas == 2:
            print("Has forzado la cerradura 3 veces seguidas. La alarma se ha activado.")
            alarma = True
            print(f"Energía restante: {energia}, Tiempo restante: {tiempo}")
            
        elif energia < 40:
            seleccion = input("Riesgo de alarma, seleccionar un numero del 1 al 3:")
            while seleccion.isdigit() == False or int(seleccion) < 1 or int(seleccion) > 3:
                print("Opción inválida. Por favor, ingrese una opción válida.")
                seleccion = input("Seleccion: ")
            seleccion = int(seleccion)
            
            if seleccion == 1 or seleccion == 2:
                print("Cerradura forzada exitosamente")
                cerraduras_abiertas += 1
                forzar_seguidas += 1
                print(f"Cerraduras abiertas: {cerraduras_abiertas}, Energía restante: {energia}, Tiempo restante: {tiempo}")
            else:
                print("Has seleccionado la opción incorrecta. La alarma se ha activado.")
                alarma = True
                print(f"Energía restante: {energia}, Tiempo restante: {tiempo}")
                
        else:
            cerraduras_abiertas += 1
            forzar_seguidas += 1
            print(f"Cerradura forzada exitosamente. Cerraduras abiertas: {cerraduras_abiertas}, Energía restante: {energia}, Tiempo restante: {tiempo}")

    elif opcion == 2:
        forzar_seguidas = 0
        for i in range(4):
            codigo = input(f"Ingrese una letra del código: ")
            while codigo.isalpha() == False or nombre_agente.isspace() == True:
                print("Opción inválida. Por favor, ingrese un número del 0 al 9.")
                digito = input(f"Ingrese el dígito {i + 1} del código: ")
            codigo_parcial += codigo
            
        if len(codigo_parcial) >= 8:
            print("Código hackeado exitosamente. La cerradura se ha abierto.")
            cerraduras_abiertas += 1
            tiempo -= 3
            energia -= 10
            codigo_parcial = ""
            print(f"Cerraduras abiertas: {cerraduras_abiertas}, Energía restante: {energia}, Tiempo restante: {tiempo}")
        else:
            tiempo -=3
            energia -= 10
            print(f"Código hackeado parcialmente. Tiempo restante: {tiempo}, Energía restante: {energia}")
            
    elif opcion == 3:
        forzar_seguidas = 0
        if energia <= 100 and alarma == True:
            energia += 5
        elif energia <= 100:
            energia += 15
        tiempo -= 1
        print(f"Descanso tomado. Energía restaurada a {energia}, Tiempo restante: {tiempo}")
        
    if alarma == True and tiempo <= 3 and cerraduras_abiertas < 3:
        flag_bloqueo = True
        break

if cerraduras_abiertas == 3:
    print("¡Felicidades! Has abierto las 3 cerraduras y completado la misión.")
elif flag_bloqueo == True:
    print("Has sido bloqueado por la alarma. Misión fallida.")
elif tiempo <= 0 and energia <= 0:
    print("Has agotado tu tiempo y energía. Misión fallida.")