DESCUENTO = 0.15
menu = [
    ["Hamburguesa", "Comida Rapida", 18000],
    ["Pizza", "Comida Rapida", 32000],
    ["Ensalada", "Saludable", 15000],
    ["Jugo Natural", "Bebida", 8000],
    ["Pasta", "Italiana", 28000],
    ["Lasaña", "Italiana", 35000]
]

def calcular_precio_final(categoria, precio, categoria_objetivo, umbral):

    if categoria == categoria_objetivo and precio > umbral:
        descuento = precio * DESCUENTO
        precio_final = precio - descuento
    else:
        precio_final = precio

    return precio_final

categoria_objetivo = input("Ingrese la categoría para la promoción: ")
umbral = int(input("Ingrese el valor mínimo para aplicar descuento: "))

print("\nMENU CON PROMOCION\n")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

   
    precio_final = calcular_precio_final(
        categoria,
        precio_base,
        categoria_objetivo,
        umbral
    )

    print("Producto:", nombre)
    print("Categoría:", categoria)
    print("Precio base: $", precio_base)
    print("Precio final: $", precio_final)
    print("-----------------------------")