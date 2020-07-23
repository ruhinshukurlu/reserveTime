from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Company(models.Model):
    user = models.OneToOneField("account.User", verbose_name=_("company"), on_delete=models.CASCADE, primary_key=True, related_name='Company')
    
    company_name = models.CharField(_("Company Name"), max_length=250)
    phone_number = models.IntegerField(_("Phone Number"))

    city_location = models.CharField(_("City"), max_length=150)
    province_location = models.CharField(_("Province"), max_length=150)
    country_location = models.CharField(_("Country"), max_length=150)

    class Meta:
        verbose_name = 'Comapany'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.user.email
    
