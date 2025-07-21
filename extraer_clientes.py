import csv 
import re

# Versión más flexible:
nombre_regex = r"([A-Za-zÁÉÍÓÚÑÜáéíóúñü]+ [A-Za-zÁÉÍÓÚÑÜáéíóúñü]+)"
telefono_regex = r"(\(?\d{3}\)?[-\s]?\d{3}[-\s]?\d{4})" 
email_regex = r"(\b[\w.-]+@[\w.-]+\.\w{2,}\b)" 


def extraer_datos(linea):
    nombre= re.search(nombre_regex,linea)
    telefono=re.search(telefono_regex,linea)
    email=re.search(email_regex,linea, re.IGNORECASE)

    return (

        nombre.group(1) if nombre else None,
        telefono.group(1) if telefono else None,
        email.group(1) if email else None
    )

def procesar_archivo(archivo_entrada):
    #lee archivo y devuelve datos validos
    datos_validos=[]

    with open(archivo_entrada, 'r', encoding='utf-8') as f:
        for linea in f:
            nombre, telefono, email = extraer_datos(linea)
            if nombre and telefono and email:
                datos_validos.append([nombre, telefono, email])
    return datos_validos

def guardar_csv(archivo_salida, datos):
    with open(archivo_salida, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Nombre", "Teléfono", "Email"])
        writer.writerows(datos)

if __name__=="__main__":
    ARCHIVO_ENTRADA="datos_mega_aleatorios.txt"
    ARCHIVO_SALIDA= "clientes_filtrados.csv"

    datos=procesar_archivo(ARCHIVO_ENTRADA)
    guardar_csv(ARCHIVO_SALIDA, datos)

    print(f"Proceso completado. Datos guardados en {ARCHIVO_SALIDA}")