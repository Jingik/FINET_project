<template>
  <div class="community-board-container">
    <div class="community-board">
      <div class="header">
        <img class="logo" src="@/assets/img/community.png" alt="communitylogo">
        <h1>커뮤니티</h1>
      </div>
      <RouterLink :to="{ name: 'CreateView' }" class="btn-create">새 글 작성</RouterLink>
      <BoardList />
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue'
import { useCounterStore } from '@/stores/counter'
import { RouterLink } from 'vue-router'
import BoardList from '@/components/BoardList.vue'

const store = useCounterStore()

onMounted(() => {
  store.getBoards()
})
</script>

<style>
  .logo {
    width: 50px; /* 원하는 너비로 설정 */
    height: auto; /* 이미지 비율을 유지하면서 높이 자동 조정 */
    margin-right: 30px; /* 이미지와 텍스트 사이에 여백 추가 */
  }

  .header {
    display: flex; /* Flexbox 사용 */
    align-items: center; /* 수직 중앙 정렬 */
    margin-bottom: 20px; /* 헤더 아래 여백 추가 */
  }

  /* 컨테이너 스타일 */
  .community-board-container {
    max-width: 1400px;
    margin: 150px auto;
    padding: 20px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1); /* box-shadow 추가 */
    background-color: #fff;
    border-radius: 5px;
  }

  /* 게시판 스타일 */
  .community-board {
    position: relative; /* 상대적 위치를 사용하여 내부 요소 배치 */
    padding: 20px;
  }

  /* 제목 스타일 */
  .community-board h1 {
    font-size: 2em;
    color: #333; /* 제목 색상 */
  }

  /* 새 글 작성 버튼 스타일 */
  .btn-create {
    position: absolute;
    top: 0;
    right: 0;
    margin: 20px;
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    text-decoration: none;
    border-radius: 5px;
  }

  /* 새 글 작성 버튼 호버 스타일 */
  .btn-create:hover {
    background-color: #0056b3;
  }
</style>
