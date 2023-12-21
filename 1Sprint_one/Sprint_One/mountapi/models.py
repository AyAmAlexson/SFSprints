from django.db import models



class MountainPass(models.Model):
   author = models.ForeignKey('User', on_delete=models.CASCADE)
   beauty_title = models.CharField(max_length=255)
   title = models.CharField(max_length=255)
   other_titles = models.CharField(max_length=255)
   connect = models.TextField(blank=True)
   add_time = models.DateTimeField()
   user = models.JSONField(default=dict)
   coord = models.JSONField(default=dict)
   level = models.JSONField(default=dict)

class Image(models.Model):
   mountain_pass = models.ForeignKey(MountainPass, related_name='images', on_delete=models.CASCADE)
   data = models.ImageField()
   title = models.CharField(max_length=255)