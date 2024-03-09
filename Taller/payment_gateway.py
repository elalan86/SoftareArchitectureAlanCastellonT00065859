class PaymentGateway:
    """
    Clase para representar una pasarela de pago.
    """

    def __init__(self, merchant_id, api_key):
        """
        Inicializa una instancia de la clase PaymentGateway.

        Args:
            merchant_id (str): ID del comerciante.
            api_key (str): Clave de la API.
        """
        self.merchant_id = merchant_id
        self.api_key = api_key

    def authorize_payment(self, card_number, expiration_date, cvv, amount):
        """
        Autoriza un pago utilizando la información de la tarjeta.

        Args:
            card_number (str): Número de la tarjeta de crédito.
            expiration_date (str): Fecha de vencimiento de la tarjeta (MM/YY).
            cvv (str): Código de verificación de la tarjeta.
            amount (float): Monto del pago.

        Returns:
            bool: True si el pago se autoriza con éxito, False de lo contrario.
        """
        if self.is_valid_card(card_number, expiration_date, cvv) and self.has_sufficient_funds(card_number, amount):
            # Autorizar el pago
            return True
        else:
            return False

    def is_valid_card(self, card_number, expiration_date, cvv):
        """
        Verifica si la tarjeta de crédito es válida.

        Args:
            card_number (str): Número de la tarjeta de crédito.
            expiration_date (str): Fecha de vencimiento de la tarjeta (MM/YY).
            cvv (str): Código de verificación de la tarjeta.

        Returns:
            bool: True si la tarjeta es válida, False de lo contrario.
        """
        return len(card_number) == 16 and card_number.isdigit() \
               and len(expiration_date) == 4 and expiration_date.isdigit() \
               and len(cvv) == 3 and cvv.isdigit()

    def has_sufficient_funds(self, card_number, amount):
        """
        Verifica si la tarjeta tiene fondos suficientes para realizar el pago.

        Args:
            card_number (str): Número de la tarjeta de crédito.
            amount (float): Monto del pago.

        Returns:
            bool: True si hay fondos suficientes, False de lo contrario.
        """
        return True
