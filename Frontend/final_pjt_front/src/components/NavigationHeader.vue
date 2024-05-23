<template>
  <div class="header">
    <div class="span" @click="handleSpanClick">
      <div class="p4">FINET</div>
      <img class="img-icon1" alt="" src="@/assets/img/img (1).png" />
    </div>
    <div class="navbar">
      <div
        class="nav"
        @mouseover="showDropdown('deposit')"
        @mouseleave="hideDropdown('deposit')"
      >
        예적금
        <div v-if="dropdownVisible.deposit" class="dropdown-content">
          <RouterLink :to="{ name: 'DepositView' }"
            ><div class="dropdown-item">정기예금</div></RouterLink
          >
          <RouterLink :to="{ name: 'SavingsView' }"
            ><div class="dropdown-item">정기적금</div></RouterLink
          >
        </div>
      </div>
      <div
        class="nav"
        @mouseover="showDropdown('loan')"
        @mouseleave="hideDropdown('loan')"
      >
        대출
        <div v-if="dropdownVisible.loan" class="dropdown-content">
          <RouterLink :to="{ name: 'CreditloanView' }"
            ><div class="dropdown-item">신용대출</div></RouterLink
          >
          <div class="dropdown-item">전세자금(개발중)</div>
          <div class="dropdown-item">주택담보(개발중)</div>
        </div>
      </div>
      <div
        class="nav"
        @mouseover="showDropdown('creditCard')"
        @mouseleave="hideDropdown('creditCard')"
      >
        신용카드
        <div v-if="dropdownVisible.creditCard" class="dropdown-content">
          <div class="dropdown-item">전체카드조회(개발중)</div>
          <div class="dropdown-item">추천카드(개발중)</div>
          <div class="dropdown-item">내게 맞는 카드(개발중)</div>
        </div>
      </div>
      <RouterLink :to="{ name: 'ExchangeView' }"
        ><div
          class="nav"
          @mouseover="showDropdown('exchange')"
          @mouseleave="hideDropdown('exchange')"
        >
          외환/환전
          <div v-if="dropdownVisible.exchange" class="dropdown-content">
            <RouterLink :to="{ name: 'ExchangeView' }"
              ><div class="dropdown-item">환전계산기</div></RouterLink
            >
          </div>
        </div>
      </RouterLink>
      <RouterLink :to="{ name: 'BoardView' }"
        ><div
          class="nav"
          @mouseover="showDropdown('lounge')"
          @mouseleave="hideDropdown('lounge')"
        >
          라운지
          <div v-if="dropdownVisible.lounge" class="dropdown-content">
            <RouterLink :to="{ name: 'maps' }"
              ><div class="dropdown-item">지역 은행 찾기</div></RouterLink
            >
            <RouterLink :to="{ name: 'BoardView' }"
              ><div class="dropdown-item">커뮤니티</div></RouterLink
            >
          </div>
        </div></RouterLink
      >
      <div class="input-typetext">
        <div class="label">검색어를 입력해주세요.</div>
        <img
          class="button-typesubmit-icon"
          alt=""
          src="@/assets/img/button type=submit.svg"
        />
      </div>
      <div class="button-group">
        <button @click="toggleChatbot" class="button">Chating Bot</button>
      </div>
      <div class="button-group">
        <button v-if="isLogin" @click="logOut" class="button">로그아웃</button>
        <RouterLink :to="isLogin ? { name: 'ProfilePage' } : { name: 'LogInView' }">
          <div @mouseover="showDropdown('user')" @mouseleave="hideDropdown('user')">
            <template v-if="isLogin">
              <img
              src="@/assets/img/user.png"
              alt="User Icon"
              class="icon-image"
              style="width: 45px; height: 45px"
              />
              <div v-if="dropdownVisible.user" class="dropdown-content">
                <RouterLink :to="{ name: 'DashBoardPage' }"
              ><div class="dropdown-item">마이페이지</div></RouterLink>
              <RouterLink :to="{ name: 'EditProfilePage' }"
              ><div class="dropdown-item">내정보 수정</div></RouterLink>
              </div>
            </template>
            <template v-else> 로그인/회원가입 </template>
          </div>
        </RouterLink>
      </div>

    </div>
  </div>
  <div v-if="chatbotVisible" class="modal-overlay" @click.self="toggleChatbot">
    <div class="modal">
      <div class="chat-page">
        <h1>AI Chat</h1>
        <div class="chat-container">
          <div
            v-for="(message, index) in chatHistory"
            :key="index"
            class="chat-message"
            :class="message.role"
          >
            <p>{{ message.content }}</p>
          </div>
        </div>
        <div class="input-container">
          <input
            v-model="message"
            @keyup.enter="sendMessage"
            placeholder="질문을 입력하세요"
            class="chat-input"
          />
          <button @click="sendMessage" class="send-button">전송</button>
        </div>
      </div>
      <button @click="toggleChatbot" class="close-button">Close</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from "vue";
import { RouterLink, useRouter } from "vue-router";
import { useUserStore } from "@/stores/user";
import axios from 'axios';

const dropdownVisible = ref({
  user: false,
  deposit: false,
  loan: false,
  creditCard: false,
  exchange: false,
  lounge: false,
});

const chatbotVisible = ref(false);
const message = ref('');
const chatHistory = ref([]);

const userStore = useUserStore();
const isLogin = computed(() => userStore.isLogin);
const router = useRouter();

const showDropdown = (key) => {
  dropdownVisible.value[key] = true;
};

const hideDropdown = (key) => {
  dropdownVisible.value[key] = false;
};

const toggleDropdown = (key) => {
  dropdownVisible.value[key] = !dropdownVisible.value[key];
};

