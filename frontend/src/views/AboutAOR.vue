<template>
  <div class="about2">
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
.about2 {
  background-image: url('@/assets/bar2.png');
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
  margin-left: 160vh;
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