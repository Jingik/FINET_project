from django.db import models
from django.conf import settings

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
    contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contract_deposit', blank=True)

class DepositOptions(models.Model):
    deposit = models.ForeignKey(DepositProducts, on_delete=models.CASCADE) # 외래키
    deposit_code = models.CharField(max_length=100)                     # 금융 상품 코드
    intr_rate_type_nm = models.CharField(max_length=100)                # 예금금리 유형명
    intr_rate = models.FloatField(null=True)                            # 예금금리
    intr_rate2 = models.FloatField(null=True)                           # 최고우대금리
    save_trm = models.CharField(max_length=3)                           # 저축기간(단위 : 개월)

# 적금
class SavingProducts(models.Model):
    saving_code = models.CharField(unique=True, max_length=100)
    fin_co_no = models.CharField(max_length=100)
    kor_co_nm = models.CharField(max_length=100)
    fin_prdt_nm = models.CharField(max_length=100)
    dcls_month = models.CharField(max_length=20)
    mtrt_int = models.TextField(blank=True, null=True)
    max_limit = models.IntegerField(blank=True, null=True)
    etc_note = models.TextField(blank=True, null=True)
    join_deny = models.IntegerField(blank=True, null=True)
    join_member = models.TextField(blank=True, null=True)
    join_way = models.CharField(max_length=100)
    spcl_cnd = models.TextField(blank=True, null=True)
    contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contract_saving', blank=True)

class SavingOptions(models.Model):
    saving = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    saving_code = models.CharField(max_length=100, default='')
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField(null=True)
    intr_rate2 = models.FloatField(null=True)
    save_trm = models.CharField(max_length=3)

# 신용대출
class CreditLoanProducts(models.Model):
    creditloan_code = models.CharField(unique=True, max_length=100)
    fin_co_no = models.CharField(max_length=100)
    kor_co_nm = models.CharField(max_length=100)
    fin_prdt_nm = models.CharField(max_length=100)
    dcls_month = models.CharField(max_length=20)
    crdt_prdt_type = models.CharField(max_length=100)
    join_way = models.CharField(max_length=100, blank=True, null=True)
    spcl_cnd = models.TextField(blank=True, null=True)
    max_limit = models.IntegerField(blank=True, null=True)
    rpay_type_nm = models.CharField(max_length=100, blank=True, null=True)
    cb_name = models.CharField(max_length=100, blank=True, null=True)
    contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contract_creditloan', blank=True)

class CreditLoanOptions(models.Model):
    creditloan = models.ForeignKey(CreditLoanProducts, on_delete=models.CASCADE)
    creditloan_code = models.CharField(max_length=100)
    crdt_lend_rate_type = models.CharField(max_length=1, default='A')  # 기본값 설정
    crdt_lend_rate_type_nm = models.CharField(max_length=100, default='기본금리')  # 기본값 설정
    crdt_grad_1 = models.FloatField(null=True)
    crdt_grad_4 = models.FloatField(null=True)
    crdt_grad_5 = models.FloatField(null=True)
    crdt_grad_6 = models.FloatField(null=True)
    crdt_grad_10 = models.FloatField(null=True)
    crdt_grad_11 = models.FloatField(null=True)
    crdt_grad_12 = models.FloatField(null=True)
    crdt_grad_13 = models.FloatField(null=True)
    crdt_grad_avg = models.FloatField(null=True)
