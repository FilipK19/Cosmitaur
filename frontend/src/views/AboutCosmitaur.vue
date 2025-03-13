<template>
  <div class="about">
    <img src="@/assets/logo.jpg" class="logo logo1 logoac">
  <div class="text">
    <div v-html="aboutCosmitaur"></div>
  </div>
  <div class="more more1 moreac">
      <p>Subscribe →</p>
      <img src="@/assets/logo.jpg" class="logom logomac">
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
.about {
  background-image: url('@/assets/bar1.jpg');
  background-position: top center;
  background-size: cover;
  background-attachment: fixed;
  height: 40vh;
  width: 100%;
  position: absolute;
  background-attachment: scroll; 
}

.text {
  max-width: 1300px;
  margin: 100px auto 20px auto;
  font-size: 25px;
  line-height: 1.6;
  text-align: left;
}

.text p {
  margin-bottom: 25px;
  text-align: justify;
}

.moreac {
  margin-top: 100px;
  padding-bottom: 100px;
}

.logomac {
  border: 1px solid black;
}

.logoac {
  margin-right: 1200px;
  margin-top: 60px;
}
</style>