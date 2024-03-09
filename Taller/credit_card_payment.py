from payment_gateway import PaymentGateway 

class CreditCard:
    """
    Clase que representa una tarjeta de crédito.

    Attributes:
        card_number (str): Número de la tarjeta de crédito.
        expiration_date (str): Fecha de vencimiento de la tarjeta.
        cvv (str): Código de seguridad de la tarjeta.
    """

    def __init__(self, card_number, expiration_date, cvv):
        """
        Inicializa un nuevo objeto CreditCard.

        Args:
            card_number (str): Número de la tarjeta de crédito.
            expiration_date (str): Fecha de vencimiento de la tarjeta.
            cvv (str): Código de seguridad de la tarjeta.
        """
        self.card_number = card_number
        self.expiration_date = expiration_date
        self.cvv = cvv


class CreditCardPayment:
    """
    Clase que gestiona los pagos con tarjeta de crédito.

    Attributes:
        cards (list): Lista para almacenar las tarjetas de crédito registradas.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de CreditCardPayment.
        """
        self.cards = []  # Lista para almacenar las tarjetas de crédito registradas

    def process(self, amount):
        """
        Procesa un pago con la tarjeta de crédito registrada.

        Args:
            amount (float): Monto del pago.

        Returns:
            bool: True si el pago se procesó correctamente, False en caso contrario.
        """
        if self.cards:
            # Seleccionar una tarjeta de crédito registrada para procesar el pago
            card_number = self.cards[0].card_number  # Selecciona la primera tarjeta (puede implementarse lógica para seleccionar)
            expiration_date = self.cards[0].expiration_date
            cvv = self.cards[0].cvv
            payment_gateway = PaymentGateway("your_merchant_id", "your_api_key")
            return payment_gateway.authorize_payment(card_number, expiration_date, cvv, amount)
        else:
            print("Error: No se han registrado tarjetas de crédito.")
            return False

    def register_card(self):
        """
        Registra una nueva tarjeta de crédito.

        Solicita al usuario ingresar los detalles de la tarjeta y la agrega a la lista de tarjetas registradas.
        """
        print("\nRegistro de nueva tarjeta de crédito:")
        card_number = input("Ingrese el número de la tarjeta: ")
        expiration_date = input("Ingrese la fecha de vencimiento (MM/YY): ")
        cvv = input("Ingrese el CVV: ")
        # Crear una instancia de CreditCard con los detalles ingresados
        new_card = CreditCard(card_number, expiration_date, cvv)
        # Agregar la tarjeta a la lista de tarjetas registradas
        self.cards.append(new_card)
        print("Tarjeta de crédito registrada correctamente.")
