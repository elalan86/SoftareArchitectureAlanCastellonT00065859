class Location:
    """
    Clase que representa una ubicación.

    Attributes:
        country (str): País de la ubicación.
        department (str): Departamento de la ubicación.
        city (str): Ciudad de la ubicación.
        street (str): Calle de la ubicación.
        career (str): Carrera de la ubicación.
        postal_code (str): Código postal de la ubicación.
    """

    def __init__(self, country, department, city, street, career, postal_code):
        """
        Inicializa una nueva instancia de Location.

        Args:
            country (str): País de la ubicación.
            department (str): Departamento de la ubicación.
            city (str): Ciudad de la ubicación.
            street (str): Calle de la ubicación.
            career (str): Carrera de la ubicación.
            postal_code (str): Código postal de la ubicación.
        """
        self.country = country
        self.department = department
        self.city = city
        self.street = street
        self.career = career
        self.postal_code = postal_code

    def register_location(self, country, department, city, street, career, postal_code):
        """
        Registra una nueva ubicación.

        Args:
            country (str): País de la ubicación.
            department (str): Departamento de la ubicación.
            city (str): Ciudad de la ubicación.
            street (str): Calle de la ubicación.
            career (str): Carrera de la ubicación.
            postal_code (str): Código postal de la ubicación.
        """
        self.country = country
        self.department = department
        self.city = city
        self.street = street
        self.career = career
        self.postal_code = postal_code
        print("Ubicación registrada exitosamente.")

    def change_location(self, country, department, city, street, career, postal_code):
        """
        Cambia la ubicación actual.

        Args:
            country (str): País de la ubicación.
            department (str): Departamento de la ubicación.
            city (str): Ciudad de la ubicación.
            street (str): Calle de la ubicación.
            career (str): Carrera de la ubicación.
            postal_code (str): Código postal de la ubicación.
        """
        self.country = country
        self.department = department
        self.city = city
        self.street = street
        self.career = career
        self.postal_code = postal_code
        print("Ubicación cambiada exitosamente.")

    def show_location(self):
        """Muestra los detalles de la ubicación."""
        print("\nDetalles de la ubicación:")
        print("País:", self.country)
        print("Departamento:", self.department)
        print("Ciudad:", self.city)
        print("Calle:", self.street)
        print("Carrera:", self.career)
        print("Código postal:", self.postal_code)
