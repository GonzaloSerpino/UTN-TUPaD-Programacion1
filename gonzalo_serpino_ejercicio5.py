import time
import os

print("--- BIENVENIDO A LA ARENA ---")
nombre_gladiador = input("Ingrese el nombre del gladiador: ")

while nombre_gladiador.isalpha() == False:
    print("Error. Solo se permiten letras")
    nombre_gladiador = input("Ingrese el nombre del gladiador: ")
    
hp_gladiador = 100
hp_enemigo = 100
pociones_vida = 3
base_gladiador = 15
base_enemigo = 12
turno_gladiador = True
multiplicador_critico = 1.5
primer_turno = True


while hp_gladiador > 0 and hp_enemigo > 0:

        
    if turno_gladiador:
        if primer_turno:
            primer_turno = False
            print("=== INICIO DEL COMBATE ===")
        else:
            print("=== NUEVO TURNO ===")
        
        print(f"Vida {nombre_gladiador}: {hp_gladiador} vs Vida Enemigo: {hp_enemigo} | Pociones: {pociones_vida}")
        accion = input("Elija una acción: \n 1. Ataque Ligero\n 2. Rafaga Veloz \n 3. Curar (+30 de vida) \n")
        while accion.isdigit() == False or int(accion) < 1 or int(accion) > 3:
            print("Error. Ingrese una opción válida.")
            accion = input("Elija una acción: \n 1. Ataque Ligero \n 2. Rafaga Veloz \n 3. Curar (+30 de vida) \n")
        accion = int(accion)
        
        if accion == 1:
            if hp_enemigo < 20:
                daño = base_gladiador * multiplicador_critico
            else:
                daño = base_gladiador
            hp_enemigo -= daño
            print(f"¡Atacaste al enemigo por {daño} puntos de daño!")
        elif accion == 2:
            print("¡Inicias una rafaga de golpes!")
            for i in range(3):
                hp_enemigo -= 5
                print("Golpe conectado por 5 de daño")
                time.sleep(0.5)
        else:
            if pociones_vida > 0:
                hp_gladiador += 30
                pociones_vida -= 1
                print("¡Has usado una poción! +30 de vida.")
            else:
                print("¡No quedan pociones!.")
        turno_gladiador = False
        time.sleep(1)
    else:
        hp_gladiador -= base_enemigo
        print(f"\n¡El Enemigo te ataco por 12 puntos de daño!")
        turno_gladiador = True
        time.sleep(2)
        os.system("cls" if os.name == "nt" else "clear")

    if hp_gladiador <= 0:
        print("DERROTA. Has caido en combate.")
    elif hp_enemigo <= 0 and hp_gladiador > 0:
        print(f"¡VICTORIA! {nombre_gladiador} ha ganado la batalla.")