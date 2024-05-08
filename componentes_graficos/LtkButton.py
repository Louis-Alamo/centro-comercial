from customtkinter import CTkButton
from tkinter import Tk

class LtkButtonFill(CTkButton):
    """Representa un botón con un fondo lleno."""

    def __init__(self, master, funcion, nombre_boton = "LtkButtonFill"):
        """Inicializa el botón con las configuraciones dadas."""
        super().__init__(master)

        # Configura el botón
        self.configure(
            text=nombre_boton,
            command=funcion,
            corner_radius=5,
            fg_color="#4A9D63",
            text_color="#FFFFFF",
            border_color="#4A9D63",
            font=("Poppins", 12, "bold"),
            border_spacing=5,
            hover=True,
            hover_color="#3B8752"
        )

    def disable(self):
        """Desactiva el botón y cambia su apariencia a desactivado."""
        self.configure(
            state="disabled",
            fg_color="#E4F4E8",
            text_color="#6EBA85",
            border_color="#E4F4E8",
            hover=False
        )

    def enable(self):
        """Activa el botón y cambia su apariencia a activado."""
        self.configure(
            state="normal",
            fg_color="#4A9D63",
            text_color="#FFFFFF",
            border_color="#4A9D63",
            hover=True
        )

class LtkButtonLine(CTkButton):
    """Representa un botón con un borde."""

    def __init__(self, master, funcion, nombre_boton = "LtkButtonLine"):
        """Inicializa el botón con las configuraciones dadas."""
        super().__init__(master)

        # Configura el botón
        self.configure(
            text=nombre_boton,
            command=funcion,
            corner_radius=5,
            fg_color="transparent",
            text_color="#4A9D63",
            border_color="#4A9D63",
            border_width=2,
            font=("Poppins", 12, "bold"),
            border_spacing=5,
            hover=True,
        )

        # Vincula los eventos de pasar el cursor por encima y fuera del botón
        self.bind("<Enter>", self.hover_on)
        self.bind("<Leave>", self.hover_off)

    def hover_on(self, event=None):
        """Cambia la apariencia del botón cuando el cursor pasa por encima."""
        self.configure(
            fg_color="transparent",
            text_color="#39804e",
            border_color="#39804e",
        )

    def hover_off(self, event=None):
        """Cambia la apariencia del botón cuando el cursor sale de encima."""
        self.configure(
            fg_color="transparent",
            text_color="#4A9D63",
            border_color="#4A9D63",
        )

    def disable(self):
        """Desactiva el botón y cambia su apariencia a desactivado."""
        self.configure(
            state="disabled",
            fg_color="transparent",
            text_color="#6EBA85",
            border_color="#6EBA85",
            hover=False
        )
        # Desvincula los eventos <Enter> y <Leave>
        self.unbind("<Enter>")
        self.unbind("<Leave>")

    def enable(self):
        """Activa el botón y cambia su apariencia a activado."""
        self.configure(
            state="normal",
            fg_color="transparent",
            text_color="#4A9D63",
            border_color="#4A9D63",
            hover=True
        )
        # Vuelve a vincular los eventos <Enter> y <Leave>
        self.bind("<Enter>", self.hover_on)
        self.bind("<Leave>", self.hover_off)

class LtkButtonTransparentBackground(CTkButton):

    def __init__(self, master, funcion, nombre_boton = "LtkButtonFill", not_border = False):
        super().__init__(master)

        self.configure(

            command=funcion,
            corner_radius=5,
            fg_color="transparent",
            text_color="#4A9D63",
            border_width=2,
            font=("Poppins", 12, "bold"),

            border_spacing=5,
            hover=False,
        )
        if not_border:
            self.configure(border_width=0)
        else:
            self.configure(border_color="#4A9D63")




# Las siguientes clases están vacías en tu código original, por lo que no he añadido comentarios
class LtkButtonFillImage(CTkButton):
    pass

class LtkButtonLineImage(CTkButton):
    pass


