import json
Lista = None
with open('D:\MIIGUEL ROSALES\Documentos\ISC - ITSZaS\Cuarto Semestre\SIMULACION\PROYECTO\centro-comercial\departamentoMR\gimnasio.json') as file:
    data = json.load(file)
    lista = data

cantidad_recepcionistas = lista['cantidad_recepcionistas']
cantidad_personal_limpieza = lista['cantidad_personal_limpieza']
cantidad_gerentes = lista['cantidad_gerentes']
cantidad_entrenadores = lista['cantidad_entrenadores']
cantidad_personal_tecnico = lista['cantidad_personal_tecnico']
sueldo_mensual_gerente = lista['sueldo_mensual_gerente']
sueldo_mensual_entrenador = lista['sueldo_mensual_entrenador']
sueldo_mensual_recepcionista = lista['sueldo_mensual_recepcionista']
sueldo_mensual_personal_limpieza = lista['sueldo_mensual_personal_limpieza']
sueldo_mensual_personal_tecnico = lista['sueldo_mensual_personal_tecnico']
horario_apertura = lista['horario_apertura']
horario_cierre = lista['horario_cierre']
tiempo_sesion_usuario = lista['tiempo_sesion_usuarios']
tiempo_uso_maquina = lista['tiempo_uso_maquina']
tiempo_uso_baño = lista['tiempo_uso_baño']
tiempo_uso_vestidor = lista['tiempo_uso_vestidor']
capacidad_gym = lista['capacidad_gym']
cantidad_mujeres = lista['cantidad_mujeres']
cantidad_hombres = lista['cantidad_hombres']
cobro_mensual_usuarios = lista['cobro_mensual_usuario']
cantidad_maquinas = lista['cantidad_maquinas']
cantidad_maquinas_cardio = lista['cantidad_maquinas_cardio']
cantidad_maquinas_musculacion = lista['cantidad_maquinas_musculacion']
pago_mensual_luz = lista['pago_mensual_luz']
pago_mensual_agua = lista['pago_mensual_agua']
pago_mensual_internet = lista['pago_mensual_internet']
pago_mensual_spotify = lista['pago_mensual_spotify']
pago_mensual_renta_local = lista['pago_mensual_renta_local']
cantidad_baños = lista['cantidad_baños']
cantidad_baños_mujeres = lista['cantidad_baños_mujeres']
cantidad_baños_hombres = lista['cantidad_baños_hombres']
cantidad_vestidores = lista['cantidad_vestidores']
cantidad_vestidores_mujeres = lista['cantidad_vestidores_mujeres']
cantidad_vestidores_hombres = lista['cantidad_vestidores_hombres']
temporada_regular = lista['temporada_regular']
temporada_alta = lista['temporada_alta']
temporada_baja = lista['temporada_baja']
atencion= lista['atencion']
descompostura= lista['descompostura']


print((sueldo_mensual_gerente * cantidad_gerentes) * 12) 

