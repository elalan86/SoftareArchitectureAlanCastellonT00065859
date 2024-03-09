class Customer:
    """
    Clase que representa a un cliente.

    Attributes:
        id (int): Identificador único del cliente.
        name (str): Nombre del cliente.
        email (str): Correo electrónico del cliente.
    """

    def __init__(self, id, name, email):
        """
        Inicializa un nuevo objeto Customer.

        Args:
            id (int): Identificador único del cliente.
            name (str): Nombre del cliente.
            email (str): Correo electrónico del cliente.
        """
        self.id = id
        self.name = name
        self.email = email

    def register_customer(self, name, email):
        """
        Registra un nuevo cliente con el nombre y correo electrónico especificados.

        Args:
            name (str): Nombre del cliente.
            email (str): Correo electrónico del cliente.
        """
        self.name = name
        self.email = email
        print("Cliente registrado exitosamente.")

    def show_customer_details(self):
        """
        Muestra los detalles del cliente.
        """
        print("\nDetalles del cliente:")
        print("ID del cliente:", self.id)
        print("Nombre del cliente:", self.name)
        print("Correo electrónico del cliente:", self.email)
