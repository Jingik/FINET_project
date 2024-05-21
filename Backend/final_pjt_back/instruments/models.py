from django.db import models
from django.conf import settings


class DepositProducts(models.Model):
    deposit_code = models.CharField(unique=True, max_length=100)
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
    contract_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='contract_deposit', blank=True)
    dcls_strt_day = models.CharField(max_length=20, blank=True, null=True)
    dcls_end_day = models.CharField(max_length=20, blank=True, null=True)
    fin_co_subm_day = models.CharField(max_length=20, blank=True, null=True)

class DepositOptions(models.Model):
    deposit = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    deposit_code = models.CharField(max_length=100)
    intr_rate_type = models.CharField(max_length=100) # 저축 금리 유형명
    intr_rate = models.FloatField(null=True) # 저축 금리
    intr_rate2 = models.FloatField(null=True) # 저축 최대금리
    save_trm = models.CharField(max_length=3) # 저축 기간


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
    crdt_prdt_type_nm = models.CharField(max_length=100) # 수정함
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
