from decimal import Decimal

from django import template
from shop.models import Product

register = template.Library()


@register.filter
def format_price(value):
    """
    Format a numeric price as 1,234.56
    """
    if value is None:
        return ""
    try:
        value = Decimal(value)
    except Exception:
        return value
    return f"{value:,.2f}"


@register.simple_tag
def total_products():
    """
    Return total number of products in the catalog.
    """
    return Product.objects.count()


@register.simple_tag
def cart_total(cart_items):
    """
    Return sum of all cart item subtotals.
    """
    total = Decimal('0.00')
    for item in cart_items:
        total += item.subtotal
    return total
