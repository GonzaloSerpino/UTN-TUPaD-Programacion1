#Ejercicio 2)
#Creo un flag para indicar si la cuenta esta bloqueada o tuvo un acceso exitoso
flag = False
usuario_correcto = "alumno"
clave_correcta = "python123"


for i in range(3):
    usuario = input("Ingrese su nombre de usuario: ")
    clave = input("Ingrese su contraseña: ")
    
    if usuario == usuario_correcto and clave == clave_correcta:
        print(f"Intento {i + 1}/3 - Usuario: {usuario} - \n Contraseña: {clave}")
        print("Acceso concedido")
        flag = True
        #Agrego el break por si el usuario ingresa las credenciales correctas antes de agotar los 3 intentos
        break

while True:
    #Chequeo si la cuenta esta bloqueada o tuvo un acceso exitoso
    if flag == False:
        print("Cuenta bloqueada.")
        break
    else:
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir ")
        opcion = input("Opcion: ")
        while opcion.isdigit() == False or int(opcion) < 1 or int(opcion) > 4:
            print("Opción inválida. Por favor, ingrese una opción válida.")
            opcion = input("Opcion: ")
        opcion = int(opcion)
        
        if opcion == 1:
            print("Estado: Inscripto")
        elif opcion == 2:
            nueva_clave = input("Ingrese su nueva contraseña: ")
            if len(nueva_clave) < 6:
                print("La contraseña debe tener al menos 6 caracteres. Por favor, ingrese una contraseña válida.")
                break
            else:
                nueva_clave_confirmacion = input("Confirme su nueva contraseña: ")
                if nueva_clave == nueva_clave_confirmacion:
                    clave_correcta = nueva_clave
                    print("Contraseña cambiada exitosamente.")
                else:
                    print("Las contraseñas no coinciden. La contraseña no ha sido cambiada.")
                    break
        elif opcion == 3:
            print("Cree en ti mismo, toma riesgos y trabaja con pasión, ya que el éxito es la suma de pequeños esfuerzos diarios, no de un golpe de suerte")
        elif opcion == 4:
            break