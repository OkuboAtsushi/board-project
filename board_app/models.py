from django.db import models


class BoardModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=50)
    snsimage = models.ImageField(null=True,
                                 blank=True,
                                 upload_to='',
                                 default='default.jpg')
    good = models.IntegerField(null=True, blank=True, default=0)
    read = models.IntegerField(null=True, blank=True, default=0)
    read_user_ids = models.TextField(null=True, blank=True, default='')
