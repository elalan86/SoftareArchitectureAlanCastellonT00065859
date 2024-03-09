class User:
    """
    Clase que representa a un usuario.
    """

    def __init__(self, id, username, email, password, cc):
        """
        Inicializa un nuevo objeto User.

        Args:
            id (str): Identificador único del usuario.
            username (str): Nombre de usuario del usuario.
            email (str): Dirección de correo electrónico del usuario.
            password (str): Contraseña del usuario.
            cc (str): Número de la tarjeta de crédito del usuario.
        """
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.cc = cc

    def update_username(self, new_username):
        """
        Actualiza el nombre de usuario del usuario.

        Args:
            new_username (str): Nuevo nombre de usuario.
        """
        self.username = new_username

    def update_email(self, new_email):
        """
        Actualiza la dirección de correo electrónico del usuario.

        Args:
            new_email (str): Nueva dirección de correo electrónico.
        """
        self.email = new_email

    def update_password(self, new_password):
        """
        Actualiza la contraseña del usuario.

        Args:
            new_password (str): Nueva contraseña.
        """
        self.password = new_password

    def update_cc(self, new_cc):
        """
        Actualiza el número de la tarjeta de crédito del usuario.

        Args:
            new_cc (str): Nuevo número de la tarjeta de crédito.
        """
        self.cc = new_cc

    def __str__(self):
        """
        Devuelve una representación de cadena del objeto User.

        Returns:
            str: Representación de cadena del objeto User.
        """
        return f"User(id={self.id}, username={self.username}, email={self.email}, cc={self.cc})"
