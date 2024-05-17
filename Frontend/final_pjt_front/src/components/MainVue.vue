<template>
    <div class="div">
      <MainBox />
      <div class ="bank">
        <MainBank />
      </div>
      <MainBox1 />
    </div>
  </template>
  
  <script setup>
  import { defineComponent } from "vue";
  import MainBank from '@/components/BankComponent.vue'
  import MainBox from '@/components/MainBoxComponent.vue'
  import MainBox1 from '@/components/MainBoxComponent1.vue'
  </script>
  
  <style scoped>
  .div {
    
    width: 100%;
    position: relative;
    /* box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25); */
    background-color: #fff;
    /* border: 1px solid #000; */
    box-sizing: border-box;
    height: 2696px;
    overflow: hidden;
    text-align: left;
    font-size: 16px;
    color: #000;
    font-family: Inter;
  }
  .bank{
    justify-content: center;
  }
  </style>