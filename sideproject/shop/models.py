from django.db import models
from django.urls import reverse
from sideproject.utils import uuid_name_upload_to

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField()
    photo = models.ImageField(blank=True, upload_to=uuid_name_upload_to)
    is_publish = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'({self.pk}) {self.name}'

    def get_absolute_url(self):
        return reverse('shop:detail', kwargs={'item_id' : self.pk})
    