<template>
  <AosWrapper>
  <div class="aboutW">
    <AosWrapper>
    <img src="@/assets/logo5.jpg" class="logo logo1 logoac">
    </AosWrapper>
  </div>
</AosWrapper>
  <div class="aboutWT">
    <AosWrapper>
      <div class="text">
      <div v-html="aboutWOWs"></div>
    </div>
    </AosWrapper>
    <AosWrapper>
      <div class="more moretW">
      <p>WOWs the game →</p>
      <img src="@/assets/logo5.jpg" class="logom logom2">
    </div>
    </AosWrapper>
  </div>
</template>

<script>
import { aboutWOWs } from '@/content/AboutWOWs';
import AosWrapper from '@/components/AosWrapper.vue';

export default {
  components: {
    AosWrapper,
  },
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

.aboutWT {
  height: 150vh;
  position: absolute;
  top: 40vh;
  overflow: hidden;
}

.moretW {
  margin-top: 120px;
  margin-left: 1100px;
}
</style>