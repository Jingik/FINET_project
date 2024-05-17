<template>
  <div id="app">
    <div class="header">
    <NavigationHeader />
    </div>
    <div class="content">
      <RouterView />
    </div>
    <div class ="footer">
    <NavigationFooter />
  </div>
  </div>
</template>

<script setup>
import NavigationHeader from './components/NavigationHeader.vue'
import NavigationFooter from './components/NavigationFooter.vue'
import { RouterView } from 'vue-router'
</script>

<style src="@/assets/global.css"></style>
<style scoped>
.header {
  width: 100%;
  position: fixed;
  top: 0;
  background-color: #ffffff; /* Adjust to your header background color */
  z-index: 999; /* Adjust z-index to make sure it's above other elements */
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  left: 0;
}
.content {
  padding-top: 0px; /* Adjust to match the height of your header */
}
.footer {
  width: 100%;
  background-color: #f0f0f0; /* Adjust to your footer background color */
  box-sizing: border-box;
}
</style>