from django.test import TestCase
from parameterized import parameterized
from django.core.exceptions import ValidationError

from ..validators import IbanValidator


class TestCoreValidators(TestCase):
    @parameterized.expand([
        ("KZ091596392977836489", None),
        ("ES9600819746319466166199", None),
        ("XK531149654951952432", None),
        ("FR5210096000707134891153V75", None),
        ("ES4431904565312458110000", "Invalid checksum digits"),
        ("BGZ9IORT80946945979686", "Invalid characters in IBAN BGZ9IORT80946945979686"),
        ("XX80003506513649929162130", "Unknown country-code 'XX'"),
    ])
    def test_validate_iban(self, iban_account, error_message):
        """Tests IBAN account validator

        Args:
            iban_account (str): Client IBAN account.
            error_message (str): Expected error message.
        """
        try:
            validated_iban = IbanValidator(iban_account)
            self.assertEqual(validated_iban, iban_account)

        except ValidationError as e:
            self.assertEqual(str(e.args[0]), error_message)
