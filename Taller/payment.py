from payment_gateway import PaymentGateway

class Payment:
    """
    Clase para manejar los pagos.
    """

    def __init__(self, merchant_id, api_key):
        """
        Inicializa una instancia de la clase Payment.

        Args:
            merchant_id (str): ID del comerciante.
            api_key (str): Clave de la API.
        """
        self.payment_gateway = PaymentGateway(merchant_id, api_key)

    def process_payment(self, card_number, expiration_date, cvv, amount):
        """
        Procesa un pago utilizando la pasarela de pago.

        Args:
            card_number (str): Número de tarjeta de crédito.
            expiration_date (str): Fecha de vencimiento de la tarjeta (MM/YY).
            cvv (str): Código de verificación de la tarjeta.
            amount (float): Monto del pago.

        Returns:
            bool: True si el pago se procesa con éxito, False de lo contrario.
        """
        if self.payment_gateway.authorize_payment(card_number, expiration_date, cvv, amount):
            print("Pago exitoso. Se ha procesado el pago.")
            return True
        else:
            print("Error: No se pudo procesar el pago.")
            return False
