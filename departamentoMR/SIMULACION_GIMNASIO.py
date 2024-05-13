import json

with open('D:\MIIGUEL ROSALES\Documentos\ISC - ITSZaS\Cuarto Semestre\SIMULACION\PROYECTO\centro-comercial\departamentoMR\gimnasio.json') as file:
    data = json.load(file)

for key, value in data.items(): 
    print(key, value)