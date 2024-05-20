<template>
  <div class="container">
    <div v-if="loading">Loading...</div>
    <div v-else-if="error">{{ error }}</div>
    <div v-else-if="board" class="card my-4">
      <div class="card-body">
        <h5 class="card-title">{{ board.title }}</h5>
        <hr>
        <p class="card-text">
          <small class="text-muted">
            작성자: {{ board.user_name }} | 작성일: {{ formatDate(board.created_at) }}
          </small>
        </p>
        <p class="card-text" style="padding-top: 50px; padding-bottom: 50px;">{{ board.content }}</p>
        <router-link :to="{ name: 'BoardView' }" class="btn btn-primary">뒤로가기</router-link> <!-- 뒤로가기 버튼 -->
        <button v-if="isCurrentUserAuthor" @click="editBoard" class="btn btn-warning">수정</button>
        <button v-if="isCurrentUserAuthor" @click="confirmDelete" class="btn btn-danger">삭제</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, ref } from 'vue';
import { useCounterStore } from '@/stores/counter';
import { useRoute, useRouter } from 'vue-router';

const store = useCounterStore();
const route = useRoute();
const router = useRouter();
const board = ref(null);
const loading = ref(true);
const error = ref(null);

onMounted(async () => {
  try {
    const response = await axios.get(`${store.API_URL}/posts/${route.params.id}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    board.value = response.data;
  } catch (err) {
    console.error('An error occurred:', err);
    error.value = 'Failed to load the board details.';
  } finally {
    loading.value = false;
  }
});

function formatDate(dateString) {
  const options = { year: 'numeric', month: 'long', day: 'numeric' };
  return new Date(dateString).toLocaleDateString('ko-KR', options);
}

function isCurrentUserAuthor() {
  return board.value && store.currentUser && board.value.user_id === store.currentUser.id;
}

async function editBoard() {
  router.push({ name: 'EditBoard', params: { id: board.value.id } });
}

async function deleteBoard() {
  try {
    await axios.delete(`${store.API_URL}/posts/${board.value.id}/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    router.push({ name: 'BoardView', params: { id: board.value.id } }); // Redirect to BoardView with the deleted board's ID
  } catch (err) {
    console.error('An error occurred:', err);
  }
}

function confirmDelete() {
  if (confirm('정말로 이 게시물을 삭제하시겠습니까?')) {
    deleteBoard();
  }
}
</script>


<style scoped>
.container {
  display: flex;
  justify-content: center;
  padding-top: 150px;
  padding-bottom: 150px;
}

.card {
  border-radius: 10px;
  box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
  transition: 0.3s;
  width: 800px;
  margin: 0 auto;
}

.card:hover {
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

.card-title {
  font-weight: bold;
  font-size: 60px;
}

.card-text {
  font-size: 30px;
}

.text-muted {
  font-size: 0.9rem;
}
</style>
