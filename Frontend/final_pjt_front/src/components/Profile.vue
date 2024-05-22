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
          <div v-if="myPosts.length > 0" v-for="post in myPosts" :key="post.id" class="card">
            <p>{{ post.title }}</p>
          </div>
          <p v-else>작성한 글이 없습니다.</p>
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
          <div v-if="myComments.length > 0" v-for="comment in myComments" :key="comment.id" class="card">
            <p>{{ comment.content }}</p>
          </div>
          <p v-else>작성한 댓글이 없습니다.</p>
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
        <div v-if="products[selectedType].length > 0" v-for="product in products[selectedType]" :key="product.id" class="card">
          <p>{{ getProductById(selectedType, product)?.fin_prdt_nm || "Unknown Product" }}
            <span class="bank-name">{{ getProductById(selectedType, product)?.kor_co_nm }}</span>
          </p>
        </div>
        <p v-else>관심 상품이 없습니다.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from "vue";
import axios from "axios";
import { useUserStore } from "@/stores/user";

const useuserstore = useUserStore();
const token = computed(() => useuserstore.token);

const myPosts = ref([]);
const myComments = ref([]);
const products = ref({
  deposits: [],
  savings: [],
  creditloans: []
});
const productTypes = ref(["deposits", "savings", "creditloans"]);
const selectedType = ref(productTypes.value[0]);

const depositProducts = ref([]);
const savingProducts = ref([]);
const creditloanProducts = ref([]);

onMounted(async () => {
  await fetchMyPosts();
  await fetchMyComments();
  await fetchFavorites();
  await fetchAllProducts();
});

async function fetchMyPosts() {
  try {
    const response = await axios.get("http://127.0.0.1:8000/posts/user/boards/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    myPosts.value = response.data.results;
  } catch (error) {
    console.error("Error fetching posts:", error);
  }
}

async function fetchMyComments() {
  try {
    const response = await axios.get("http://127.0.0.1:8000/posts/user/comments/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    myComments.value = response.data.results;
  } catch (error) {
    console.error("Error fetching comments:", error);
  }
}

async function fetchFavorites() {
  try {
    const response = await axios.get("http://127.0.0.1:8000/financial/favorites/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    products.value.deposits = response.data.deposit_subscriptions;
    products.value.savings = response.data.saving_subscriptions;
    products.value.creditloans = response.data.creditloan_subscriptions;
    console.log('Fetched Favorites:', products.value);
  } catch (error) {
    console.error("Error fetching favorite products:", error);
  }
}

async function fetchAllProducts() {
  try {
    const depositResponse = await axios.get("http://127.0.0.1:8000/financial/deposit-products/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    depositProducts.value = depositResponse.data;
    console.log('Deposit Products:', depositProducts.value);

    const savingResponse = await axios.get("http://127.0.0.1:8000/financial/saving-products/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    savingProducts.value = savingResponse.data;
    console.log('Saving Products:', savingProducts.value);

    const creditloanResponse = await axios.get("http://127.0.0.1:8000/financial/creditloan-products/", {
      headers: { Authorization: `Token ${token.value}` }
    });
    creditloanProducts.value = creditloanResponse.data;
    console.log('Credit Loan Products:', creditloanProducts.value);
  } catch (error) {
    console.error("Error fetching product data:", error);
  }
}

function getProductById(type, product) {
  const productId = product[`${type.slice(0, -1)}_product`];
  console.log(`Matching product in ${type} with ID: ${productId}`);
  let productList;
  switch (type) {
    case "deposits":
      productList = depositProducts.value;
      break;
    case "savings":
      productList = savingProducts.value;
      break;
    case "creditloans":
      productList = creditloanProducts.value;
      break;
    default:
      productList = [];
  }
  const matchedProduct = productList.find(p => p.id === productId);
  console.log(`Matched Product:`, matchedProduct);
  return matchedProduct;
}
</script>

<style scoped>
img {
  width: 30px;
  height: 30px;
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

h2 {
  font-size: 1em;
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
  display: flex;
  justify-content: space-between;
}

.bank-name {
  margin-left: auto;
  color: grey;
  font-size: 0.9em;
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
