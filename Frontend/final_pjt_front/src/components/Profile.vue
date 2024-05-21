<template>
  <div class="articles">
    <div class="container">
      <div class="section">
        <span>
          <img src="@/assets/img/blog.png" alt="interest" />
          <h2>내가 쓴 글</h2>
        </span>
        <hr />
        <div class="cards">
          <div v-for="post in myPosts" :key="post.id" class="card">
            <p>{{ post.title }}</p>
          </div>
        </div>
      </div>
    </div>

    <div class="container">
      <div class="section">
        <span>
          <img src="@/assets/img/comment.png" alt="interest" />
          <h2>내가 쓴 댓글</h2>
        </span>
        <hr />
        <div class="cards">
          <div v-for="comment in myComments" :key="comment.id" class="card">
            <p>{{ comment.text }}</p>
          </div>
        </div>
      </div>
    </div>
  </div>

  <div class="bigcontainer">
    <div class="section">
      <span>
        <img src="@/assets/img/filledheart.png" alt="interest" />
        <h2>내 관심 상품</h2>
      </span>
      <hr />
      <div class="tabs">
        <button
          v-for="type in productTypes"
          :key="type"
          @click="selectedType = type"
          :class="{ active: type === selectedType }"
          class="tab-button"
        >
          {{ type }}
        </button>
      </div>
      <div class="cards">
        <div
          v-for="product in products[selectedType]"
          :key="product.id"
          class="card"
        >
          <p>{{ product.name }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";

// Example data
const myPosts = ref([
  { id: 1, title: "첫 번째 글" },
  { id: 2, title: "두 번째 글" },
]);

const myComments = ref([
  { id: 1, text: "첫 번째 댓글" },
  { id: 2, text: "두 번째 댓글" },
]);

const products = ref({
  예금: [
    { id: 1, name: "예금 상품 1" },
    { id: 2, name: "예금 상품 2" },
  ],
  적금: [
    { id: 1, name: "적금 상품 1" },
    { id: 2, name: "적금 상품 2" },
  ],
  신용대출: [
    { id: 1, name: "신용대출 상품 1" },
    { id: 2, name: "신용대출 상품 2" },
  ],
});

const productTypes = ref(Object.keys(products.value));
const selectedType = ref(productTypes.value[0]);
</script>

<style scoped>
img {
  width: 40px;
  height: 40px;
}

span {
  display: inline-flex;
  justify-content: center;
  align-items: center;
}

.bigcontainer {
  height: 95%;
}

.container {
  background-color: #ffffff;
  padding: 20px;
  margin: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: calc(50% - 40px); /* 기존 너비에서 margin값을 빼줍니다. */
  border-radius: 10px;
}

.bigcontainer {
  background-color: #ffffff;
  padding: 20px;
  margin: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 10px;
  height: 50%;
}
.articles {
  display: flex;
  height: 50%;
  width: 100%;
}

/* .posts {
  display: flex;
  justify-content: space-between;
} */

h2 {
  font-size: 1.5em;
  margin: 15px 20px 15px;
}

.cards {
  display: flex;
  flex-wrap: wrap;
}

.card {
  background-color: #ffffff;
  box-shadow: 0 0 5px rgba(0, 0, 0, 0.1);
  padding: 10px;
  margin: 10px;
  width: 100%;
}

.tabs {
  margin-top: 20px;
  margin-bottom: 10px;
}

.tab-button {
  border: none;
  background-color: #f0f0f0;
  cursor: pointer;
  margin-right: 10px;
  font-size: 1em;
  border-radius: 20px;
  padding: 5px 15px;
  width: 100px;
}

.tab-button.active {
  font-weight: bold;
  background-color: #007bff;
  color: #ffffff;
}
</style>
