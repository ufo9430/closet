from django.db import models

# Create your models here.
BRAND_LIST = {
    'Lafudgestore': '라퍼지스토어',
    'Uniformbridge': '유니폼브릿지',
    'Insilence': '인사일런스',
    'YALE': '예일',
    'Covernat': '커버낫',
    'ATTENTIONROW': '어텐션로우',
    'WhatitisNt': '와릿이즌',
    'ADER': '아더에러',
    'Diesel': '디젤',
    'Needles': '니들스',
}
CATEGORY_LIST = {
    '전체' : '',
    '자켓' : 'jacket',
    '셔츠' : 'shirts',
    '티셔츠' : 't-shirts',
    '상의' : 'top',
    '바지' : 'pants',
    '반바지': 'shorts',
    '모자' : 'hats',
    '악세사리' : 'accessory',
    '신발' : 'shoes',
    '가방' : 'bag',
}
class Brand(models.Model):
    brand_name = models.CharField(max_length=30)