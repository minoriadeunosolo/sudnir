from django.core.exceptions import ValidationError
from schwifty import IBAN


def IbanValidator(iban):
    """Validates an IBAN account.
            Args:
                iban (str): IBAN account to be checked
            Raise:
                ValidationError: if the IBAN has invalid checksum digits or a unknown country-code.
    """
    try:
        IBAN(iban)
    except ValueError as e:
        raise ValidationError(e)

    return iban

