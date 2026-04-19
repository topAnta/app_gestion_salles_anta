import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle

class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()
        self.service = ServiceSalle()

        self.title("Gestion des salles")

        self.entry_code = ctk.CTkEntry(self)
        self.entry_code.pack()

        self.entry_desc = ctk.CTkEntry(self)
        self.entry_desc.pack()

        self.entry_cat = ctk.CTkEntry(self)
        self.entry_cat.pack()

        self.entry_cap = ctk.CTkEntry(self)
        self.entry_cap.pack()

        btn = ctk.CTkButton(self, text="Ajouter", command=self.ajouter)
        btn.pack()

    def ajouter(self):
        salle = Salle(
            self.entry_code.get(),
            self.entry_desc.get(),
            self.entry_cat.get(),
            int(self.entry_cap.get())
        )

        self.service.ajouter_salle(salle)

        
    def ajouter(self):
    try:
        cap = int(self.entry_cap.get())
    except:
        print("Capacité invalide")
        return

    salle = Salle(
        self.entry_code.get(),
        self.entry_desc.get(),
        self.entry_cat.get(),
        cap
    )

    self.service.ajouter_salle(salle)
    print("Salle ajoutée")

    