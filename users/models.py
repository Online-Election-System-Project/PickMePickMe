from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """Custom User Model"""

    GENDER_MALE = "male"
    GENDER_FEMALE = "female"
    GENDER_OTHER = "other"

    GENDER_CHOICES = (
        (GENDER_MALE, "남자"),
        (GENDER_FEMALE, "여자"),
        (GENDER_OTHER, "그 외"),
    )

    MAIN_CITIES = (
        ("seoul", "서울특별시"),
        ("incheon", "인천광역시"),
        ("deagu", "대구광역시"),
        ("gwangju", "광주광역시"),
        ("deajeon", "대전광역시"),
        ("ulsan", "울산광역시"),
        ("sejong", "세종특별자치시"),
        ("busan", "부산광역시"),
        ("gyeonggi", "경기도"),
        ("kangwon", "강원도"),
        ("chungbuk", "충청북도"),
        ("cjungnam", "충청남도"),
        ("gyeongbuk", "경상북도"),
        ("gyeongnam", "경상남도"),
        ("jeonbuk", "전라북도"),
        ("jeonnam", "전라남도"),
        ("jeju", "제주특별자치도"),
    )

    # username & password
    resident_registration_number = models.CharField(
        max_length=14, blank=True, null=True
    )
    # 주민번호
    gender = models.CharField(choices=GENDER_CHOICES, max_length=10, blank=True)
    main_city = models.CharField(
        choices=MAIN_CITIES, max_length=30, blank=True, null=True
    )
    sub_city = models.CharField(max_length=30, blank=True, null=True)
    # # 거주지
