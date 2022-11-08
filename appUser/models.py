from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.

class UserChild(models.Model):
    user = models.ForeignKey(User, verbose_name=("Kullanıcı"), on_delete=models.CASCADE)
    profilname = models.CharField(("Profil Adı"), max_length=50)
    image = models.FileField(("Profil Resmi"), upload_to='')
    slug = models.SlugField(("Profil İlk Adı"), editable=False)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.profilname)
        return super().save(*args, **kwargs)
       
