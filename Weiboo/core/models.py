from django.db import models

class SiteSetting(models.Model):
    site_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='core/logos/', blank=True, null=True)
    contact_email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()

    def __str__(self):
        return self.site_name
