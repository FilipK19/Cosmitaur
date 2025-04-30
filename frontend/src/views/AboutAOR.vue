<template>
  <AosWrapper>
  <div class="aboutA">
    <AosWrapper>
      <img src="@/assets/logo2.jpg" class="logo logo1 logoac">
    </AosWrapper>
  </div>
</AosWrapper>
  <div class="aboutWT">
    <AosWrapper>
    <div class="text">
      <div v-html="aboutAOR"></div>
    </div>
    </AosWrapper>
    <AosWrapper>
    <div class="more moretW">
      <p>Join the community →</p>
      <img src="@/assets/logo3.jpg" class="logom logom2">
    </div>
    </AosWrapper>
  </div>
</template>

<script>
import { aboutAOR } from '@/content/AboutAOR';
import AosWrapper from '@/components/AosWrapper.vue';

export default {
  components: {
    AosWrapper,
  },
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