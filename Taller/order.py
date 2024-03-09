class Order:
    """
    Clase para representar un pedido.
    """

    def __init__(self, order_id, package, is_paid, total_payment, receiver, sender, status, location):
        """
        Inicializa una instancia de la clase Order.

        Args:
            order_id (int): El ID del pedido.
            package (str): Descripción del paquete.
            is_paid (bool): Indica si el pedido está pagado.
            total_payment (float): Monto total del pago.
            receiver (str): Nombre del receptor.
            sender (str): Nombre del remitente.
            status (str): Estado del pedido.
            location (str): Ubicación del pedido.
        """
        self.id = order_id
        self.package = package
        self.is_paid = is_paid
        self.total_payment = total_payment
        self.receiver = receiver
        self.sender = sender
        self.status = status
        self.location = location

    def register_order(self, package, receiver, sender, status, location):
        """
        Registra un nuevo pedido con los detalles proporcionados.

        Args:
            package (str): Descripción del paquete.
            receiver (str): Nombre del receptor.
            sender (str): Nombre del remitente.
            status (str): Estado del pedido.
            location (str): Ubicación del pedido.
        """
        self.package = package
        self.is_paid = False  # Por defecto, el pedido no está pagado
        self.total_payment = 0  # El total del pago se establecerá posteriormente
        self.receiver = receiver
        self.sender = sender
        self.status = status
        self.location = location
        print("Pedido registrado exitosamente.")

    def show_order_details(self):
        """
        Muestra los detalles del pedido.
        """
        print("\nDetalles del pedido:")
        print("ID del pedido:", self.id)
        print("Paquete:", self.package)
        print("¿Está pagado?:", "Sí" if self.is_paid else "No")
        print("Total del pago:", self.total_payment)
        print("Receptor:", self.receiver)
        print("Remitente:", self.sender)
        print("Estado:", self.status)
        print("Ubicación:", self.location)
