from django.db import models

class Promotion(models.Model):

    title = models.CharField(max_length =200, blank=False)
    text = models.TextField(blank=True, null=True)

    # 후보자 모델 생성? 그냥 유저 모델에서 역할만 부여?
    candidate = models.CharField(max_length = 10)

    # 선거 모델 생성 후 연결 예정
    election = models.CharField(max_length = 200)
