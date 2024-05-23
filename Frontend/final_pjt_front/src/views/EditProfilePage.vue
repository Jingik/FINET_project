<template>
  <div class="mypage-container">
    <div class="mypage">
      <div class="sidemenu">
      <RouterLink :to="{ name: 'DashBoardPage' }">
        <div class="sidemenu-item1">
          FINET 보드
        </div>
      </RouterLink>
        <RouterLink :to="{ name: 'ProfilePage' }">
        <div class="sidemenu-item1">
          내 활동 로그
        </div>
      </RouterLink>
      <RouterLink :to="{ name: 'EditProfilePage' }">
        <div class="sidemenu-item2">
          내 정보 수정
        </div>
      </RouterLink>
      <RouterLink :to="{ name: 'RecommendPage' }">
        <div class="sidemenu-item1">
          내 맞춤 상품
        </div>
      </RouterLink>
      </div>
      <div class="bigcontainer">
        <EditProfile />
        
      </div>
    </div>
  </div>
</template>

<script setup>
import EditProfile from "@/components/EditProfile.vue";
import { ref } from "vue";
</script>

<style scoped>

.mypage-container {
  margin : 0px auto;
  align-items: center;
  justify-content: center;
  padding: 20px;
  width: 1920px;
  align-items:center;
  left:50%
}
.smallcontainer{
  height:300px;
}

.mypage {
  margin : 60px auto;
  display: flex;
  flex-direction: row;
  padding: 20px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  border-radius: 20px;
  background-color: #0599f1;
  height: 700px;
  box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
  width: 1500px;
  margin-bottom: 20px;

}
.sidemenu {
  width:10%
}
.sidemenu-item1 {
  text-align: center;
  font-size: px;
  font-weight: bold;
  padding: 10px;
  margin-top: 20px;;
  height:50px;
  background-color: white;
  border-radius: 10px;
}
.sidemenu-item2 {
  font-size: 18px;
  box-shadow: 0 15px 30px 0 rgba(0, 0, 0, 0.2);
  text-align: center;
  font-weight: bold;
  padding: 10px;
  margin-top: 20px;;
  height:50px;
  background-color: white;
  border-radius: 10px;
}

/* .sidemenu-item3 {
  font-size: 18px;
  box-shadow: 0 15px 30px 0 rgba(0, 0, 0, 0.2);
  text-align: center;
  font-weight: bold;
  padding: 10px;
  margin-top: 20px;;
  height:50px;
  background-color: white;
  border-radius: 10px;
} */
.bigcontainer {
  display:flex;
  flex-direction: column;
  height:100%;
  width:90%;
}
</style>
