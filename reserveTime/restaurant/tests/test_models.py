from django.test import TestCase
from restaurant.models import Company
from account.models import User


class CompanyTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create(email="test@gmail.com", first_name="test", last_name='test')
        self.company = Company.objects.create(user=self.user, company_name='test',phone_number=1234,city_location='test',province_location='test',country_location='test')

    def test_check_company(self):

        self.assertTrue(self.company)

    def test_company_str(self):
        
        self.assertEqual(str(self.company),self.company.user.email)