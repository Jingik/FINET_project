from django.db import models
from django.conf import settings

# 예금
class DepositProducts(models.Model):
    deposit_code = models.CharField(unique=True, max_length=100)        # 금융 상품 코드
    fin_co_no = models.CharField(max_length=100)                       # 금융회사 코드
    kor_co_nm = models.CharField(max_length=100)                       # 금융회사명
    fin_prdt_nm = models.CharField(max_length=100)                     # 금융상품명
    dcls_month = models.CharField(max_length=20)                       # 공시 제출월
    mtrt_int = models.TextField(blank=True, null=True)                 # 만기 후 이자율
    max_limit = models.IntegerField(blank=True, null=True)             # 최고한도
    etc_note = models.TextField(blank=True, null=True)                 # 금융상품설명
    join_deny = models.IntegerField(blank=True, null=True)             # 가입제한(1:제한없음, 2:서민전용, 3:일부제한)
    join_member = models.TextField(blank=True, null=True)              # 가입대상
    join_way = models.CharField(max_length=100)                        # 가입 방법
    spcl_cnd = models.TextField(blank=True, null=True)                 # 우대조건
    contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contract_deposit')
 
class DepositOptions(models.Model):
    deposit = models.ForeignKey(DepositProducts, on_delete=models.CASCADE) # 외래키
    deposit_code = models.TextField()                     # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100) # 예금금리 유형명
    intr_rate = models.FloatField(null=True)                      # 예금금리
    intr_rate2 = models.FloatField(null=True)                     # 최고우대금리
    save_trm = models.CharField(max_length=3)                    # 저축기간(단위 : 개월)
    
 
# 적금
class SavingProducts(models.Model):
    saving_code = models.CharField(max_length=100) # fin_prdt_cd 
    fin_co_no = models.CharField(max_length=100)
    kor_co_nm = models.CharField(max_length=100)
    name = models.CharField(max_length=100) # fin_prdt_nm
    dcls_month = models.CharField(max_length=20)
    join_way = models.CharField(max_length=100)
    mtrt_int = models.TextField(blank=True, null=True)
    spcl_cnd = models.TextField(blank=True, null=True)
    join_deny = models.IntegerField(blank=True, null=True)
    join_member = models.TextField(blank=True, null=True)
    etc_note = models.TextField(blank=True, null=True)
    max_limit = models.IntegerField(blank=True, null=True)
    contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contract_saving')

class SavingOptions(models.Model):
    saving = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    intr_rate_type_nm = models.CharField(max_length=2)
    rsrv_type_nm = models.CharField(max_length=10)
    save_trm = models.CharField(max_length=3)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)
    

## 개인 신용 대출
## 모델도 아직 안 만듬
## serializer도 아직 안 만듬