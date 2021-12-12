from django.db import models
from elections import models as election_models


class Promotion(models.Model):

    STATUS_WATING = "waiting"
    STATUS_ACCEPTED = "accepted"
    STATUS_REJECTED = "rejected"

    STATUS_CHOICES = (
        (STATUS_WATING, "승인 대기 중"),
        (STATUS_ACCEPTED, "승인 완료"),
        (STATUS_REJECTED, "거절됨"),
    )

    title = models.CharField(max_length=200, blank=False)
    text = models.TextField(blank=True, null=True)

    symbol = models.IntegerField(blank=True, null=True)
    party = models.CharField(max_length=100, blank=True)
    name_kor = models.CharField(max_length=100, blank=True)
    name_hanja = models.CharField(max_length=100, blank=True)
    sex = models.CharField(max_length=100, blank=True)  # type choice로 바꿔야됨
    birth = models.DateField(null=True, blank=True)
    job = models.CharField(max_length=100, blank=True)
    educational_background = models.CharField(max_length=100, blank=True)
    career = models.CharField(max_length=100, blank=True)

    bulletin = models.FileField(upload_to="pdf", blank=True)
    poster = models.FileField(upload_to="pdf", blank=True)
    pledge = models.FileField(upload_to="pdf", blank=True)

    # 후보자 모델 생성? 그냥 유저 모델에서 역할만 부여?
    candidate = models.ForeignKey("users.User", on_delete=models.CASCADE)

    # 선거 모델 생성 후 연결 예정
    election = models.ForeignKey("elections.Election", on_delete=models.CASCADE)

    vote_number = models.IntegerField(default=0)

    status = models.CharField(
        choices=STATUS_CHOICES, max_length=30, blank=True, null=True
    )
