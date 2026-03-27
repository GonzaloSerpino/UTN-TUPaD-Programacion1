#Ejercicio 1)
nombre_cliente = input("Ingrese el nombre del cliente: ")
#Validacion nombre de cliente
while nombre_cliente.isalpha() == False or nombre_cliente.isspace() == True:
    print("El nombre del cliente no puede contener números o caracteres especiales. Por favor, ingrese un nombre válido.")
    nombre_cliente = input("Ingrese el nombre del cliente: ")


cant_productos = input("Ingrese la cantidad de productos que desea comprar: ")
#Validacion cantidad de productos
while cant_productos.isdigit() == False or int(cant_productos) <= 0:
    print("La cantidad de productos debe ser un número entero positivo. Por favor, ingrese una cantidad válida.")
    cant_productos = input("Ingrese la cantidad de productos que desea comprar: ")

#Luego de la validacion, parseo la cantidad de productos a entero para poder usarlo en el ciclo for
cant_productos = int(cant_productos)


#Inicializo variables y listas para almacenar los precios y si aplica descuento de cada producto
ahorro = 0
precio_descuento = 0
precio_total = 0
lista_precios = []
lista_descuentos = []
#Inicio de ciclo for
for i in range(cant_productos):
    precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    #Validacion precio del producto
    while precio <= 0:
        print("El precio del producto debe ser un número positivo. Por favor, ingrese un precio válido.")
        precio = float(input(f"Ingrese el precio del producto {i + 1}: "))
    lista_precios.append(precio)  # Almaceno el precio del producto en la lista de precios
    
    descuento = input("¿El producto tiene descuento? (s/n): ")
    #Validacion descuento
    while descuento.lower() not in ['s', 'n']:
        print("Por favor, ingrese 's' para sí o 'n' para no.")
        descuento = input("¿El producto tiene descuento? (s/n): ")
    lista_descuentos.append(descuento)  # Almaceno si el producto tiene descuento
    
    #Aplicar descuento si corresponde y almacenar los precios totales
    if descuento.lower() == 's':
        precio_descuento += precio * 0.9  # Aplica un descuento del 10%
    else:
        precio_descuento += precio
    precio_total += precio 
    ahorro = precio_total - precio_descuento 

print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cant_productos}")
print(f"Total sin descuentos: {precio_total:.2f}")
print(f"Total con descuentos: {precio_descuento:.2f}")
print(f"Ahorro total: {ahorro:.2f}")
print(f"Promedio por producto: {(precio_descuento / cant_productos):.2f}")