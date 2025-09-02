#creacion de tipos de datos de un diccionadrio 

maquina_empacadora = {
    "marca": "Acmi",
    "sensores de proximidad": 5,
    "motores": 8,
    "palometas": 32,
    "transportes": 12,
    "dispositivos de seguridad": 1.5
    
}

#Agregar un dato adicional a la variable 

maquina_empacadora["numero de cabezales"] = 4

#imprime los datos que se le solicitamos de la varable 

print("nombre", maquina_empacadora["marca"])
print("sensores", maquina_empacadora["sensores de proximidad"])
print("numero de motores", maquina_empacadora["motores"])
print("numero de palometas", maquina_empacadora["palometas"])
print("numero de transportes", maquina_empacadora["transportes"])
print("numero de dispositivos SAM", maquina_empacadora["dispositivos de seguridad"])
print("cantidad de cabezales", maquina_empacadora["numero de cabezales"])