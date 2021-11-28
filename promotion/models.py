from django.db import models

# Create your models here.


class Promotion(models.Model):


    title = models.CharField(max_length =200, blank=False)
    
    content = models.CharField(max_length = 1000, blank=False)
    poster = models.FileField(upload_to="posters")

    # temp
    candidate = models.CharField(max_length = 10)


    
    # 요것도 나중에 선거 모델 생기면 통합 예정
    election = models.CharField(max_length = 200);


    # 후보자와 통합 시 채워질 예정.
    #  candiate = 