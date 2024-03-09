import unittest
from customer import Customer
from package import Package
from location import Location

class TestLocation(unittest.TestCase):
    """
    Pruebas unitarias para la clase Location.
    """

    def test_location_creation(self):
        """
        Prueba la creación de una ubicación.
        """
        # Arrange
        country = "USA"
        department = "California"
        city = "Los Angeles"
        street = "123 Main St"
        career = "5th Ave"
        postal_code = "90001"

        # Act
        location = Location(country, department, city, street, career, postal_code)

        # Assert
        self.assertEqual(location.country, country)
        self.assertEqual(location.department, department)
        self.assertEqual(location.city, city)
        self.assertEqual(location.street, street)
        self.assertEqual(location.career, career)
        self.assertEqual(location.postal_code, postal_code)

class TestCustomer(unittest.TestCase):
    """
    Pruebas unitarias para la clase Customer.
    """

    def test_customer_creation(self):
        """
        Prueba la creación de un cliente.
        """
        # Arrange
        id = "123"
        name = "John Doe"
        email = "john@example.com"

        # Act
        customer = Customer(id, name, email)

        # Assert
        self.assertEqual(customer.id, id)
        self.assertEqual(customer.name, name)
        self.assertEqual(customer.email, email)

class TestPackage(unittest.TestCase):
    """
    Pruebas unitarias para la clase Package.
    """

    def test_package_creation(self):
        """
        Prueba la creación de un paquete.
        """
        # Arrange
        id = "P001"
        description = "Travel insurance"
        weight = 1.5
        grams_price = 10
        quota = 500
        sender = "John Doe"

        # Act
        package = Package(id, description, weight, grams_price, quota, sender)

        # Assert
        self.assertEqual(package.id, id)
        self.assertEqual(package.description, description)
        self.assertEqual(package.weight, weight)
        self.assertEqual(package.grams_price, grams_price)
        self.assertEqual(package.quota, quota)
        self.assertEqual(package.sender, sender)

if __name__ == "__main__":
    unittest.main()
