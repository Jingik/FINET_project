<template>
  <div>
    <h5>{{ board.id }}</h5>
    <p>{{ board.title }}</p>
    <p>{{ board.content }}</p>
    <RouterLink 
      :to="{ name: 'DetailView', params: { id: board.id }}"
    >
      [DETAIL]
    </RouterLink>
    <hr>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'

defineProps({
  board: Object
})
</script>
