from django.db import models

# Create your models here.
class Album(models.Model):
    title=models.CharField(max_length=200)
    year=models.PositiveIntegerField()
    director=models.CharField(max_length=200)
    language=models.CharField(max_length=200)
    image=models.ImageField(upload_to="albimage",default="/albimage/default.png")
    
    def __str__(self):
        return self.title
    
    
class Songs(models.Model):
    title=models.CharField(max_length=200)
    singer=models.CharField(max_length=200)
    track_number=models.PositiveIntegerField()
    album_object=models.ForeignKey(Album,on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title