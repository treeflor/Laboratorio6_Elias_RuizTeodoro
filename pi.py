# Función para consultar el inventario
def consultar_inventario(inventario, producto):
    if producto in inventario:
        return f"{producto}: {inventario[producto]} unidades"
    else:
        return f"El producto '{producto}' no se encuentra en el inventario."

# Función para agregar un producto al inventario
def agregar_producto(inventario, producto, cantidad):
    if producto in inventario:
        inventario[producto] += cantidad
        return f"Cantidad de '{producto}' actualizada a {inventario[producto]} unidades."
    else:
        inventario[producto] = cantidad
        return f"Producto '{producto}' agregado con {cantidad} unidades."

# Función para eliminar un producto del inventario
def eliminar_producto(inventario, producto):
    if producto in inventario:
        del inventario[producto]
        return f"Producto '{producto}' eliminado del inventario."
    else:
        return f"El producto '{producto}' no se encuentra en el inventario."

# Función para mostrar el inventario completo
def mostrar_inventario(inventario):
    if inventario:
        print("Inventario actual:")
        for producto, cantidad in sorted(inventario.items()):
            print(f"- {producto}: {cantidad} unidades")
    else:
        print("El inventario está vacío.")

# Programa principal
def main():
    inventario = {'manzanas': 50, 'bananas': 30}
    mostrar_inventario(inventario)
    
    while True:
        accion = input("\n¿Qué acción deseas realizar? (consultar/agregar/eliminar/mostrar/salir): ").lower()
        
        if accion == "consultar":
            producto = input("Ingresa el nombre del producto: ").lower()
            print(consultar_inventario(inventario, producto))
        
        elif accion == "agregar":
            producto = input("Ingresa el nombre del producto: ").lower()
            try:
                cantidad = int(input("Ingresa la cantidad: "))
                print(agregar_producto(inventario, producto, cantidad))
            except ValueError:
                print("Por favor, ingresa una cantidad válida.")
        
        elif accion == "eliminar":
            producto = input("Ingresa el nombre del producto: ").lower()
            print(eliminar_producto(inventario, producto))
        
        elif accion == "mostrar":
            mostrar_inventario(inventario)
        
        elif accion == "salir":
            print("Saliendo del programa.")
            break
        
        else:
            print("Acción no reconocida. Por favor, intenta de nuevo.")

        # Mostrar el inventario actualizado después de cada operación
        mostrar_inventario(inventario)

# Ejecutar el programa principal
main()
