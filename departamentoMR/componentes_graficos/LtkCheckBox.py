from customtkinter import CTkCheckBox

class LtkCheckBoxFill(CTkCheckBox):
    def __init__(self, master, texto, variable):
        super().__init__(master)

        self.configure(
            text=texto,
            variable=variable,
            corner_radius=5,
            fg_color="#4A9D63",
            text_color="#0f2417",
            border_color="#4A9D63",
            font=("Poppins", 12, "bold"),
            hover=True,
            hover_color="#3B8752"
        )

