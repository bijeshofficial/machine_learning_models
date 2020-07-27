from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.
class Card(models.Model):
    title = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'images')
    description = models.TextField(null= True)
    url_name = models.CharField(max_length = 30, null = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return self.url_name
    

@receiver(post_delete, sender=Card)
def submission_delete(sender, instance, **kwargs):
    instance.image.delete(False)