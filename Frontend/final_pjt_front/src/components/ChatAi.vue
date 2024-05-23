<template>
  <div class="chat-page">
    <h1>AI Chat</h1>
    <div class="chat-container">
      <div v-for="(message, index) in chatHistory" :key="index" class="chat-message" :class="message.role">
        <p>{{ message.content }}</p>
      </div>
    </div>
    <div class="input-container">
      <input v-model="message" @keyup.enter="sendMessage" placeholder="질문을 입력하세요" class="chat-input" />
      <button @click="sendMessage" class="send-button">전송</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const message = ref('')
const chatHistory = ref([])

const sendMessage = async () => {
  if (message.value.trim() === '') return

  chatHistory.value.push({ role: 'user', content: message.value })
  try {
    const res = await axios.get('http://localhost:8000/chat/', {
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
}
</script>

<style scoped>
.chat-page {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
}

h1 {
  margin-bottom: 20px;
}

.chat-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 600px;
  flex: 1;
  overflow-y: auto;
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
  max-width: 600px;
  padding: 10px;
  background-color: #ffffff;
  border-top: 1px solid #cccccc;
  border-radius: 0 0 10px 10px;
  box-shadow: 0 -2px 10px rgba(0, 0, 0, 0.1);
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
