from django.db import models

class Tourist(models.Model):
    email = models.EmailField()
    fam = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    otc = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)

class Coord(models.Model):
    latitude = models.FloatField(default=0.00)
    longitude = models.FloatField(default=0.00)
    height = models.IntegerField(default=0)


class Level(models.Model):
    winter = models.CharField(max_length=5, default='A0', null=True, blank=True)
    summer = models.CharField(max_length=5, default='A0', null=True, blank=True)
    autumn = models.CharField(max_length=5, default='A0', null=True, blank=True)
    spring = models.CharField(max_length=5, default='A0', null=True, blank=True)

class Passage(models.Model):
    status = models.CharField(max_length=20, default='new')
    beauty_title = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    other_titles = models.CharField(max_length=100, null=True, blank=True)
    connect = models.CharField(max_length=255, null=True, blank=True)
    add_time = models.DateTimeField(auto_now_add=True)
    user = models.OneToOneField(Tourist, on_delete=models.CASCADE)
    coords = models.OneToOneField(Coord, on_delete=models.CASCADE)
    level = models.OneToOneField(Level, on_delete=models.CASCADE)


class Image(models.Model):
    data = models.CharField(max_length=255)
    title = models.CharField(max_length=100)
    passage = models.ForeignKey(Passage, related_name='images', on_delete=models.CASCADE)