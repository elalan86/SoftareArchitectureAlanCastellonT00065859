from order import Order  # Importa la clase Order
from user import User  # Importa la clase User

class Invoice:
    """
    Clase que representa una factura.

    Attributes:
        id (int): Identificador único de la factura.
        order_id (int): Identificador único del pedido asociado a la factura.
        price (float): Precio total de la factura.
        status (str): Estado actual de la factura.
        order (Order): Objeto Order asociado a la factura.
        user_a (User): Usuario asociado a la factura.
        payment_method (str): Método de pago utilizado para la factura.
    """

    def __init__(self, id, order_id, price, status, order, user_a, payment_method):
        """
        Inicializa una nueva instancia de Invoice.

        Args:
            id (int): Identificador único de la factura.
            order_id (int): Identificador único del pedido asociado a la factura.
            price (float): Precio total de la factura.
            status (str): Estado inicial de la factura.
            order (Order): Objeto Order asociado a la factura.
            user_a (User): Usuario asociado a la factura.
            payment_method (str): Método de pago utilizado para la factura.
        """
        self.id = id
        self.order_id = order_id
        self.price = price
        self.status = status
        self.order = order
        self.user_a = user_a
        self.payment_method = payment_method

    def update_status(self, new_status):
        """
        Actualiza el estado de la factura.

        Args:
            new_status (str): Nuevo estado de la factura.
        """
        self.status = new_status
        print(f"Estado de la factura actualizado: {new_status}")

    def show_invoice_details(self):
        """
        Muestra los detalles de la factura.
        """
        print("\nDetalles de la factura:")
        print("ID de factura:", self.id)
        print("ID de pedido asociado:", self.order_id)
        print("Precio total:", self.price)
        print("Estado:", self.status)
        print("Método de pago:", self.payment_method)
