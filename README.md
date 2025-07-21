# Parser de Clientes

Este script en Python permite extraer datos relevantes (nombre, número de teléfono y correo electrónico) desde un archivo de texto desestructurado que contiene registros de clientes con información adicional irrelevante. El objetivo es filtrar únicamente los campos útiles y almacenarlos en un archivo CSV limpio y estructurado.

## ¿Qué hace este script?

1. Lee un archivo de texto línea por línea.
2. Utiliza expresiones regulares para identificar:
   - Nombre completo (nombre y apellido)
   - Número de teléfono (formato flexible)
   - Dirección de correo electrónico
3. Filtra las líneas que contienen los tres campos correctamente formateados.
4. Escribe los resultados válidos en un archivo CSV de salida.

## Estructura del proyecto

- `datos_mega_aleatorios.txt`: archivo de entrada con miles de líneas de datos desestructurados (datos ficticios).
- `clientes_filtrados.csv`: archivo de salida generado con los registros limpios.
- `parser_clientes.py`: script principal que realiza todo el procesamiento.

## Uso

1. Coloca el archivo de entrada (`datos_mega_aleatorios.txt`) en el mismo directorio que el script.
2. Ejecuta el script:

```bash
python parser_clientes.py
```
3. Al finalizar, se generará el archivo clientes_filtrados.csv con los resultados.

## Requisitos
Este script utiliza solamente bibliotecas estándar de Python, por lo tanto no requiere instalación de dependencias externas.

Requiere:

Python 3.6 o superior

## Notas
- El nombre se asume como una combinación de dos palabras (nombre y apellido).

- Los números de teléfono pueden tener formato libre, con o sin guiones o espacios.

- Los emails se extraen con una expresión regular simple y común.

- Las líneas incompletas (con campos faltantes) se descartan automáticamente.

## Licencia

Este proyecto se ha desarrollado con fines educativos con el objetivo de aprender expresiones regulares, manipulación de archivos y procesamiento de texto con Python
