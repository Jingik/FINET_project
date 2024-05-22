<!-- BarChart.vue -->
<template>
    <div v-if="chartData12 && chartData24" class="charts-container">
      <div class="chart">
        <Bar :data="chartData12" :options="chartOptions12"></Bar>
      </div>
      <div class="chart">
        <Bar :data="chartData24" :options="chartOptions24"></Bar>
      </div>
    </div>
  </template>
  
  <script setup>
  import { defineProps, computed } from 'vue';
  import { Bar } from 'vue-chartjs';
  import {
    Chart as ChartJS,
    Title,
    Tooltip,
    Legend,
    BarElement,
    CategoryScale,
    LinearScale,
    Colors
  } from 'chart.js';
  
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale, Colors);
  
  const props = defineProps({
    comparisonProducts: {
      type: Array,
      required: true,
    },
  });
  
  const chartData12 = computed(() => {
    if (props.comparisonProducts.length === 0) return null;
  
    const labels = props.comparisonProducts.map(product => product.fin_prdt_nm);
    const data = props.comparisonProducts.map(product => parseFloat(getInterestRate(product, '12')));
  
    return {
      labels,
      datasets: [
        {
          label: '금리 (12개월)',
          backgroundColor: 'rgba(75, 192, 192, 0.2)',
          borderColor: 'rgba(75, 192, 192, 1)',
          borderWidth: 1,
          data,
        },
      ],
    };
  });
  
  const chartData24 = computed(() => {
    if (props.comparisonProducts.length === 0) return null;
  
    const labels = props.comparisonProducts.map(product => product.fin_prdt_nm);
    const data = props.comparisonProducts.map(product => parseFloat(getInterestRate(product, '24')));
  
    return {
      labels,
      datasets: [
        {
          label: '금리 (24개월)',
          backgroundColor: 'rgba(153, 102, 255, 0.2)',
          borderColor: 'rgba(153, 102, 255, 1)',
          borderWidth: 1,
          data,
        },
      ],
    };
  });
  
  const chartOptions12 = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: '12개월 금리 비교',
      },
    },
  };
  
  const chartOptions24 = {
    responsive: true,
    plugins: {
      legend: {
        position: 'top',
      },
      title: {
        display: true,
        text: '24개월 금리 비교',
      },
    },
  };
  
  function getInterestRate(product, months) {
    return product.deposit_options.find(option => option.save_trm === months)?.intr_rate || 0;
  }
  </script>
  
  <style scoped>
  .charts-container {
    display: flex;
    gap: 20px;
  }
  
  .chart {
    flex: 1;
  }
  </style>
  