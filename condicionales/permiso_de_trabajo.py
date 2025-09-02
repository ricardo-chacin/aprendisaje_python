# verificacion para permiso de trabajo 

edad = int(input("ingrese su edad:"))
while True:
    estado_de_salud = input("¿Cómo se siente hoy? (bien / regular / mal): ").strip().lower()
    if estado_de_salud in ["bien", "regular", "mal"]:
        break
    else:
        print("Opción inválida. Por favor ingrese: bien, regular o mal.")
                             
while True:
        verificación_de_epp = input("¿Cuenta con los EPPS adecuados y los verifico? (si/no): ").strip().lower()
        if verificación_de_epp in ["si", "no"]:
            break   
        else:
            print("Opción inválida. Por favor ingrese: si o no.")   

while True: 
    estado_del_clima = input("¿El estado del clima es favorable? (si/no): ").strip().lower()
    if estado_del_clima in ["si", "no"]:
       break
    else:
        print("Opción inválida. Por favor ingrese: si o no.")      

while True:
    herramientas = input("¿Se va a hacer uso de herramientas eléctricas? (si/no): ").strip().lower()
    if herramientas in ["si", "no"]:
      break
    else:
     print("Opción inválida. Por favor ingrese: si o no.")   

# verificacion de las herramientas 

lista = ["taladro"," pulidora","maquina de soldar"]

if edad < 18:
    print("no cumples con la edad minima para la ejecución de esta activid")

elif estado_de_salud in ["mal","regular"]:
    print("lo siento tu estado de salud no es favorable ")

elif verificación_de_epp != "si":
    print("los EPPS no cumplen con los estandandares requeridos")

elif estado_del_clima != "si":
    print("el estado del clima no permite realizar la actividad")

elif herramientas.startswith("si"):
    print("de ser ser afirmativo cial es ?")
    
    for i, herramienta in enumerate(lista, 1):
        print(f"{i}. {herramienta}")

    seleccion = input("Escriba los números separados por comas (ejemplo: 1,3): ").strip()
    
    try:
        indices = [int(num.strip()) - 1 for num in seleccion.split(",")]
        herramientas_utilizadas = [lista[i] for i in indices if 0 <= i < len(lista)]

        if not herramientas_utilizadas:
            print(" No se seleccionaron herramientas válidas.")
        else:
            print(" Actividad autorizada. Herramientas declaradas:", ", ".join(herramientas_utilizadas))

    except ValueError:
        print(" Entrada inválida. Por favor ingrese números válidos separados por comas.")
else :
    print("actividad autotizada")
