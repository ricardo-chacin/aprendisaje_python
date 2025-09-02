# Función genérica para solicitar y validar datos
def solicitar_dato(mensaje, validacion, error="❌ Entrada inválida. Inténtalo de nuevo."):
    while True:
        entrada = input(mensaje).strip().lower()
        if validacion(entrada):
            return entrada
        print(error)

# Validaciones específicas
def validar_edad(valor):
    return valor.isdigit() and 18 <= int(valor) <= 65

def validar_opcion_si_no(valor):
    return valor in ["si", "no"]

def validar_salud(valor):
    return valor in ["bien", "regular", "mal"]

def seleccionar_herramientas(lista):
    print("Selecciona las herramientas que vas a usar (número):")
    for i, herramienta in enumerate(lista, 1):
        print(f"{i}. {herramienta}")
    
    seleccion = input("Escribe los números separados por comas (ejemplo: 1,3): ").strip()
    try:
        indices = [int(num.strip()) - 1 for num in seleccion.split(",")]
        seleccionadas = [lista[i] for i in indices if 0 <= i < len(lista)]
        return seleccionadas if seleccionadas else None
    except ValueError:
        return None

# Programa principal
def evaluar_actividad():
    edad = solicitar_dato("Ingrese su edad: ", validar_edad)
    estado_salud = solicitar_dato("¿Cómo se siente hoy? (bien / regular / mal): ", validar_salud)
    epp = solicitar_dato("¿Cuenta con los EPPS adecuados y verificados? (si/no): ", validar_opcion_si_no)
    clima = solicitar_dato("¿El estado del clima es favorable? (si/no): ", validar_opcion_si_no)
    herramientas = solicitar_dato("¿Se van a usar herramientas eléctricas? (si/no): ", validar_opcion_si_no)

    edad = int(edad)

    if edad < 18:
        print("🚫 No cumples con la edad mínima para esta actividad.")
    elif estado_salud in ["mal", "regular"]:
        print("🚫 Tu estado de salud no es favorable.")
    elif epp != "si":
        print("🚫 Los EPPs no cumplen con los estándares requeridos.")
    elif clima != "si":
        print("🚫 El clima no permite realizar la actividad.")
    elif herramientas == "si":
        lista_herramientas = ["taladro", "pulidora", "máquina de soldar"]
        seleccionadas = seleccionar_herramientas(lista_herramientas)
        if seleccionadas:
            print("✅ Actividad autorizada. Herramientas declaradas:", ", ".join(seleccionadas))
        else:
            print("🚫 No se seleccionaron herramientas válidas.")
    else:
        print("✅ Actividad autorizada sin herramientas eléctricas.")

# Ejecutar
evaluar_actividad()