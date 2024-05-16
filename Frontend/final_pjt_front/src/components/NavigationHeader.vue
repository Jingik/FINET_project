<template>
  <div :class="styles.navigationFooter">
    <!-- 네비게이션 푸터 -->
    <div :class="styles.itemsParent">
      <!-- 네비게이션 메뉴들 -->
      <div :class="styles.items">
        <div :class="styles.div1">예적금</div>
        <div :class="styles.page">정기예금</div>
        <div :class="styles.page">정기적금</div>
        <div :class="styles.page">자유입출금</div>
      </div>
      <div :class="styles.items">
        <div :class="styles.div1">대출</div>
        <div :class="styles.page">신용대출</div>
        <div :class="styles.page">전세자금대출</div>
        <div :class="styles.page">주택담보대출</div>
      </div>
      <div :class="styles.items">
        <div :class="styles.div1">신용카드</div>
        <div :class="styles.page">한눈에 보기</div>
        <div :class="styles.page">추천카드</div>
        <div :class="styles.page">내게 맞는 카드</div>
      </div>
      <div :class="styles.items">
        <div :class="styles.div1">외환/환전</div>
        <div :class="styles.page">환율조회</div>
        <div :class="styles.page">환전계산기</div>
      </div>
      <div :class="styles.items">
        <div :class="styles.div1">라운지</div>
        <div :class="styles.page">Page</div>
        <div :class="styles.page">Page</div>
        <div :class="styles.page">Page</div>
      </div>
    </div>

  </div>
</template>

<script setup>
const styles = {
  navigationFooter: {
    position: 'relative',
    marginTop: '20px',
    width: '100%',
    backgroundColor: '#fff',
    color: '#454545',
  },
  itemsParent: {
    display: 'flex',
    flexDirection: 'row',
    alignItems: 'flex-start',
    justifyContent: 'flex-start',
    gap: '43px',
  },
  items: {
    width: '100px',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'flex-end',
    justifyContent: 'center',
    gap: '24px',
  },
  div1: {
    alignSelf: 'stretch',
    position: 'relative',
    lineHeight: '150%',
    fontWeight: '500',
    color: '#000',
  },
  page: {
    alignSelf: 'stretch',
    position: 'relative',
    lineHeight: '150%',
    fontWeight: '500',
  },
};
</script>
