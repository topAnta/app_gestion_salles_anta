import customtkinter as ctk
from services.services_salle import ServiceSalle
from models.salle import Salle
from tkinter import ttk


class ViewSalle(ctk.CTk):

    def __init__(self):
        super().__init__()

        self.service = ServiceSalle()
        self.title("Gestion des salles")

        # ENTRY
        self.entry_code = ctk.CTkEntry(self)
        self.entry_code.pack()

        self.entry_desc = ctk.CTkEntry(self)
        self.entry_desc.pack()

        self.entry_cat = ctk.CTkEntry(self)
        self.entry_cat.pack()

        self.entry_cap = ctk.CTkEntry(self)
        self.entry_cap.pack()

        # BUTTONS
        ctk.CTkButton(self, text="Ajouter", command=self.ajouter).pack()
        ctk.CTkButton(self, text="Supprimer", command=self.supprimer).pack()
        ctk.CTkButton(self, text="Rechercher", command=self.rechercher).pack()

        # TABLE
        self.cadreList = ctk.CTkFrame(self)
        self.cadreList.pack(pady=10)

        self.treeList = ttk.Treeview(
            self.cadreList,
            columns=("code", "description", "categorie", "capacite"),
            show="headings"
        )

        self.treeList.heading("code", text="CODE")
        self.treeList.heading("description", text="Description")
        self.treeList.heading("categorie", text="Catégorie")
        self.treeList.heading("capacite", text="Capacité")

        self.treeList.pack()

        self.lister_salles()

    # ---------------- AJOUTER ----------------
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
        self.lister_salles()
        print("Salle ajoutée")

    # ---------------- SUPPRIMER ----------------
    def supprimer(self):
        code = self.entry_code.get()
        self.service.supprimer_salle(code)
        self.lister_salles()
        print("Salle supprimée")

    # ---------------- RECHERCHER ----------------
    def rechercher(self):
        code = self.entry_code.get()

        salle = self.service.rechercher_salle(code)
        self.lister_salles()

        if salle:
            self.entry_desc.delete(0, "end")
            self.entry_cat.delete(0, "end")
            self.entry_cap.delete(0, "end")

            self.entry_desc.insert(0, salle.description)
            self.entry_cat.insert(0, salle.categorie)
            self.entry_cap.insert(0, salle.capacite)

            print("Salle trouvée")
        else:
            print("Salle non trouvée")

    # ---------------- LISTE ----------------
    def lister_salles(self):
        self.treeList.delete(*self.treeList.get_children())

        liste = self.service.recuperer_salles()

        for s in liste:
            self.treeList.insert("", "end", values=(
                s.code,
                s.description,
                s.categorie,
                s.capacite
            ))