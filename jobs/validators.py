from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from datetime import date

def validate_future_date(value):
    """Validate that a date is in the future"""
    if value < date.today():
        raise ValidationError(_('Date must be in the future'))

def validate_budget(value):
    """Validate that budget is within reasonable bounds"""
    if value < 5:
        raise ValidationError(_('Budget must be at least $5'))
    if value > 100000:
        raise ValidationError(_('Budget cannot exceed $100,000'))