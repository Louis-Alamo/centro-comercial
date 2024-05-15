import json

def cargar_datos():
    with open('D:\\MIIGUEL ROSALES\\Documentos\\ISC - ITSZaS\\Cuarto Semestre\\SIMULACION\\PROYECTO\\centro-comercial\\departamentoMR\\gimnasio.json', 'r') as file:
        return json.load(file)

def mostrar_datos_gimnasio():
    datos = cargar_datos()
    print("--- Datos del Gimnasio ---")
    for key, value in datos.items():
        print(f"{key}: {value}")


mostrar_datos_gimnasio()
