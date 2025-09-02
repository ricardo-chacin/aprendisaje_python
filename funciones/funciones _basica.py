def contar_vocales(palabra):
    vocales = "aeiouAEIOU"
    contador = 0
    for letra in palabra: 
        if letra in vocales: 
            contador +=1
    return contador
palabra = input ("ingrese la palabra")
print (f"la palabra {palabra} tiene {contar_vocales(palabra)} vocales")