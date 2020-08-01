from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.

class Company(models.Model):

    PAYMENT_CHOICES = (
        ('AMEX', 'AMEX'),
        ('DinersClub', 'Diners Club'),
        ('MasterCard', 'MasterCard'),
        ('Visa', 'Visa'),
    )
    
    user = models.OneToOneField("account.User", verbose_name=_("customer"), on_delete=models.CASCADE, related_name='company')
    company_name = models.CharField(_("Company Name"), max_length=250)
    phone_number = models.CharField(_("Phone Number"), max_length=50)

    city_location = models.CharField(_("City"), max_length=150)
    province_location = models.CharField(_("Province"), max_length=150)
    country_location = models.CharField(_("Country"), max_length=150)

    work_hours_from = models.TimeField(_("Start Time"), auto_now=False, auto_now_add=False, blank=True, null=True)
    work_hours_to = models.TimeField(_("Finish Time"), auto_now=False, auto_now_add=False, blank=True, null=True)

    cuisines = models.CharField(_("Cuisines"), max_length=50,  blank=True, null=True)
    dining_style = models.CharField(_("Dining Style"), max_length=50,  blank=True, null=True)
    parking_details = models.TextField(_("Parking details"), blank=True, null=True)
    public_transit = models.TextField(_("Public transit"), blank=True, null=True)
    payment_options = models.CharField(_("Payment Options"), choices = PAYMENT_CHOICES, max_length=50, blank=True, null=True)
    executive_chef = models.CharField(_("Executive chef"), max_length=50, blank=True, null=True)
    website = models.URLField(_("Website"), max_length=200, blank=True, null=True)
    private_party_contact = models.CharField(_("Private party contact"), max_length=150, blank=True, null=True)
    description = models.TextField(_("Description"),  blank=True, null=True)

    class Meta:
        verbose_name = 'Comapany'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.user.email


class Photo(models.Model):
    PHOTO_TYPES = (
        ('1', 'Food'),
        ('2', 'Drink'),
        ('3', 'Interior'),
        ('4', 'Exterior'),
    )
    owner = models.ForeignKey("restaurant.Company", verbose_name=_("Owner"), on_delete=models.CASCADE, related_name='photo_owner')
    photo = models.ImageField(_("Company Photo"), upload_to='company-photos/')
    photo_url = models.URLField(_("Photo Url"), max_length=200, blank=True, null=True)
    photo_type = models.CharField(_("type"), choices=PHOTO_TYPES ,max_length=50)

    class Meta:
        verbose_name = _("Photo")
        verbose_name_plural = _("Photos")

    def __str__(self):
        return self.photo


class Menu(models.Model):
    # company = models.OneToOneField("restaurant.Company", verbose_name=_("Company"), on_delete=models.CASCADE, related_name='company_menu')
    company = models.ForeignKey("restaurant.Company", verbose_name=_("Company"), on_delete=models.CASCADE, related_name='menu')
    title = models.CharField(_("Title"), max_length=50)
    price = models.IntegerField(_("Price"))
    description = models.TextField(_("Description"))
    menu_type = models.ForeignKey("restaurant.MenuCategory", verbose_name=_("Type"), on_delete=models.CASCADE, related_name='menu_type')

    class Meta:
        verbose_name = _("Menu")
        verbose_name_plural = _("Menus")

    def __str__(self):
        return self.title


class MenuCategory(models.Model):
    title = models.CharField(_("Title"), max_length=50)

    class Meta:
        verbose_name = _("Menu Category")
        verbose_name_plural = _("Menu Categories")

    def __str__(self):
        return self.title

class Comment(models.Model):

    company = models.ForeignKey("restaurant.Company", verbose_name=_("Company"), on_delete=models.CASCADE, related_name='company_comment')
    user = models.ForeignKey("account.Customer", verbose_name=_("User"), on_delete=models.CASCADE, related_name='user_comment')
    text = models.TextField(_("Comment Text"))
    comment_img = models.ImageField(_("Comment Image"), upload_to='comment-images/')
    commented_at = models.DateTimeField(_("Written Date"), auto_now_add=True)

    class Meta:
        verbose_name = _("Comment")
        verbose_name_plural = _("Comments")

    def __str__(self):
        return self.text


class Table(models.Model):
    TABLE_PLACES = (
        ('outside', 'Outside'),
        ('inside', 'Inside'),
    )

    company = models.ForeignKey("restaurant.Company", verbose_name=_("Company"), on_delete=models.CASCADE, related_name='company_table')
    size = models.IntegerField(_("Size"))
    times = models.ManyToManyField("restaurant.Time", verbose_name=_("Time"))
    table_place = models.CharField(_("Table Place"), max_length=50, choices=TABLE_PLACES)
    
    class Meta:
        verbose_name = _("Table")
        verbose_name_plural = _("Tables")

    def __str__(self):
        return self.size

    
class Time(models.Model):

    free_time = models.TimeField(_("Free Time"), auto_now=False, auto_now_add=False)
    reserved = models.BooleanField(_("Reserved"), default=False)

    class Meta:
        verbose_name = _("Time")
        verbose_name_plural = _("Times")

    def __str__(self):
        return self.reserved_time


class Reservation(models.Model):

    user = models.OneToOneField("account.User", verbose_name=_("User"), on_delete=models.CASCADE, related_name='reservation')
    company = models.ForeignKey("restaurant.Company", verbose_name=_("Company"), on_delete=models.CASCADE, related_name='reservation')
    table = models.OneToOneField("restaurant.Table", verbose_name=_("Table"), on_delete=models.CASCADE, related_name='reservation')
    reserved_time = models.TimeField(_("Reserved Time"), auto_now=False, auto_now_add=False)
    menus = models.ManyToManyField("restaurant.Menu", verbose_name=_("Menus"), related_name='reservation')

    class Meta:
        verbose_name = _("Reservation")
        verbose_name_plural = _("Reservations")

    def __str__(self):
        return self.reserved_time
