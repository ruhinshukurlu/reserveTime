from restaurant.models import Notification

from django import template

register = template.Library()


@register.simple_tag()
def notification(user):
    notification = Notification.objects.filter(reciever=user, read=False)
    
    return notification

