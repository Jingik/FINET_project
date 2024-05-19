<template>
  <div class="post-container">
    <div class="center-content">
      <img class="img" src="@/assets/img/logo_name.png" alt="logo">
      <h1 class="board-title">새로운 게시글 작성</h1>
    </div>
    <div class="post-form">    
      <form @submit.prevent="createBoard">
        <div>
          <label for="title">제목</label>
          <input type="text" v-model.trim="title" id="title" placeholder="예시) 'OO금융상품' 후기">
        </div>
        <div>
          <label for="content">내용</label>
          <textarea v-model.trim="content" id="content" placeholder="좋았던 점, 아쉬웠던 점, 바라는 점을 작성해 주세요."></textarea>
        </div>
        <input type="submit" value="작성하기">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { usePostStore } from '@/stores/post';
import { useRouter } from 'vue-router';

const store = usePostStore();
const title = ref('');
const content = ref('');
const router = useRouter();

const createBoard = async () => {
  try {
    const response = await store.createBoard(title.value, content.value);
    console.log(response);
    router.push({ name: 'BoardView' });
  } catch (error) {
    console.log(error);
  }
};
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
