from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ('name',)
        
class CommonInfo(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    release_date = models.DateField()
    poster = models.ImageField(upload_to='pinterest_posters')
    watch_count = models.IntegerField()
    likes = models.IntegerField()
    
    def __str__(self):
        return self.title
    
    class Meta:
        abstract = True
        
class Series(CommonInfo):
    season = models.CharField(max_length=50)
    episode = models.CharField(max_length=50)

class Movie(CommonInfo):
    pass