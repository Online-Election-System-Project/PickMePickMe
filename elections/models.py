from django.db import models


class Election(models.Model):
    """Election Model Definition"""

    TYPE_PRESIDENT_ELELCTION = "president_election"
    TYPE_MAYOR_ELECTION = "mayor_election"
    TYPE_PARLIAMENTARY_ELECTION = "parliamentary_election"

    TYPE_CHOICES = (
        (TYPE_PRESIDENT_ELELCTION, "대통령 선거"),
        (TYPE_MAYOR_ELECTION, "시장 선거"),
        (TYPE_PARLIAMENTARY_ELECTION, "국회의원 선거"),
    )

    title = models.CharField(max_length=100)
    register_period_begin = models.DateTimeField(auto_now_add=False, null=True)
    register_period_end = models.DateTimeField(auto_now_add=False, null=True)
    election_period_begin = models.DateTimeField(auto_now_add=False, null=True)
    election_period_end = models.DateTimeField(auto_now_add=False, null=True)
    election_type = models.CharField(choices=TYPE_CHOICES, max_length=40, null=True)
    # election_area -> 라이브러리 사용해서 할지, 아니면 choice 사용해서 할지
    # candidate_list
