from customtkinter import CTkComboBox

class LtkComboBoxFill(CTkComboBox):
    """Representa un ComboBox con un diseño personalizado."""

    def __init__(self, master, valores):
        """Inicializa el ComboBox con las configuraciones dadas."""
        super().__init__(master)

        # Configura el ComboBox
        self.configure(
            values=valores,
            corner_radius=5,
            fg_color="#cae8d2",
            text_color="#0f2417",
            border_color="#e4f4e8",
            border_width=2,
            dropdown_fg_color="#cae8d2",
            dropdown_font=("Poppins", 12, "bold"),
            dropdown_text_color="#0f2417",
            dropdown_hover_color="#3B8752",
            button_color="#39804e",
            button_hover_color="#2f6640",
            font=("Poppins", 12, "bold"),
        )
        self.set(valores[0])

    def disable(self):
        """Desactiva el ComboBox y cambia su apariencia a desactivado."""
        self.configure(
            state="disabled",
            fg_color="#E4F4E8",
            text_color="#6EBA85",
            border_color="#E4F4E8",

        )

    def enable(self):
        """Activa el ComboBox y cambia su apariencia a activado."""
        self.configure(
            state="readonly",
            fg_color="#4A9D63",
            text_color="#0f2417",
            border_color="#4A9D63",

        )

class LtkComboBoxLine(CTkComboBox):
    """Representa un ComboBox con un borde."""

    def __init__(self, master, valores):
        """Inicializa el ComboBox con las configuraciones dadas."""
        super().__init__(master)

        # Configura el ComboBox
        self.configure(
            values=valores,
            corner_radius=5,
            fg_color="#FFFFFF",
            text_color="#23442e",
            border_color="#4A9D63",
            dropdown_fg_color="#FFFFFF",
            dropdown_font=("Poppins", 12, "bold"),
            dropdown_text_color="#23442e",
            dropdown_hover_color="#3B8752",
            border_width=2,
            button_color="#4A9D63",
            button_hover_color="#3B8752",
            font=("Poppins", 12, "bold"),
        )
        self.set(valores[0])

    def disable(self):
        """Desactiva el ComboBox y cambia su apariencia a desactivado."""
        self.configure(
            state="disabled",
            fg_color="transparent",
            text_color="#6EBA85",
            border_color="#E4F4E8",
        )

    def enable(self):
        """Activa el ComboBox y cambia su apariencia a activado."""
        self.configure(
            state="readonly",
            fg_color="transparent",
            text_color="#4A9D63",
            border_color="#4A9D63",
        )


