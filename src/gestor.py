# gestor.py
import json
from src.contacto import Contacto

class GestorContactos:
    """
    Clase para administrar varios contactos en el sistema.
    Mantiene una lista de contactos y permite CRUD con persistencia en JSON.
    """

    def __init__(self, archivo="contactos.json"):
        self.archivo = archivo
        self.contactos = self.cargar_contactos()

    def agregar_contacto(self, contacto):
        """
        Agrega un nuevo contacto si no existe duplicado.
        """
        # Revisar duplicados por teléfono o correo
        for c in self.contactos:
            if c.telefono == contacto.telefono:
                print(f"⚠️ Ya existe un contacto con el teléfono {contacto.telefono}")
                return False


        self.contactos.append(contacto)
        self.guardar_contactos()
        return True

    def listar_contactos(self):
        """
        Imprime todos los contactos almacenados.
        """
        if not self.contactos:
            print("No hay contactos registrados.")
        for c in self.contactos:
            print(c)

    def buscar_contacto(self, texto):
        """
        Busca contactos por nombre o teléfono (no distingue mayúsculas).
        Retorna una lista de contactos encontrados.
        """
        return [c for c in self.contactos 
                if texto.lower() in c.nombre.lower() or texto in c.telefono]

    def eliminar_contacto(self, contacto):
        """
        Elimina un contacto específico y guarda los cambios.
        """
        if contacto in self.contactos:
            self.contactos.remove(contacto)
            self.guardar_contactos()
            return True
        return False

    def guardar_contactos(self):
        """
        Guarda todos los contactos en el archivo JSON.
        """
        data = [c.to_dict() for c in self.contactos]
        with open(self.archivo, "w") as f:
            json.dump(data, f, indent=4)

    def cargar_contactos(self):
        """
        Carga los contactos desde el archivo JSON al iniciar el programa.
        """
        try:
            with open(self.archivo, "r") as f:
                data = json.load(f)
                return [Contacto(**d) for d in data]
        except FileNotFoundError:
            return []
