from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
 
class Customer(models.Model):
    name = models.CharField(
        max_length=100,
        help_text=_('First and last name.'),
        verbose_name=_('name'))
    address = models.CharField(
        max_length=100,
        verbose_name=_('address'))
    phone = models.CharField(
        max_length=10,
        validators=[RegexValidator(
            '^\d{10}$',
            _('Phone must be exactly 10 digits.'))],
        verbose_name=_('phone number'))
 
    class Meta:
        verbose_name = _('customer')
        verbose_name_plural = _('customers')