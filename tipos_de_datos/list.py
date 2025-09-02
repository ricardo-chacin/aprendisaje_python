#listado de frutas 
vehiculos = ["renault","chevrolet","pygeot","mercedes","ferrari"]

#indica cual es el primer vehiculo de la lista 

primer_vehiculos = vehiculos[0]

#indica el ultimo vehicilo de la lista 
ultimo_vehiculos = vehiculos[4] 

#imprime los resultados 
print("listado de vehiculos", vehiculos)
print("primer vehiculo del listado", primer_vehiculos)
print("ultimo vehiculo del listado", ultimo_vehiculos)

#ordena alfabeticamente los vehiculos 
vehiculos.sort()

print(vehiculos)

#inserta un nuevo vehiculo
vehiculos.append("ford")

#imprime el nuevo vehiculo en la lista 
print(vehiculos)

#insertar un articulo en una posicion especifica 
vehiculos.insert(2,"BMW")

print(vehiculos)

#eliminar un articulo de la lista 
vehiculos.remove("pygeot")

print(vehiculos)
