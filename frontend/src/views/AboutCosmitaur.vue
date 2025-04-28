<template>
  <div class="aboutC">
    <AosWrapper>
      <img src="@/assets/logo.jpg" class="logo logo1 logoac">
    </AosWrapper>
  </div>
  <div class="aboutC2">
    <AosWrapper>
    <div class="text">
      <div v-html="aboutCosmitaur"></div>
    </div>
  </AosWrapper>
    <AosWrapper>
    <div class="more moreac">
      <p>Subscribe →</p>
      <img src="@/assets/logo.jpg" class="logomac">
    </div>
    </AosWrapper>
  </div>
</template>

<script>
import { aboutCosmitaur } from '@/content/AboutCosmitaur';
import AosWrapper from '@/components/AosWrapper.vue';

export default {
  components: {
    AosWrapper,
  },
  data () {
    return {
      aboutCosmitaur: aboutCosmitaur
    }
  }
}
</script>

<style>
.aboutC {
  background-image: url('@/assets/bar1.jpg');
  background-position: top center;
  background-size: cover;
  height: 40vh;
  width: 100%;
  position: absolute;
  background-attachment: scroll;
  overflow: hidden;
}

.aboutC2 {
  height: 120vh;
  position: absolute;
  top: 40vh;
  overflow: hidden;
}

.text {
  max-width: 80%;
  margin: 12vh auto 2vh auto;
  font-size: 25px;
  line-height: 1.6;
  text-align: left;
}

.text p {
  margin-bottom: 4vh;
  text-align: justify;
}

.moreac {
  margin-top: 105px;
  margin-left: 1200px;
}

.logomac {
  border: 1px solid black;
  max-width: 120px;
  height: auto;
}

.logoac {
  margin-right: 1200px;
  margin-top: 60px;
}
</style>