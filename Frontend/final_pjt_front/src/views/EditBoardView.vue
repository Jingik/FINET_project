<template>
  <div class="post-container">
    <div class="center-content">
      <img class="img" src="@/assets/img/logo_name.png" alt="logo">
      <h1 class="board-title">게시글 수정</h1>
    </div>
    <div class="post-form">    
      <form @submit.prevent="updateBoard">
        <div>
          <label for="title">제목</label>
          <input type="text" v-model.trim="editedBoard.title" id="title" placeholder="예시) 'OO금융상품' 후기" required>
        </div>
        <div>
          <label for="content">내용</label>
          <textarea v-model.trim="editedBoard.content" id="content" placeholder="좋았던 점, 아쉬웠던 점, 바라는 점을 작성해 주세요." rows="6" required></textarea>
        </div>
        <div class="button-group">
          <input type="submit" value="수정하기">
          <button type="button" @click="cancelUpdate">수정취소</button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';
import { useCounterStore } from '@/stores/counter';

const route = useRoute();
const router = useRouter();
const editedBoard = ref({ title: '', content: '' });
const store = useCounterStore();

onMounted(async () => {
  try {
    const response = await axios.get(`${store.API_URL}/posts/${route.params.id}/`);
    editedBoard.value = response.data;
  } catch (err) {
    console.error('An error occurred:', err);
  }
});

async function updateBoard() {
  try {
    await axios.put(`${store.API_URL}/posts/${route.params.id}/update/`, editedBoard.value);
    router.push({ name: 'DetailView', params: { id: route.params.id } });
  } catch (err) {
    console.error('An error occurred:', err);
  }
}

function cancelUpdate() {
  router.push({ name: 'DetailView', params: { id: route.params.id } });
}
</script>

<style scoped>
/* 폼 컨테이너 스타일 */
.post-container {
  max-width: 1000px;
  margin: 100px auto 20px;
  padding: 20px;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

/* 가운데 정렬을 위한 클래스 */
.center-content {
  text-align: center;
}

/* 게시판 제목 스타일 */
.board-title {
  font-size: 24px;
  margin-bottom: 20px;
  color: #000000;
}

/* 게시글 작성 폼 스타일 */
.post-form label {
  font-size: 18px;
  font-weight: bold;
}

.post-form input[type="text"],
.post-form textarea {
  width: calc(100% - 20px);
  padding: 10px;
  margin: 20px 10px;
  border: 1px solid #e1e2e3;
  border-radius: 4px;
  font-size: 16px;
}

.post-form textarea {
  height: 200px; /* 기본 높이를 원하는 값으로 설정 */
}

.post-form .button-group {
  display: flex;
  justify-content: space-around;
}

.post-form input[type="submit"],
.post-form button[type="button"] {
  padding: 12px 0;
  width: 48%;
  font-size: 20px;
  font-weight: bold;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.post-form button[type="button"] {
  background-color: #dc3545;
}

.post-form input[type="submit"]:hover {
  background-color: #0056b3;
}

.post-form button[type="button"]:hover {
  background-color: #c82333;
}

.img {
  width: 200px; /* 원하는 너비로 설정 */
  height: auto; /* 이미지 비율을 유지하면서 높이 자동 조정 */
  margin-bottom: 20px; /* 이미지와 텍스트 사이에 여백 추가 */
}
</style>
