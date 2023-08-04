from django.db import models

# Create your models here.
BRAND_LIST = {
    'lafudgestore': '라퍼지스토어',
    'uniformbridge': '유니폼브릿지',
    'insilence': '인사일런스',
    'YALE': '예일',
    'covernat': '커버낫',
    'WhatitisNt': '와릿이즌',
    'ADER': '아더에러',
    'diesel': '디젤',
}
CATEGORY_LIST = {
    '전체' : '',
    '아우터' : '아우터',
    '상의' : '상의',
    '바지' : '바지',
    '악세사리' : '악세사리',
    '신발' : '신발',
}
class Brand(models.Model):
    brand_name = models.CharField(max_length=30)