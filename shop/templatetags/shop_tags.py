from django import template
from shop.models import Product  # Make sure this is your Product model

register = template.Library()

@register.simple_tag
def total_products():
    return Product.objects.count()
