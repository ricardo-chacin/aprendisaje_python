def calcular_precio_final(precio):
    descuento = 10
    precio_final = precio - (precio * descuento /100)
    return precio_final

precio = float(input("ingrese el presio del producto : "))


print(f"precio final con descuento es de {calcular_precio_final(precio)} ")