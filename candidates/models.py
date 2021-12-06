from django.db import models
from django.db.models import fields

# Create your models here.


class Candidate(models.Model):
    symbol = fields.IntegerField()
    party = fields.CharField(max_length=100)
    name_kor = fields.CharField(max_length=100)
    name_hanja = fields.CharField(max_length=100)
    sex = fields.CharField(max_length=100)  # type choice로 바꿔야됨
    birth = fields.DateField(null=True, blank=True)
    job = fields.CharField(max_length=100)
    educational_background = fields.CharField(max_length=100)
    career = fields.CharField(max_length=100)

    bulletin = models.FileField(upload_to="pdf")
    poster = models.FileField(upload_to="pdf")
    pledge = models.FileField(upload_to="pdf")


# class Photo()
