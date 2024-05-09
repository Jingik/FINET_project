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

class CreditLoanProducts(models.Model):
    creditloan_code = models.CharField(max_length=100) # fin_prdt_cd 
    fin_co_no = models.CharField(max_length=100) # 금융회사 코드
    kor_co_nm = models.CharField(max_length=100) # 금융 회사 명
    name = models.CharField(max_length=100) # fin_prdt_nm 상품명
    dcls_month = models.CharField(max_length=20) # 공시 제출월
    join_way = models.CharField(max_length=100) # 가입 방법
    crdt_prdt_type = models.CharField(max_length=100) # 대출 종류 코드
    cb_name = models.TextField() # CB 회사명
    dcls_strt_day = models.CharField(max_length=100) # 공시 시작일
    dcls_end_day = models.CharField(max_length=100) # 공시 종료일
    fin_co_subm_day = models.CharField(max_length=100) # 금융회사 제출일
    contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contract_credit_loan')
    
class CreditLoanOptions(models.Model):
    creditloan = models.ForeignKey(CreditLoanProducts, on_delete=models.CASCADE)
    crdt_lend_rate_type = models.CharField(max_length=100) # 금리 구분 코드 
    crdt_lend_rate_type_nm = models.CharField(max_length=2) # 금리 구분
    crdt_grad_1 = models.FloatField(null=True) # 900점 초과
    crdt_grad_4 = models.FloatField(null=True) # 801 ~ 900
    crdt_grad_5 = models.FloatField(null=True) # 701 ~ 800
    crdt_grad_6 = models.FloatField(null=True) # 601 ~ 700
    crdt_grad_10 = models.FloatField(null=True) # 501 ~ 600
    crdt_grad_11 = models.FloatField(null=True) # 401 ~ 500
    crdt_grad_12 = models.FloatField(null=True) # 301 ~ 400점
    crdt_grad_13 = models.FloatField(null=True) # 300점 이하
    crdt_grad_avg = models.FloatField(null=True) # 평균 금리
    
