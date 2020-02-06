from django.conf import settings
from django.db import models
from .validators import IbanValidator


class CtClient(models.Model):
    """Client Class"""
    first_name = models.CharField(max_length=40, help_text='First Name')
    last_name = models.CharField(max_length=40, help_text='Last Name')
    iban = models.CharField(max_length=50, unique=True, help_text='Client IBAN account', validators=[IbanValidator])
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    def save(self, *args, **kwargs):
        """Converts to lowercase first_name and last_name"""
        self.first_name = self.first_name.lower()
        self.last_name = self.last_name.lower()

        return super(CtClient, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Clients"
        ordering = ['first_name', 'last_name', 'iban']
