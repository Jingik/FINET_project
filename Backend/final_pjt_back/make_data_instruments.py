import random
import json
import requests
from collections import OrderedDict
from datetime import datetime, timedelta

# Replace 'instruments' with your actual app name.

# 현재 API 에 들어있는 금융 상품 코드 리스트 저장
DP_URL = 'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
SP_URL = 'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json'

API_KEY = 'e3b1e1d317e3d9e6788a5f8e822e2123'

financial_products = []

params = {
    'auth': API_KEY,
    # 금융회사 코드 020000(은행), 030200(여신전문), 030300(저축은행), 050000(보험), 060000(금융투자)
    'topFinGrpNo': '020000',
    'pageNo': 1,
}

# 정기예금 목록 저장
response = requests.get(DP_URL, params=params).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# 적금 목록 저장
response = requests.get(SP_URL, params=params).json()
baseList = response.get('result').get('baseList')  # 상품 목록

for product in baseList:
    financial_products.append(product['fin_prdt_cd'])

# List of dummy users (replace with actual user ids if needed)
user_ids = list(range(1, 101))  # Assuming 100 users

# Replace the following lists with actual IDs from your database
deposit_product_ids = list(range(1, 21))  # Assuming these IDs exist in the database
saving_product_ids = list(range(1, 21))  # Assuming these IDs exist in the database

# Generate random date within the past year
def random_date():
    start_date = datetime.now() - timedelta(days=365)
    end_date = datetime.now()
    return start_date + (end_date - start_date) * random.random()

# To ensure uniqueness, track already used combinations
used_favorite_saving_combinations = set()
used_deposit_subscription_combinations = set()
used_favorite_deposit_combinations = set()
used_saving_subscription_combinations = set()

# FavoriteSavingProduct dummy data
favorite_saving_product_data = []
for i in range(1, 1000):
    user = random.choice(user_ids)
    saving_product = random.choice(saving_product_ids)
    while (user, saving_product) in used_favorite_saving_combinations:
        user = random.choice(user_ids)
        saving_product = random.choice(saving_product_ids)
    used_favorite_saving_combinations.add((user, saving_product))
    favorite_saving_product_data.append(OrderedDict([
        ("model", "instruments.favoritesavingproduct"),
        ("pk", i),
        ("fields", {
            "user": user,
            "saving_product": saving_product,
            "subscribed_at": random_date().strftime("%Y-%m-%dT%H:%M:%SZ")
        })
    ]))

# DepositSubscription dummy data
deposit_subscription_data = []
for i in range(1, 1000):
    user = random.choice(user_ids)
    deposit_product = random.choice(deposit_product_ids)
    while (user, deposit_product) in used_deposit_subscription_combinations:
        user = random.choice(user_ids)
        deposit_product = random.choice(deposit_product_ids)
    used_deposit_subscription_combinations.add((user, deposit_product))
    deposit_subscription_data.append(OrderedDict([
        ("model", "instruments.depositsubscription"),
        ("pk", i),
        ("fields", {
            "user": user,
            "deposit_product": deposit_product,
            "subscribed_at": random_date().strftime("%Y-%m-%dT%H:%M:%SZ")
        })
    ]))

# FavoriteDepositProduct dummy data
favorite_deposit_product_data = []
for i in range(1, 1000):
    user = random.choice(user_ids)
    deposit_product = random.choice(deposit_product_ids)
    while (user, deposit_product) in used_favorite_deposit_combinations:
        user = random.choice(user_ids)
        deposit_product = random.choice(deposit_product_ids)
    used_favorite_deposit_combinations.add((user, deposit_product))
    favorite_deposit_product_data.append(OrderedDict([
        ("model", "instruments.favoritedepositproduct"),
        ("pk", i),
        ("fields", {
            "user": user,
            "deposit_product": deposit_product,
            "favorited_at": random_date().strftime("%Y-%m-%dT%H:%M:%SZ")
        })
    ]))

# SavingSubscription dummy data
saving_subscription_data = []
for i in range(1, 1000):
    user = random.choice(user_ids)
    saving_product = random.choice(saving_product_ids)
    while (user, saving_product) in used_saving_subscription_combinations:
        user = random.choice(user_ids)
        saving_product = random.choice(saving_product_ids)
    used_saving_subscription_combinations.add((user, saving_product))
    saving_subscription_data.append(OrderedDict([
        ("model", "instruments.savingsubscription"),
        ("pk", i),
        ("fields", {
            "user": user,
            "saving_product": saving_product,
            "subscribed_at": random_date().strftime("%Y-%m-%dT%H:%M:%SZ")
        })
    ]))

# Combine all data
all_data = favorite_saving_product_data + deposit_subscription_data + favorite_deposit_product_data + saving_subscription_data

# Save to JSON file
save_dir = './dummydata/financial_data.json'
with open(save_dir, 'w', encoding='utf-8') as f:
    json.dump(all_data, f, ensure_ascii=False, indent=4)

print(f'Dummy data generation complete. Saved to {save_dir}')
