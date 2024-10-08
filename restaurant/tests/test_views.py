from django.test import TestCase
from ..models import MenuItem

class MenuViewTest(TestCase):

    def setUp(self):
        MenuItem.objects.create(title='Beans', price=20, inventory=100)
        MenuItem.objects.create(title='Rice', price=1, inventory=1000)
        MenuItem.objects.create(title='Water', price=100, inventory=3)

    def test_getall(self):
        items = MenuItem.objects.all()
        # print(items)
        self.assertEqual(str(items[0]), 'Beans:20.00')
        self.assertEqual(str(items[1]), 'Rice:1.00')
        self.assertEqual(str(items[2]), 'Water:100.00')
        self.assertEqual(items[0].inventory, 100)
        self.assertEqual(items[1].inventory, 1000)
        self.assertEqual(items[2].inventory, 3)
