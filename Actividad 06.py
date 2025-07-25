def ingresar_producto(inventario):
    while True:
        codigo = input("Ingrese el código del producto: ").strip()
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
            cantidad = int(input("Ingrese la cantidad en stock: "))
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

def mostrar_inventario(inventario):
        print("\n\Inventario completo:")
        for codigo, datos in inventario.items():
            print(f"\nCódigo: {codigo}")
            for clave, valor in datos.items():
                print(f"  {clave.capitalize()}: {valor}")

def buscar_producto(inventario):
        codigo = input("\nIngrese el código del producto a buscar: ").strip()
        producto = inventario.get(codigo)
        if producto:
            print(f"\nProducto encontrado ({codigo}):")
            for clave, valor in producto.items():
                print(f"  {clave.capitalize()}: {valor}")
        else:
            print("Producto no encontrado.")
def calcular_valor_total(inventario):
    total = sum(p["precio"] * p["cantidad"] for p in inventario.values())
    print(f"\nValor total del inventario: Q{total:.2f}")
def contar_por_categoría(inventario):
    conteo = {"Hombre": 0, "Mujer": 0, "Niño": 0}
    for producto in inventario.values():
        categoria = producto["categoría"]
        if categoria in conteo:
            conteo[categoria] += 1
    print("\nProductos por categoría:")
    for cat, cant in conteo.items():
        print(f"  {cat}: {cant} producto(s)")

# Programa principal
def main():
    inventario = {}

    try:
        n = int(input("¿Cuántos productos desea ingresar? "))
        for i in range(n):
            print(f"\nIngresando producto #{i + 1}")
            ingresar_producto(inventario)

        mostrar_inventario(inventario)
        buscar_producto(inventario)
        calcular_valor_total(inventario)
        contar_por_categoría(inventario)

    except ValueError:
        print("Entrada no válida. Reinicie el programa.")

if __name__ == "__main__":
    main()
