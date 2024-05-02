Para obtener la ruta del directorio actual del archivo y luego unirlo con el nombre de un archivo de configuración en Python, puedes utilizar el siguiente código:



```python
import os

# Obtiene la ruta del directorio del archivo actual
dir_path = os.path.dirname(os.path.abspath(__file__))

# Une la ruta del directorio con el nombre del archivo de configuración
config_path = os.path.join(dir_path, r'configuraciones\configuracion_dentro_comercial.json')

print(config_path)
```

- ```s.path.abspath(__file__):``` Devuelve la ruta absoluta del archivo actual.
- ```os.path.dirname():``` Devuelve la parte del directorio de la ruta proporcionada.
- ```os.path.join():``` Une las partes de una ruta usando el separador del sistema operativo, en este caso, une la ruta del directorio con el nombre del archivo de configuración.

- El prefijo ```r``` antes de la cadena de la ruta sirve para interpretarla como una "cadena sin procesar" (raw string), lo que significa que los caracteres de escape como \n o \t no serán interpretados, útil para las rutas de archivos en Windows donde \ es un carácter de escape.  


Cualquier duda o comentario, pregunteme o pueden preguntar a chat. 
