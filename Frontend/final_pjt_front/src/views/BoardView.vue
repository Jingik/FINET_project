<template>
  <div>
    <h1>Board Page</h1>
    <RouterLink :to="{ name: 'CreateView' }">
      [CREATE]
    </RouterLink>
    <BoardList />
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

</style>
