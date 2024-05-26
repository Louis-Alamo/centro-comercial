from datetime import datetime, timedelta
from departamentoLG.excepciones.HoraExcepcion import HoraErrorExcepcion

class Hora:
    """
    Clase que representa una hora en formato de 12 horas y permite realizar operaciones de suma de tiempo.
    """
    def __init__(self, hora: str):
        """
        Inicializa una instancia de Hora.

        :param hora: Hora en formato de 12 horas (e.g., "02:30 PM")
        :raises HoraError: Si el formato de la hora es incorrecto.
        """
        self.formato_12h = "%I:%M %p"
        try:
            self.hora = datetime.strptime(hora, self.formato_12h)
        except ValueError:
            raise HoraErrorExcepcion(f"Formato de hora incorrecto: {hora}")

    def __str__(self):
        """
        Devuelve la hora como una cadena en formato de 12 horas.

        :return: Hora en formato de 12 horas (e.g., "02:30 PM")
        """
        return self.hora.strftime(self.formato_12h)

    def sumar_segundos(self, segundos: int):
        """
        Suma segundos a la hora actual.

        :param segundos: Número de segundos a sumar.
        """
        self.hora += timedelta(seconds=segundos)

    def sumar_minutos(self, minutos: int):
        """
        Suma minutos a la hora actual.

        :param minutos: Número de minutos a sumar.
        """
        self.hora += timedelta(minutes=minutos)

    def sumar_horas(self, horas: int):
        """
        Suma horas a la hora actual.

        :param horas: Número de horas a sumar.
        """
        self.hora += timedelta(hours=horas)

    def sumar_hora(self, otra_hora_str: str):
        """
        Suma otra hora a la hora actual.

        :param otra_hora_str: Hora en formato de 12 horas a sumar (e.g., "01:30 PM")
        :raises HoraError: Si el formato de la otra hora es incorrecto.
        """
        try:
            otra_hora = datetime.strptime(otra_hora_str, self.formato_12h)
        except ValueError:
            raise HoraErrorExcepcion(f"Formato de hora incorrecto: {otra_hora_str}")
        delta = timedelta(hours=otra_hora.hour, minutes=otra_hora.minute)
        self.hora += delta

    def get_hora(self):
        """
        Devuelve la hora actual como una cadena en formato de 12 horas.

        :return: Hora en formato de 12 horas (e.g., "02:30 PM")
        """
        return self.hora.strftime(self.formato_12h)

    def set_hora(self, hora_str: str):
        """
        Establece una nueva hora.

        :param hora_str: Nueva hora en formato de 12 horas (e.g., "02:30 PM")
        :raises HoraError: Si el formato de la nueva hora es incorrecto.
        """
        try:
            self.hora = datetime.strptime(hora_str, self.formato_12h)
        except ValueError:
            raise HoraErrorExcepcion(f"Formato de hora incorrecto: {hora_str}")

    def __lt__(self, other):
        """
        Compara si la hora actual es menor que otra hora.

        :param other: Otra instancia de Hora.
        :return: True si la hora actual es menor que otra, False en caso contrario.
        """
        return self.hora < other.hora

    def __le__(self, other):
        """
        Compara si la hora actual es menor o igual que otra hora.

        :param other: Otra instancia de Hora.
        :return: True si la hora actual es menor o igual que otra, False en caso contrario.
        """
        return self.hora <= other.hora

    def __gt__(self, other):
        """
        Compara si la hora actual es mayor que otra hora.

        :param other: Otra instancia de Hora.
        :return: True si la hora actual es mayor que otra, False en caso contrario.
        """
        return self.hora > other.hora

    def __ge__(self, other):
        """
        Compara si la hora actual es mayor o igual que otra hora.

        :param other: Otra instancia de Hora.
        :return: True si la hora actual es mayor o igual que otra, False en caso contrario.
        """
        return self.hora >= other.hora

    def __eq__(self, other):
        """
        Compara si la hora actual es igual a otra hora.

        :param other: Otra instancia de Hora.
        :return: True si la hora actual es igual a otra, False en caso contrario.
        """
        return self.hora == other.hora

    def __ne__(self, other):
        """
        Compara si la hora actual es diferente a otra hora.

        :param other: Otra instancia de Hora.
        :return: True si la hora actual es diferente a otra, False en caso contrario.
        """
        return self.hora != other.hora

    def copiar(self):
        return Hora(self.get_hora())


