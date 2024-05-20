<template>
  <div class="container">
    <h1>Edit Board</h1>
    <form @submit.prevent="updateBoard">
      <div class="form-group">
        <label for="title">Title:</label>
        <input type="text" class="form-control" id="title" v-model="editedBoard.title" required>
      </div>
      <div class="form-group">
        <label for="content">Content:</label>
        <textarea class="form-control" id="content" v-model="editedBoard.content" rows="6" required></textarea>
      </div>
      <button type="submit" class="btn btn-primary">Update</button>
    </form>
  </div>
</template>

<script setup>
import axios from 'axios';
import { ref, onMounted } from 'vue';
import { useRouter, useRoute } from 'vue-router';

const route = useRoute();
const router = useRouter();
const editedBoard = ref({ title: '', content: '' });

onMounted(async () => {
  try {
    const response = await axios.get(`/api/posts/${route.params.id}/`);
    editedBoard.value = response.data;
  } catch (err) {
    console.error('An error occurred:', err);
  }
});

async function updateBoard() {
  try {
    await axios.put(`/api/posts/${route.params.id}/`, editedBoard.value);
    router.push({ name: 'BoardView', params: { id: route.params.id } });
  } catch (err) {
    console.error('An error occurred:', err);
  }
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
  margin-bottom: 20px;
  border: 1px solid #e1e2e3;
  border-radius: 4px;
  font-size: 16px;
}

.post-form textarea {
  height: 200px; /* 기본 높이를 원하는 값으로 설정 */
}

.post-form input[type="submit"] {
  padding: 12px 0;
  width: 100%;
  font-size: 20px;
  font-weight: bold;
  color: #fff;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.post-form input[type="submit"]:hover {
  background-color: #0056b3;
}

.img {
  width: 200px; /* 원하는 너비로 설정 */
  height: auto; /* 이미지 비율을 유지하면서 높이 자동 조정 */
  margin-bottom: 20px; /* 이미지와 텍스트 사이에 여백 추가 */
}
</style>