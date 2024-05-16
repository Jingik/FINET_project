from django.db import models

# Create your models here.
class Map (models.Model):
    # cur_unit = models.CharField(max_length=100) # 통화코드
    # cur_nm = models.CharField(max_length=100) # 국가/통화명
    # ttb = models.CharField(max_length=100) # 전신환 받을 때
    # tts = models.CharField(max_length=100) # 전신환 보낼 때
    # deal_bas_r = models.CharField(max_length=100) # 매매 기준율