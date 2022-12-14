from django.db import models

# Create your models here.
#10.
# declare a new model with a name "GeeksModel"
# class GeeksModel(models.Model):
#         # fields of the model
#     title = models.CharField(max_length = 200)
#     description = models.TextField()
#     last_modified = models.DateTimeField(auto_now_add = True)
#     img = models.ImageField(upload_to = "images/")
  
#         # renames the instances of the model
#         # with their title name
#     def __str__(self):
#         return self.title

#11,12,13,14
class GeeksModel11(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()

    def __str__(self) -> str:
        return self.title

from django.db import models
 
# declare a new model with a name "GeeksModel"
class GeeksModel(models.Model):
        # fields of the model
    title = models.CharField(max_length = 200)
    description = models.TextField()
    last_modified = models.DateTimeField(auto_now_add = True)
    img = models.ImageField(upload_to = "images/")
 
        # renames the instances of the model
        # with their title name
    def __str__(self):
        return self.title


class Album(models.Model):
    title = models.CharField(max_length = 30)
    artist = models.CharField(max_length = 30)
    genre = models.CharField(max_length = 30)
  
    def __str__(self):
        return self.title
  
class Song(models.Model):
    name = models.CharField(max_length = 100)
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
  
    def __str__(self):
        return self.name