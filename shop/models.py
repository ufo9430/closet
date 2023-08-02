from django.db import models

# Create your models here.
BRAND_LIST = {
    'lafudgestore': '라퍼지스토어',
    'uniformbridge': '유니폼브릿지',
    'insilence': '인사일런스',
    'YALE': '예일',
    'ADER': '아더에러',
}
class Brand(models.Model):
    brand_name = models.CharField(max_length=30)