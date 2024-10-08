from django.test import TestCase
from ..models import MenuItem

# Create your tests here.
class TestMenuItem(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(title='IceCream', price=80, inventory=100)
        self.assertEqual(str(item), 'IceCream:80')