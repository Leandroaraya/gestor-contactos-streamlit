# contacto.py

class Contacto:
    """
    Clase que representa un contacto individual en el sistema de gestión de contactos.
    """

    def __init__(self, nombre, telefono, correo, direccion):
        """
        Inicializa un nuevo contacto con los atributos proporcionados.
        """
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion

    def __str__(self):
        """
        Retorna la información del contacto en un formato legible.
        """
        return f"{self.nombre} | {self.telefono} | {self.correo} | {self.direccion}"

    def actualizar(self, nombre=None, telefono=None, correo=None, direccion=None):
        """
        Permite actualizar los atributos del contacto.
        Solo actualiza los campos que se proporcionen.
        """
        if nombre is not None and nombre != "":
            self.nombre = nombre
        if telefono is not None and telefono != "":
            self.telefono = telefono
        if correo is not None and correo != "":
            self.correo = correo
        if direccion is not None and direccion != "":
            self.direccion = direccion

    def to_dict(self):
        """
        Convierte el contacto a un diccionario para guardarlo en JSON.
        """
        return {
            "nombre": self.nombre,
            "telefono": self.telefono,
            "correo": self.correo,
            "direccion": self.direccion
        }
