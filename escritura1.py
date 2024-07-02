#crear archivo, w es permiso de escritura
#Las comillas al inicio y 3 al final del texto representan un texto
#con saltos de línea
datos = """Puro, Chile, es tu cielo azulado,
puras brisas te cruzan también,
y tu campo de flores bordado
es la copia feliz del Edén.
Majestuosa es la blanca montaña
que te dio por baluarte el Señor,
que te dio por baluarte el Señor,
Y ese mar que tranquilo te baña
te promete futuro esplendor.
Y ese mar que tranquilo te baña
te promete futuro esplendor.

Dulce Patria, recibe los votos
Con que Chile en tus aras juró
Que o la tumba serás de los libres
O el asilo contra la opresión
Que o la tumba serás de los libres
O el asilo contra la opresión
Que o la tumba serás de los libres
O el asilo contra la opresión.
O el asilo contra la opresión.
O el asilo contra la opresión. 
"""
with open('archivo.txt', 'w') as archivo:
	archivo.write(datos)
    
# a) 
# crear un archivo "datos.txt"
# solicitar ingreso de rut, nombre y edad
# agregar al archivo
# formato:
# rut : rut_capturado 
# nombre : nombre_capturado
# edad : edad_capturada


# b)	
# Solicitar el nombre del archivo a crear
# añadir los datos anteriores al nuevo archivo


# c) 
# armar el nombre del archivo nuevo
# a partir del nombre y edad ingresadas
# el formato: nombre_edad.txt

rut_capturado=input("INGRESE SU RUT:	")
nombre_capturado=input("INGRESE SU NOMBRE:	")											#CREACION DE DATOS DE UN ARCHIVO 
edad_capturado=input("INGRESE SU EDAD:	")
datos_Ingresados=rut_capturado, nombre_capturado, edad_capturado

nombre_Archivo_A_Crear=input("INGRESE EL NOMBRE DEL ARCHIVO A CREAR:	")
with open(nombre_Archivo_A_Crear, "w") as archivo_Nuevo:								#CREACION DE ARCHVO Y ASIGNACION DE NOMBRE
    archivo_Nuevo.write(datos_Ingresados)

formato=nombre_capturado, edad_capturado