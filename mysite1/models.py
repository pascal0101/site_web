from django.db import models

# Create your models here.
class TimespamtedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract:True
        
class Post(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

class Galerie(TimespamtedModel):
    titre_gal = models.CharField(max_length=255)
    description_gal = models.TextField()

    def __str__(self):
        return self.titre_gal

class Image(TimespamtedModel):
    titre_img = models.CharField(max_length=255)
    description_img = models.TextField()
    image_path = models.ImageField(upload_to='image',blank=True,null=True)
    categorie = models.ForeignKey(Galerie, on_delete=models.CASCADE)

    def __str__(self):
        return self.titre_img
    