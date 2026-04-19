from data.dao_salle import DataSalle

class ServiceSalle:

    def __init__(self):
        self.dao = DataSalle()

    def ajouter_salle(self, salle):
        if not salle.code or not salle.description or not salle.categorie:
            return False, "Champs manquants"

        if salle.capacite < 1:
            return False, "Capacité invalide"

        self.dao.insert_salle(salle)
        return True, "Salle ajoutée"

    def recuperer_salles(self):
        return self.dao.get_salles()