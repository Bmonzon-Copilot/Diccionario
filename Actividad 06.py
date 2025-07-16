def ingresar_producto(inventario):
    while True:
        codigo = input("Ingrese el código del producto (ej. P001): ").strip()
        if codigo in inventario:
            print("\Ese código ya existe. Intente con otro.")
        else:
            break

    nombre = input("Ingrese el nombre del producto: ").strip()

    while True:
        categoria = input("Ingrese la categoría (Hombre, Mujer, Niño): ").capitalize()
        if categoria in ["Hombre", "Mujer", "Niño"]:
            break
        else:
            print("\Categoría no válida. Intente de nuevo.")

    while True:
        talla = input("Ingrese la talla (S, M, L, XL): ").upper()
        if talla in ["S", "M", "L", "XL"]:
            break
        else:
            print("\Talla no válida. Intente de nuevo.")

    while True:
        try:
            precio = float(input("Ingrese el precio unitario (> 0): "))
            if precio > 0:
                break
            else:
                print("\El precio debe ser mayor a 0.")
        except ValueError:
            print("\Entrada no válida. Ingrese un número.")

    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en stock (entero positivo): "))
            if cantidad >= 0:
                break
            else:
                print("\La cantidad debe ser 0 o mayor.")
        except ValueError:
            print("\Entrada no válida. Ingrese un número entero.")

    inventario[codigo] = {
        "nombre": nombre,
        "categoría": categoria,
        "talla": talla,
        "precio": precio,
        "cantidad": cantidad
    }
