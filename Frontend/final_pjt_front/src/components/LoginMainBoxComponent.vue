<template>
  <div class="container">
    <div class="header">
      <div class="title">인기 금융상품</div>
      <div class="date">2024. 5. 6 기준</div>
      <div class="rate-title">한국은행 기준금리</div>
      <div class="rate">3.50%</div>
    </div>
    <div class="product-container">
      <div class="product-box">
        <div class="product-category">정기적금</div>
        <div class="product-item">
          <div class="rank">1</div>
          <div class="product-image" style="background-image: url('https://c.animaapp.com/uJhSq5S4/img/image@2x.png')"></div>
          <div class="product-name">IBK탄소제로적금(자유적립식)</div>
          <div class="product-bank">중소기업은행</div>
        </div>
        <div class="product-item">
          <div class="rank">2</div>
          <div class="product-image" style="background-image: url('https://c.animaapp.com/uJhSq5S4/img/image-1@2x.png')"></div>
          <div class="product-name">MZ플랜적금</div>
          <div class="product-bank">제주은행</div>
        </div>
        <div class="product-item">
          <div class="rank">3</div>
          <div class="product-image" style="background-image: url('https://c.animaapp.com/uJhSq5S4/img/image-2@2x.png')"></div>
          <div class="product-name">카카오뱅크 26주적금</div>
          <div class="product-bank">주식회사 카카오뱅크</div>
        </div>
      </div>
      <div class="product-box">
        <div class="product-category">정기예금</div>
        <div class="product-item">
          <div class="rank">1</div>
          <div class="product-image" style="background-image: url('https://c.animaapp.com/uJhSq5S4/img/image-3@2x.png')"></div>
          <div class="product-name">더(The) 특판 정기예금</div>
          <div class="product-bank">부산은행</div>
        </div>
        <div class="product-item">
          <div class="rank">2</div>
          <div class="product-image" style="background-image: url('https://c.animaapp.com/uJhSq5S4/img/image-4@2x.png')"></div>
          <div class="product-name">굿스타트예금</div>
          <div class="product-bank">광주은행</div>
        </div>
        <div class="product-item">
          <div class="rank">3</div>
          <div class="product-image" style="background-image: url('https://c.animaapp.com/uJhSq5S4/img/dg-logo-4b9d3ef2eaf3e404d7df-png@2x.png')"></div>
          <div class="product-name">DGB함께예금</div>
          <div class="product-bank">대구은행</div>
        </div>
      </div>
    </div>
    
    <div class="service-header">
      <div class="title">나를 위한 서비스</div>
    </div>
    <div class="service-container">
      <div class="service-box" v-for="card in cards" :key="card.id">
        <div class="service-item">
          <div class="service-title">{{ card.title }}</div>
          <div class="service-description">{{ card.description }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive } from 'vue';

const cards = reactive([
  { id: 1, title: '서비스 1', description: '이것은 서비스 1입니다.' },
  { id: 2, title: '서비스 2', description: '이것은 서비스 2입니다.' },
  { id: 3, title: '서비스 3', description: '이것은 서비스 3입니다.' },
  { id: 4, title: '서비스 4', description: '이것은 서비스 4입니다.' }
]);
</script>

<style scoped>
html, body {
  height: 100%;
  margin: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: "Inter", Helvetica, Arial, sans-serif;
}

.container {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  padding: 0 20px;
  margin: 0;
  box-sizing: border-box;
}

.header {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  margin-bottom: 10px;
  text-align: center;
}

.header .title {
  color: #000;
  font-size: 1.75rem;
  font-weight: 700;
}

.header .date {
  color: #000;
  font-size: 1rem;
  font-weight: 400;
  opacity: 0.6;
  margin-top: 5px;
}

.header .rate-title {
  color: #000;
  font-size: 1rem;
  font-weight: 700;
  opacity: 0.4;
  margin-top: 5px;
}

.header .rate {
  color: #000;
  font-size: 2.5rem;
  font-weight: 700;
  margin-top: 5px;
}

.product-container {
  display: grid;
  gap: 20px;
  width: 100%;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  justify-content: center;
}

.product-box {
  background-color: #fff;
  border: 1px solid #e1e1e4;
  border-radius: 20px;
  box-shadow: 0px 4px 4px #00000040;
  padding: 20px;
  width: 100%;
  max-width: 500px;
  margin: 0 auto 20px;
}

.product-category {
  color: #000;
  font-size: 1.375rem;
  font-weight: 400;
  margin-bottom: 20px;
  text-align: center;
}

.product-item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.product-item .rank {
  color: #000;
  font-size: 1rem;
  font-weight: 400;
  text-align: center;
  width: 20px;
}

.product-item .product-image {
  background-position: 50% 50%;
  background-size: cover;
  height: 49px;
  width: 49px;
  margin: 0 10px;
}

.product-item .product-name {
  color: #000;
  font-size: 1.125rem;
  font-weight: 700;
  flex: 1;
}

.product-item .product-bank {
  color: #000;
  font-size: 1rem;
  font-weight: 400;
  width: 150px;
}

.service-header {
  margin: 40px 0; /* Added top and bottom margin */
  text-align: center;
}

.service-header .title {
  color: #000;
  font-size: 1.75rem;
  font-weight: 700;
}

.service-container {
  display: grid;
  gap: 20px;
  width: 100%;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  justify-content: center;
  margin-bottom: 80px; /* Added bottom margin */
}

.service-box {
  background-color: #fff;
  border: 1px solid #e1e1e4;
  border-radius: 20px;
  box-shadow: 0px 4px 4px #00000040;
  padding: 20px;
  width: 100%;
  max-width: 500px;
  margin: 0 auto 20px;
}

.service-item {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.service-title {
  color: #000;
  font-size: 1.375rem;
  font-weight: 700;
  margin-bottom: 10px;
}

.service-description {
  color: #000;
  font-size: 1rem;
  font-weight: 400;
  text-align: center;
}
</style>
