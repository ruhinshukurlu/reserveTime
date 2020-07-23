from django.test import TestCase
from account.models import User,Customer
class UserTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@gmail.com", first_name="test", last_name='test')

    def test_user_str(self):

        self.assertEqual(str(self.user), self.user.email)

class CustomerTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@gmail.com", first_name="test", last_name='test')
        self.customer = Customer.objects.create(user=self.user, profile_img='media/img.jpg')

    def test_check_customer(self):

        self.assertTrue(self.customer)

    def test_customer_str(self):
        
        self.assertEqual(str(self.customer),self.customer.user.email)
