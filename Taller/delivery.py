from order import Order  # Importa la clase Order
from location import Location  # Importa la clase Location
from user import User  # Importa la clase User

class Delivery:
    """
    Clase que representa un proceso de entrega.

    Attributes:
        order (Order): Objeto Order que contiene los detalles del pedido.
        status (str): Estado actual de la entrega.
        sender (User): Remitente del paquete.
        receiver (User): Destinatario del paquete.
        location (Location): Ubicación actual del paquete.
    """

    def __init__(self, order, status, sender, receiver, location):
        """
        Inicializa una nueva instancia de Delivery.

        Args:
            order (Order): Objeto Order que contiene los detalles del pedido.
            status (str): Estado inicial de la entrega.
            sender (User): Remitente del paquete.
            receiver (User): Destinatario del paquete.
            location (Location): Ubicación inicial del paquete.
        """
        self.order = order
        self.status = status
        self.sender = sender
        self.receiver = receiver
        self.location = location

    def update_status(self, new_status):
        """
        Actualiza el estado de la entrega.

        Args:
            new_status (str): Nuevo estado de la entrega.
        """
        self.status = new_status
        print(f"Estado de la entrega actualizado: {new_status}")

    def update_location(self, new_location):
        """
        Actualiza la ubicación de la entrega.

        Args:
            new_location (Location): Nueva ubicación de la entrega.
        """
        self.location = new_location
        print("Ubicación de la entrega actualizada.")

    def show_delivery_details(self):
        """
        Muestra los detalles de la entrega.
        """
        print("\nDetalles de la entrega:")
        print("ID del pedido:", self.order.id)
        print("Estado:", self.status)
        print("Remitente:", self.sender.name)
        print("Destinatario:", self.receiver.name)
        print("Ubicación:", self.location.city, ",", self.location.country)
