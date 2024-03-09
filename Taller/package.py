class Package:
    """
    Clase para representar un paquete.
    """

    def __init__(self, package_id, description, weight, grams_price, quota, sender):
        """
        Inicializa una instancia de la clase Package.

        Args:
            package_id (int): ID del paquete.
            description (str): Descripción del paquete.
            weight (float): Peso del paquete en kilogramos.
            grams_price (float): Precio por gramo del paquete.
            quota (float): Cuota del paquete.
            sender (str): Remitente del paquete.
        """
        self.id = package_id
        self.description = description
        self.weight = weight
        self.grams_price = grams_price
        self.quota = quota
        self.sender = sender


class StandardPackage(Package):
    """
    Clase para representar un paquete estándar, que hereda de la clase Package.
    """

    def __init__(self, package_id, description, weight, grams_price, quota, sender):
        """
        Inicializa una instancia de la clase StandardPackage.

        Args:
            package_id (int): ID del paquete.
            description (str): Descripción del paquete.
            weight (float): Peso del paquete en kilogramos.
            grams_price (float): Precio por gramo del paquete.
            quota (float): Cuota del paquete.
            sender (str): Remitente del paquete.
        """
        super().__init__(package_id, description, weight, grams_price, quota, sender)