const toggleChatbot = () => {
  chatbotVisible.value = !chatbotVisible.value;
};

const logOut = () => {
  userStore.logOut();
  hideDropdown('user');
};

const handleSpanClick = () => {
  if (isLogin.value) {
    router.push({ name: "MainLogin" });
  } else {
    router.push({ name: "MainView" });
  }
};

const goToPage = (pageName) => {
  router.push({ name: pageName });
  hideDropdown('user'); // dropdown 닫기
};

const sendMessage = async () => {
  if (message.value.trim() === '') return

  chatHistory.value.push({ role: 'user', content: message.value })
  try {
    const res = await axios.get('http://127.0.0.1:8000/chat/', {
      params: {
        message: message.value,
      },
    })
    chatHistory.value.push({ role: 'ai', content: res.data })
    message.value = ''
  } catch (error) {
    console.error(error)
    chatHistory.value.push({ role: 'error', content: 'Error: Failed to get response' })
  }
};
</script>

<style scoped>
.header {
  align-items: flex-start;
  display: flex;
  gap: 10px;
  height: 80px;
  width: 83.33%;
  margin: 0 auto;
  top: 0;
}

.header .span {
  height: 107px;
  margin-bottom: -21px;
  position: relative;
  width: 162px;
  cursor: pointer;
}

.header .p4 {
  color: var(--x1-3);
  font-family: "Inter", Helvetica;
  font-size: 25px;
  font-weight: 500;
  height: 38px;
  left: 86px;
  letter-spacing: 0;
  line-height: 37.5px;
  position: absolute;
  top: 31px;
  white-space: nowrap;
  width: 74px;
}

.header .img-icon1 {
  height: 107px;
  left: 0;
  object-fit: cover;
  position: absolute;
  top: 0;
  width: 86px;
}

.header .navbar {
  align-items: center;
  display: flex;
  gap: var(--variable-collection-spacing-m);
  height: 86px;
  justify-content: flex-end;
  margin-left: auto;
}

.header .nav {
  color: #828282;
  font-family: var(--body-text-font-family);
  font-size: var(--body-text-font-size);
  font-style: var(--body-text-font-style);
  font-weight: var(--body-text-font-weight);
  letter-spacing: var(--body-text-letter-spacing);
  line-height: var(--body-text-line-height);
  position: relative;
  white-space: nowrap;
  width: fit-content;
  cursor: pointer;
}

.header .dropdown-content {
  display: flex;
  flex-direction: column;
  position: absolute;
  background-color: white;
  box-shadow: 0px 8px 16px 0px rgba(0, 0, 0, 0.2);
  z-index: 1;
  min-width: 160px;
}

.header .dropdown-item {
  padding: 12px 16px;
  cursor: pointer;
}

.header .dropdown-item:hover {
  background-color: #ddd;
}

.header .input-typetext {
  align-items: center;
  border: 1px solid;
  border-color: #0000001a;
  border-radius: 6px;
  display: flex;
  gap: 4px;
  justify-content: flex-end;
  padding: 8px;
  position: relative;
  width: 200px;
}

.header .label {
  color: #00000080;
  flex: 1;
  font-family: "Roboto", Helvetica;
  font-size: 14px;
  font-weight: 400;
  letter-spacing: 0;
  line-height: 20px;
  margin-top: -1px;
  position: relative;
}

.header .button-typesubmit-icon {
  height: 20px;
  position: relative;
  width: 20px;
}

.header .button-group {
  display: flex;
  align-items: center;
}

.header .button {
  color: black;
  border: 1px solid #808080;
  padding: 8px 16px;
  font-size: 16px;
  border-radius: 4px;
  cursor: pointer;
  margin-right: 20px;
}

.header .button:hover {
  background-color: #0056b3;
}

.modal-overlay {
  position: fixed;
  bottom: 0;
  right: 0;
  width: auto;
  height: auto;
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  z-index: 1000;
  padding: 20px;
}

.modal {
  background-color: white;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: relative;
  width: 500px;
  max-width: 500px; /* 최대 너비를 줄임 */
  height: 55vh; /* 높이를 고정 */
  display: flex;
  flex-direction: column;
}

.close-button {
  background-color: #007bff;
  color: white;
  border: none;
  padding: 10px 15px;
  cursor: pointer;
  border-radius: 5px;
  position: absolute;
  top: 10px;
  right: 10px;
}

.close-button:hover {
  background-color: #0056b3;
}

.chat-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  width: 100%;
  height: 100%; /* 부모의 높이에 맞춤 */
}

h1 {
  margin-bottom: 20px;
}

.chat-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  flex: 1;
  overflow-y: auto; /* 스크롤 가능 */
  padding: 20px;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.chat-message {
  margin-bottom: 10px;
  padding: 10px;
  border-radius: 10px;
  max-width: 75%;
  word-wrap: break-word;
}

.user {
  align-self: flex-end;
  background-color: #007bff;
  color: #ffffff;
}

.ai {
  align-self: flex-start;
  background-color: #e0e0e0;
  color: #000000;
}

.error {
  background-color: #f8d7da;
  color: #721c24;
  align-self: flex-start;
}

.input-container {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 100%;
  padding: 10px;
  background-color: #ffffff;
  border-top: 1px solid #cccccc;
  border-radius: 0 0 10px 10px;
}

.chat-input {
  flex: 1;
  padding: 10px;
  border: 1px solid #cccccc;
  border-radius: 5px;
  margin-right: 10px;
}

.send-button {
  background-color: #007bff;
  color: #ffffff;
  padding: 10px 15px;
  border: none;
  cursor: pointer;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.send-button:hover {
  background-color: #0056b3;
}
</style>

