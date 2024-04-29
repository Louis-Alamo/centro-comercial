from customtkinter import CTkEntry

class LtkEntryFill(CTkEntry):

    def __init__(self, master, placeholder = "LtkEntryFill"):
        super().__init__(master)
        self.configure(
            placeholder_text=placeholder,
            placeholder_text_color="#A0D5AF",
            corner_radius=5,
            fg_color="#E4F4E8",
            text_color="#000000",
            border_color="#6EBA85",
            font=("Poppins", 12, "bold"),
        )

    def get_text(self):
        return self.get()





class LtkEntryLine(CTkEntry):

    def __init__(self, master, placeholder = "LtkEntryLine"):
        super().__init__(master)
        self.configure(
            placeholder_text=placeholder,
            placeholder_text_color="#A0D5AF",
            corner_radius=5,
            fg_color="#FFFFFF",
            text_color="#000000",
            border_color="#6EBA85",
            font=("Poppins", 12, "bold"),
        )

    def get_text(self):
        return self.get()


class LtkEntryFillImage(CTkEntry):
    pass

class LtkEntryLineImage(CTkEntry):
    pass

class LtkEntryFillPassword(CTkEntry):
    pass

class LtkEntryLinePassword(CTkEntry):
    pass

