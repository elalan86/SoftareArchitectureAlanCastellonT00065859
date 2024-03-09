from user import User  # Importa la clase User

class Authentication:
    """
    Clase que gestiona la autenticación de usuarios.

    Attributes:
        users (list): Lista para almacenar los usuarios registrados.
        authenticated_user (User): Usuario autenticado.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de Authentication.
        """
        self.users = []  # Lista para almacenar los usuarios registrados
        self.authenticated_user = None  # Usuario autenticado

    def register_user(self, user):
        """
        Registra un nuevo usuario.

        Args:
            user (User): Objeto User a registrar.

        Returns:
            bool: True si el usuario se registró exitosamente, False si el nombre de usuario ya está en uso.
        """
        # Verificar si el nombre de usuario ya existe
        if self.find_user_by_username(user.username):
            print("Error: El nombre de usuario ya está en uso.")
            return False
        # Agregar el usuario a la lista de usuarios registrados
        self.users.append(user)
        print("Usuario registrado exitosamente.")
        return True

    def login(self, username, password):
        """
        Inicia sesión para un usuario con las credenciales proporcionadas.

        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña.

        Returns:
            bool: True si la autenticación fue exitosa, False en caso contrario.
        """
        # Buscar al usuario por nombre de usuario y contraseña
        user = self.find_user_by_credentials(username, password)
        if user:
            self.authenticated_user = user
            print(f"Bienvenido, {user.username}! Has iniciado sesión exitosamente.")
            return True
        else:
            print("Error: Credenciales inválidas. Por favor, inténtalo de nuevo.")
            return False

    def logout(self):
        """
        Cierra la sesión del usuario autenticado.
        """
        # Cerrar sesión del usuario autenticado
        self.authenticated_user = None
        print("Sesión cerrada exitosamente.")

    def find_user_by_username(self, username):
        """
        Busca un usuario por nombre de usuario.

        Args:
            username (str): Nombre de usuario a buscar.

        Returns:
            User or None: El objeto User si se encuentra, None si no se encuentra.
        """
        # Buscar un usuario por nombre de usuario
        for user in self.users:
            if user.username == username:
                return user
        return None

    def find_user_by_credentials(self, username, password):
        """
        Busca un usuario por nombre de usuario y contraseña.

        Args:
            username (str): Nombre de usuario.
            password (str): Contraseña.

        Returns:
            User or None: El objeto User si se encuentra, None si no se encuentra o las credenciales son incorrectas.
        """
        # Buscar un usuario por nombre de usuario y contraseña
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        return None

    def get_authenticated_user(self):
        """
        Devuelve el usuario autenticado.

        Returns:
            User or None: El objeto User si hay un usuario autenticado, None si no hay ningún usuario autenticado.
        """
        # Devuelve el usuario autenticado
        return self.authenticated_user
