# chatbot/views.py

from django.shortcuts import render
import pymysql
from django.conf import settings
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import pandas as pd
import json
import openai
import logging

# 로그 설정
logger = logging.getLogger(__name__)

# DB 데이터를 읽어와서 AI에게 줄 리스트로 만들기
creditloan_info = []
deposit_info = []
saving_info = []

try:
    conn = pymysql.connect(
        host='localhost',
        user='yonggu97',
        password=settings.DB_PASSWORD,
        db='ssafy_final'
    )
    cursor = conn.cursor()
    db_list = [
        'instruments_creditloanproducts',
        'instruments_depositproducts',
        'instruments_savingproducts'
    ]

    for db in db_list:
        if 'creditloan' in db:
            cursor.execute(f'SELECT kor_co_nm, fin_prdt_nm, dcls_month, crdt_prdt_type_nm, join_way, spcl_cnd, max_limit, rpay_type_nm, cb_name, crdt_grad_avg FROM {db}')
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            df = pd.DataFrame(rows, columns=columns)
            json_data = df.to_json(orient='records', force_ascii=False)
            creditloan_info.extend(json.loads(json_data))
        elif 'deposit' in db:
            cursor.execute(f'SELECT kor_co_nm, fin_prdt_nm, dcls_month, mtrt_int, max_limit, etc_note, join_deny, join_member, join_way, spcl_cnd, dcls_strt_day, dcls_end_day, fin_co_subm_day FROM {db}')
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            df = pd.DataFrame(rows, columns=columns)
            json_data = df.to_json(orient='records', force_ascii=False)
            deposit_info.extend(json.loads(json_data))
        elif 'saving' in db:
            cursor.execute(f'SELECT kor_co_nm, fin_prdt_nm, dcls_month, mtrt_int, max_limit, etc_note, join_deny, join_member, join_way, spcl_cnd FROM {db}')
            rows = cursor.fetchall()
            columns = [description[0] for description in cursor.description]
            df = pd.DataFrame(rows, columns=columns)
            json_data = df.to_json(orient='records', force_ascii=False)
            saving_info.extend(json.loads(json_data))

    conn.close()
except Exception as e:
    logger.error(f"Database error: {e}")

@api_view(['GET'])
def chatAI(request):
    API_KEY = settings.API_KEY_AI
    openai.api_key = API_KEY
    input_message = request.query_params.get('message', '')
    chat_history = request.session.get('chat_history', [])
    
    chat_history.append({"role": "user", "content": f"{input_message}"})
    
    # 기본 문구 추가
    chat_history.append(
        {"role": "system", "content": "예금, 적금, 대출 상품을 상황에 맞게 추천해 드리겠습니다. 기본적으로 예적금은 금리가 높은 것을, 대출은 금리가 낮은 것을 추천해드립니다."}
    )

    def recommend_best_product(products, key, ascending=False):
        sorted_products = sorted(products, key=lambda x: x[key], reverse=not ascending)
        return sorted_products[0] if sorted_products else None

    def filter_products_by_bank(products, bank_name):
        return [product for product in products if bank_name in product['kor_co_nm']]

    def format_product_info(product):
        return (
            f"상품 이름: {product.get('fin_prdt_nm', 'N/A')}\n\n"
            f"상품 기간: {product.get('dcls_month', 'N/A')}\n\n"
            f"해당 은행: {product.get('kor_co_nm', 'N/A')}\n\n"
            f"금리: {product.get('mtrt_int', 'N/A')}\n\n"
            f"최대 한도: {product.get('max_limit', 'N/A')}\n\n"
            # f"기타 정보: {product.get('etc_note', 'N/A')}\n\n"
            # f"가입 제한: {product.get('join_deny', 'N/A')}\n\n"
            f"가입 대상: {product.get('join_member', 'N/A')}\n\n"
            f"가입 방법: {product.get('join_way', 'N/A')}\n\n"
            # f"특별 조건: {product.get('spcl_cnd', 'N/A')}\n\n"
            # f"공시 시작일: {product.get('dcls_strt_day', 'N/A')}\n\n"
            # f"공시 종료일: {product.get('dcls_end_day', 'N/A')}\n\n"
            f"금융회사 제출일: {product.get('fin_co_subm_day', 'N/A')}"
        )

    bank_name = None

    if '은행' in input_message:
        words = input_message.split()
        for word in words:
            if '은행' in word:
                bank_name = word
                break

    if bank_name:
        filtered_deposit_info = filter_products_by_bank(deposit_info, bank_name)
        filtered_saving_info = filter_products_by_bank(saving_info, bank_name)
        filtered_creditloan_info = filter_products_by_bank(creditloan_info, bank_name)
    else:
        filtered_deposit_info = deposit_info
        filtered_saving_info = saving_info
        filtered_creditloan_info = creditloan_info

    if '예금' in input_message and '추천' in input_message:
        best_deposit = recommend_best_product(filtered_deposit_info, 'mtrt_int', ascending=False)
        if best_deposit:
            chat_history.append(
                {"role": "system", "content": f"추천 예금 상품:\n{format_product_info(best_deposit)}"}
            )
    elif '적금' in input_message and '추천' in input_message:
        best_saving = recommend_best_product(filtered_saving_info, 'mtrt_int', ascending=False)
        if best_saving:
            chat_history.append(
                {"role": "system", "content": f"추천 적금 상품:\n{format_product_info(best_saving)}"}
            )
    elif '대출' in input_message and '추천' in input_message:
        best_loan = recommend_best_product(filtered_creditloan_info, 'crdt_grad_avg', ascending=True)
        if best_loan:
            chat_history.append(
                {"role": "system", "content": f"추천 대출 상품:\n{format_product_info(best_loan)}"}
            )
    elif '예금' in input_message and '금리' in input_message:
        chat_history.append(
            {"role": "system", "content": f"예금 상품의 금리는 다음과 같습니다.\n{filtered_deposit_info}"}
        )
    elif '적금' in input_message and '금리' in input_message:
        chat_history.append(
            {"role": "system", "content": f"적금 상품의 금리는 다음과 같습니다.\n{filtered_saving_info}"}
        )
    elif '대출' in input_message and '금리' in input_message:
        chat_history.append(
            {"role": "system", "content": f"대출 상품의 금리는 다음과 같습니다.\n{filtered_creditloan_info}"}
        )
    elif '설명' in input_message:
        product_name = input_message.split()[-1]
        all_products = deposit_info + saving_info + creditloan_info
        product = next((p for p in all_products if p['fin_prdt_nm'] == product_name), None)
        if product:
            chat_history.append(
                {"role": "system", "content": f"상품 설명:\n{format_product_info(product)}"}
            )
        else:
            chat_history.append(
                {"role": "system", "content": "해당 상품을 찾을 수 없습니다. 정확한 상품 이름을 입력해 주세요."}
            )
    else:
        chat_history.append(
            {"role": "system", "content": "죄송합니다. 더 구체적인 질문을 해주시겠습니까? 예를 들어, '예금 추천' 또는 '적금 금리'와 같은 질문을 해주세요."}
        )

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            temperature=0.5,
            messages=chat_history,
            frequency_penalty=0.5,
            presence_penalty=0.5,
        )
        output_message = response['choices'][0]['message']['content']
        chat_history.append({"role": "assistant", "content": output_message})
        request.session['chat_history'] = chat_history  # 세션에 채팅 기록 저장
        return Response(output_message, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"OpenAI API error: {e}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
