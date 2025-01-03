from django.core.exceptions import ValidationError
import re

def validate_name(name):
    error_message = "Improper name format"
    regex = r'^[A-Z][a-z]*$'
    good_name = re.match(regex, name)
    if good_name:
        return name
    else:
        raise ValidationError(error_message, params={ 'name' : name })

def validate_school_email(value):
    email_pattern = re.compile(r'^.+@school\.com$')
    if not email_pattern.match(value):
        raise ValidationError('Invalid school email format. Please use an email ending with "@school.com".')