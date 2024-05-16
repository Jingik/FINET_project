<template>
    <div :class="$style.finetCopyright2008FinetContainer">
      <p :class="$style.finet">FINET</p>
      <p :class="$style.copyright2008FinetAllRight">
        Copyrightⓒ2008 FINET All rights reserved.
      </p>
    </div>
</template>

<script setup>

</script>

<style scoped>
.finet {
  margin: 0;
}

.copyright2008FinetAllRight {
    margin: 0;
    font-size: 20px;
    color: #000;
}
.finetCopyright2008FinetContainer {
    position: absolute;
    top: 32px;
    left: 80px;
    line-height: 150%;
    font-size: 25px;
    color: #00408b;
}
</style>

