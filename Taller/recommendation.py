import sqlite3  # Importa el módulo de Python para SQLite
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Recommendation:
    def __init__(self, customer, recommended_packages):
        self.customer = customer
        self.recommended_packages = recommended_packages

    def add_recommendation(self, package):
        """
        Agrega un paquete a la lista de recomendaciones.
        """
        self.recommended_packages.append(package)
        print("Paquete recomendado añadido exitosamente.")

    def remove_recommendation(self, package_id):
        """
        Elimina un paquete de la lista de recomendaciones según su ID.
        """
        for package in self.recommended_packages:
            if package.id == package_id:
                self.recommended_packages.remove(package)
                print("Paquete recomendado eliminado exitosamente.")
                return
        print("Error: No se encontró el paquete recomendado con el ID proporcionado.")

    def filter_recommendations_by_weight(self, max_weight):
        """
        Filtra las recomendaciones por peso máximo.
        """
        filtered_recommendations = [package for package in self.recommended_packages if package.weight <= max_weight]
        return filtered_recommendations

    def get_recommendation_details(self, package_id):
        """
        Obtiene los detalles de un paquete recomendado según su ID.
        """
        for package in self.recommended_packages:
            if package.id == package_id:
                return package
        return None

    def save_recommendations_to_database(self):
        """
        Guarda las recomendaciones en una base de datos.
        """
        # Conexión a la base de datos (o creación si no existe)
        conn = sqlite3.connect('recommendations.db')
        c = conn.cursor()

        # Creación de la tabla si no existe
        c.execute('''CREATE TABLE IF NOT EXISTS recommendations
                     (customer_id TEXT, package_id TEXT, package_description TEXT, weight REAL)''')

        # Inserción de las recomendaciones en la base de datos
        for package in self.recommended_packages:
            c.execute("INSERT INTO recommendations VALUES (?, ?, ?, ?)",
                      (self.customer.id, package.id, package.description, package.weight))

        # Guardar (commit) los cambios y cerrar la conexión
        conn.commit()
        conn.close()

        print("Recomendaciones guardadas en la base de datos correctamente.")

    def send_recommendations_email(self):
        """
        Envía las recomendaciones por correo electrónico al cliente.
        """
        # Configuración del servidor SMTP
        smtp_server = 'smtp.example.com'  # Ejemplo de servidor SMTP
        smtp_port = 587  # Puerto SMTP
        sender_email = 'your_email@example.com'  # Dirección de correo electrónico del remitente
        password = 'your_password'  # Contraseña del remitente

        # Crear un mensaje multipart
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = self.customer.email
        msg['Subject'] = 'Recomendaciones de paquetes'

        # Cuerpo del mensaje
        body = f'Hola {self.customer.name},\n\nAquí tienes algunas recomendaciones de paquetes:\n\n'
        for package in self.recommended_packages:
            body += f'- {package.description}\n'
        msg.attach(MIMEText(body, 'plain'))

        # Iniciar conexión con el servidor SMTP
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Iniciar el cifrado TLS
            server.login(sender_email, password)  # Autenticación en el servidor SMTP
            server.send_message(msg)  # Envío del mensaje

        print("Correo electrónico con las recomendaciones enviado correctamente.")
