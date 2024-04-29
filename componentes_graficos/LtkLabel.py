from customtkinter import CTkLabel
class LtkLabel(CTkLabel):
    def __init__(self, master, texto='LtkLabel'):
        super().__init__(master)
        self.configure(font=('Poppins', 12, "bold"), text=texto)

    def cambiar_texto(self, texto):
        self.configure(text=texto)

