from django.conf import settings
from django.db import models
from django.utils import timezone

class Portfolio(models.Model):

    # 후보자 모델 생성? 그냥 유저 모델에서 역할만 부여?
    # candiatae = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    title = models.CharField(max_length=200)
    text = models.TextField(blank=True, null=True)
    poster = models.FileField(upload_to="posters", blank=True, null=True)

    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title