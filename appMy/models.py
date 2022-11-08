from django.db import models

# Create your models here.



class Category(models.Model):
    category = models.CharField(("Category"), max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.category
    
class ClassModel(models.Model):
    classmodel = models.CharField(("Populer"), max_length=100, blank=True, null=True)
   
    def __str__(self) -> str:
        return self.classmodel

class Video(models.Model):
    video = models.CharField(("Video Çeşidi"), max_length=100, blank=True, null=True)
   
    def __str__(self) -> str:
        return self.video

class Movie(models.Model):
    title = models.CharField(("Film Başlık"), max_length=100)
    image = models.FileField(("Film Foroğrafı"), upload_to="")
    info = models.TextField(("Film Açıklaması"))
    category = models.ForeignKey(Category, verbose_name=("Category"), on_delete=models.CASCADE, blank=True, null=True)
    classmodel = models.ForeignKey(ClassModel, verbose_name=("Category"), on_delete=models.CASCADE, blank=True, null=True)
    video = models.ManyToManyField(Video, verbose_name=("Video Film yada Dizi"))
    
    def __str__(self) -> str:
        return self.title
    

    
