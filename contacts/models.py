from django.core.urlresolvers import reverse
from django.db import models
import datetime
from time import time

def get_upload_file_name(instance, filename):
	return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename) 


class Contact(models.Model):

    first_name = models.CharField(max_length=255,)
    last_name = models.CharField(max_length=255,)
    birthday = models.DateField(blank=True, default=datetime.date.today())
    phone = models.CharField(max_length=25, blank=True)
    picture = models.FileField(blank=True, upload_to=get_upload_file_name)
    email = models.EmailField()

    def __str__(self):

        return ' '.join([
	    self.last_name,
            self.first_name,  
        ])

    def get_absolute_url(self):

        return reverse('contacts-view', kwargs={'pk': self.id})


class Address(models.Model):

    contact = models.ForeignKey(Contact)
    address_type = models.CharField(
        max_length=255,
    )
    street = models.CharField(
        max_length=255,
    )
    city = models.CharField(
        max_length=255,
    )
    state = models.CharField(
        max_length=255,
    )
    postal_code = models.CharField(
        max_length=5,
    )

    class Meta:
        unique_together = ('contact', 'address_type',)
