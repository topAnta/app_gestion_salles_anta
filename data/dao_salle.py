import mysql.connector
import json
from models.salle import Salle

class DataSalle:

    def get_connection(self):
        with open("Data/config.json") as f:
            config = json.load(f)
        return mysql.connector.connect(**config)

    def insert_salle(self, salle):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO salle VALUES (%s, %s, %s, %s)",
            (salle.code, salle.description, salle.categorie, salle.capacite)
        )
        conn.commit()
        conn.close()

    def get_salles(self):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM salle")
        rows = cursor.fetchall()
        conn.close()

        return [Salle(*row) for row in rows]