from django.test import TestCase
from customers.models import Customer

class CustomerTestCase(TestCase):
    def setUp(self):
        Customer.objects.create(name="Mike Mike", code="MM123", phone_number="+254712345678")

    def test_customer_creation(self):
        customer = Customer.objects.get(code="MM123")
        self.assertEqual(customer.name, "Mike Mike")
