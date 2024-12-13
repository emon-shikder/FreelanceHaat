from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_hourly_rate(value):
    """Validate hourly rate is within reasonable bounds"""
    if value < 0:
        raise ValidationError(_('Hourly rate cannot be negative'))
    if value > 1000:
        raise ValidationError(_('Hourly rate cannot exceed $1000'))