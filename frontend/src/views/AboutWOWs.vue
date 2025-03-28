<template>
  <div class="aboutW">
    <img src="@/assets/logo5.jpg" class="logo logo1 logoac">
  <div class="text">
    <div v-html="aboutWOWs"></div>
  </div>
  <div class="more moreac">
      <p>WOWs the game →</p>
      <img src="@/assets/logo5.jpg" class="logom logom2">
    </div>
  </div>
</template>

<script>
import { aboutWOWs } from '@/content/AboutWOWs';

export default {
  data () {
    return {
      aboutWOWs: aboutWOWs
    }
  }
}
</script>

<style>
.aboutW {
  background-image: url('@/assets/bar3.png');
  background-position: top center;
  background-size: cover;
  height: 40vh;
  width: 100%;
  position: absolute;
  background-attachment: scroll; 
}
</style>