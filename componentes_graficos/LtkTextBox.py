from customtkinter import CTkTextbox

class LtkTextboxFill(CTkTextbox):
    def __init__(self, master):
        super().__init__(master)

        self.configure(
            corner_radius=5,
            fg_color="#E4F4E8",
            border_color="#6EBA85",
            border_width=2,
            font=("Poppins", 12),

        )

    def get_text(self):
        return self.get("1.0", "end-1c")

    def insertar_texto(self, texto):
        self.limpiar()
        self.insert("end", texto)

    def insertar_texto_final(self, texto):
        self.insert("end", texto)

    def insertar_lista(self, lista, salto_linea=False):
        self.limpiar()
        self.insertar_lista_final(lista, salto_linea)

    def insertar_lista_final(self, lista, salto_linea=False):
        for item in lista:
            self.insert("end", item)
            if salto_linea:
                self.insert("end", "\n")



    def limpiar(self):
        self.delete("1.0", "end")
