from django.db import models
from django.utils import timezone
# Create your models here.

class Galerie(models.Model):
    titre_gal = models.CharField(max_length=255)
    description_gal = models.TextField()
    image_gal = models.ImageField(upload_to='image',blank=True,null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    def __str__(self):
        return self.titre_gal

class Image(models.Model):
    titre_img = models.CharField(max_length=255)
    description_img = models.TextField()
    image_path = models.ImageField(upload_to='image',blank=True,null=True)
    categorie = models.ForeignKey(Galerie, on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True,null=True)

    def __str__(self):
        return self.titre_img

class Comment(models.Model):
    nom = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    message = models.TextField()
    gal = models.ForeignKey(Galerie,on_delete=models.CASCADE,blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    updated_at = models.DateTimeField(default=timezone.now,blank=True,null=True)
    def __str__(self):
        return self.nom
    