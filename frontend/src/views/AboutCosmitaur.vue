<template>
  <div class="aboutC">
    <img src="@/assets/logo.jpg" class="logo logo1 logoac">
  <div class="text">
    <div v-html="aboutCosmitaur"></div>
  </div>
  <div class="more moreac">
      <p>Subscribe →</p>
      <img src="@/assets/logo.jpg" class="logomac">
    </div>
  </div>
</template>

<script>
import { aboutCosmitaur } from '@/content/AboutCosmitaur';

export default {
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
}

.text {
  max-width: 80%;
  margin: 12vh auto 2vh auto;
  font-size: 1.6rem;
  line-height: 1.6;
  text-align: left;
}

.text p {
  margin-bottom: 4vh;
  text-align: justify;
}

.moreac {
  margin-top: 15vh;
  padding-bottom: 15vh;
  margin-left: 155vh;
}

.logomac {
  border: 1px solid black;
  max-width: 120px;
  height: auto;
}

.logoac {
  margin-right: 155vh;
  margin-top: 8vh;
}
</style>