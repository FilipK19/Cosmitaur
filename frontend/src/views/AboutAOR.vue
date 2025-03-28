<template>
  <div class="aboutA">
    <img src="@/assets/logo2.jpg" class="logo logo1 logoac">
  <div class="text">
    <div v-html="aboutAOR"></div>
  </div>
  <div class="more moreac">
      <p>Join the community →</p>
      <img src="@/assets/logo3.jpg" class="logom logom2">
    </div>
  </div>
</template>

<script>
import { aboutAOR } from '@/content/AboutAOR';

export default {
  data () {
    return {
      aboutAOR: aboutAOR
    }
  }
}
</script>

<style>
.aboutA {
  background-image: url('@/assets/bar2.png');
  background-position: top center;
  background-size: cover;
  height: 40vh;
  width: 100%;
  position: absolute;
  background-attachment: scroll; 
}
</style>