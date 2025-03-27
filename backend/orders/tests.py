from django.test import TestCase
from customers.models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="John Doe", code="JD123", phone_number="0712345678")

    def test_customer_creation(self):
        customer = Customer.objects.get(code="JD123")
        self.assertEqual(customer.name, "John Doe")
