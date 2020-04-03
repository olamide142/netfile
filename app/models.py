from django.db import models

# Create your models here.


class File(models.Model):
    file_owner = models.CharField(max_length=50, null=True)
    file_name = models.CharField(max_length=250, null=True)
    file_ext = models.CharField(max_length=10, null=True)
    file_size = models.BigIntegerField(default=0)
    file_id = models.CharField(max_length=10, null=True)
    
    def __str__(self):
        return self.file_name

