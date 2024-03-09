from authentication import Authentication
from user import User
from credit_card_payment import CreditCardPayment
from location import Location

def register_credit_card():
    """
    Registra una tarjeta de crédito.
    """
    print("\nRegistro de tarjeta de crédito:")
    card_number = input("Ingrese el número de tarjeta: ")
    expiration_date = input("Ingrese la fecha de vencimiento (MM/YY): ")
    cvv = input("Ingrese el CVV: ")
    # Crear una instancia de CreditCardPayment y registrar la tarjeta
    new_credit_card = CreditCardPayment()
    new_credit_card.register_card(card_number, expiration_date, cvv)
    print("Tarjeta de crédito registrada exitosamente.")

def register_user(auth):
    """
    Registra un nuevo usuario.
    """
    print("\nRegistro de nuevo usuario:")
    cc = int(input("Ingrese su cc de usuario: "))
    username = input("Ingrese su nombre de usuario: ")
    email = input("Ingrese su dirección de correo electrónico: ")
    password = input("Ingrese su contraseña: ")
    # Crear una instancia de User con los datos proporcionados
    new_user = User(id=cc, username=username, email=email, password=password, cc=cc)

    # Llamar al método de autenticación para registrar al nuevo usuario
    if auth.register_user(new_user):
        print("¡Registro exitoso! Ahora puede iniciar sesión.")
    else:
        print("Error al registrar usuario. Por favor, intente nuevamente.")

def login(auth):
    """
    Inicia sesión de usuario.
    """
    print("\nInicio de sesión:")
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    # Intentar iniciar sesión con las credenciales proporcionadas
    if auth.login(username, password):
        print("¡La autenticación fue exitosa!")
        return True
    else:
        print("La autenticación falló. Por favor, verifique sus credenciales.")
        return False

def view_profile(auth):
    """
    Muestra el perfil del usuario.
    """
    # Obtener el usuario autenticado
    authenticated_user = auth.get_authenticated_user()
    
    if authenticated_user:
        print("\nPerfil del usuario:")
        print("Nombre de usuario:", authenticated_user.username)
        print("Correo electrónico:", authenticated_user.email)
        print("CC de usuario:", authenticated_user.cc)
    else:
        print("Debe iniciar sesión para ver su perfil.")

def logout():
    """
    Cierra sesión de usuario.
    """
    print("\nCierre de sesión exitoso.")

def register_location():
    """
    Registra una nueva ubicación.
    """
    print("\nRegistro de ubicación:")
    country = input("Ingrese el país: ")
    department = input("Ingrese el departamento: ")
    city = input("Ingrese la ciudad: ")
    street = input("Ingrese la calle: ")
    career = input("Ingrese la carrera: ")
    postal_code = input("Ingrese el código postal: ")
    # Crear una instancia de Location y registrar la ubicación
    new_location = Location(country, department, city, street, career, postal_code)
    new_location.register_location(country, department, city, street, career, postal_code)

def modify_location():
    """
    Modifica una ubicación existente.
    """
    print("\nModificación de ubicación:")
    # Se solicita al usuario que ingrese detalles para buscar la ubicación existente
    country = input("Ingrese el país: ")
    department = input("Ingrese el departamento: ")
    city = input("Ingrese la ciudad: ")

    # Se busca la ubicación existente en una base de datos o sistema de almacenamiento
    existing_location = find_location(country, department, city)

    if existing_location:
        print("\nUbicación encontrada. Proporcione los nuevos detalles:")
        new_country = input("Nuevo país (Deje en blanco para mantener sin cambios): ")
        new_department = input("Nuevo departamento (Deje en blanco para mantener sin cambios): ")
        new_city = input("Nueva ciudad (Deje en blanco para mantener sin cambios): ")
        new_street = input("Nueva calle (Deje en blanco para mantener sin cambios): ")
        new_career = input("Nueva carrera (Deje en blanco para mantener sin cambios): ")
        new_postal_code = input("Nuevo código postal (Deje en blanco para mantener sin cambios): ")

        # Se actualizan los detalles de la ubicación existente con los nuevos detalles proporcionados
        if new_country:
            existing_location.country = new_country
        if new_department:
            existing_location.department = new_department
        if new_city:
            existing_location.city = new_city
        if new_street:
            existing_location.street = new_street
        if new_career:
            existing_location.career = new_career
        if new_postal_code:
            existing_location.postal_code = new_postal_code

        print("Ubicación modificada exitosamente.")
    else:
        print("Ubicación no encontrada. Verifique los detalles proporcionados.")

def view_location():
    """
    Muestra detalles de una ubicación.
    """
    print("\nVer ubicación:")
    # Se solicita al usuario que ingrese detalles para buscar la ubicación
    country = input("Ingrese el país: ")
    department = input("Ingrese el departamento: ")
    city = input("Ingrese la ciudad: ")

    # Se busca la ubicación en una base de datos o sistema de almacenamiento
    location = find_location(country, department, city)

    if location:
        # Se muestra la ubicación si se encuentra
        print("\nDetalles de la ubicación encontrada:")
        print("País:", location.country)
        print("Departamento:", location.department)
        print("Ciudad:", location.city)
        print("Calle:", location.street)
        print("Carrera:", location.career)
        print("Código postal:", location.postal_code)
    else:
        print("Ubicación no encontrada. Verifique los detalles proporcionados.")

def main_menu():
    """
    Muestra el menú principal.
    """
    print("\nMenú Principal:")
    print("1. Registrarse")
    print("2. Iniciar sesión")
    print("3. Salir")

def logged_in_menu():
    """
    Muestra el menú cuando el usuario está autenticado.
    """
    print("\nMenú de Sesión Iniciada:")
    print("1. Acceder a los beneficios financieros")
    print("2. Ver perfil")
    print("3. Cerrar sesión")

def financial_benefits_menu():
    """
    Muestra el menú de beneficios financieros.
    """
    print("\nMenú de Beneficios Financieros:")
    print("1. Registrar ubicación")
    print("2. Modificar ubicación")
    print("3. Ver ubicación")
    print("4. Registrar tarjeta de crédito")
    print("5. Volver al menú principal")

def main():
    """
    Función principal que maneja la lógica del programa.
    """
    # Crear una instancia de Authentication
    auth = Authentication()
    logged_in = False

    while True:
        if not logged_in:
            main_menu()
        else:
            logged_in_menu()
        choice = input("Seleccione una opción: ").strip()

        if not logged_in:
            if choice == "1":
                register_user(auth)
            elif choice == "2":
                if login(auth):
                    logged_in = True
            elif choice == "3":
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")
        else:
            if choice == "1":
                financial_benefits_menu()
                while True:
                    financial_choice = input("Seleccione una opción: ").strip()
                    if financial_choice == "1":
                        register_location()
                    elif financial_choice == "2":
                        modify_location()
                    elif financial_choice == "3":
                        view_location()
                    elif financial_choice == "4":
                        register_credit_card()
                    elif financial_choice == "5":
                        break
                    else:
                        print("Opción no válida. Por favor, seleccione una opción válida.")
            elif choice == "2":
                view_profile(auth)
            elif choice == "3":
                logout()
                logged_in = False
            else:
                print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()
