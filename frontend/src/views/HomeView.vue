<template>
  <div class="top-half-background">
    <div class="home">
      <img src="@/assets/logo.jpg" class="logo">
      <h1>Cosmitaur</h1>
    </div>
    <div class="video-thumbnail">
      <a :href="youtubelink" target="_blank">
        <img :src="thumbnailUrl" :alt="videoTitle" />
      </a>
    </div>
    <div class="more1">
      <h2>Learn more --></h2>
      <img src="@/assets/logo.jpg" class="logom">
    </div>
    <div class="more2">
      <h2>Learn more --></h2>
      <img src="@/assets/logo.jpg" class="logom">
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      videoId: "1weAWiePcsQ",
      videoTitle: "A map of all steam users… Part 3"
    }
  },
  computed: {
    youtubelink() {
      return `https://www.youtube.com/watch?v=${this.videoId}`
    },
    thumbnailUrl() {
      return `https://img.youtube.com/vi/${this.videoId}/hqdefault.jpg`
    }
  }
}
</script>

<style>
.logo {
  width: 200px;
  height: 200px;
  margin-top: 80px;
  margin-right: 1000px;
  border-radius: 360px;
}

h1 {
  font-family: "Poppins", sans-serif;
  font-size: 130px;
  font-style: italic;
  font-weight: 200;
  margin-top: -180px;
  margin-left: 450px;
}

.video-thumbnail img {
  width: 100%;
  height: 100%;
  max-width: 500px;
  max-height: 250px;
  margin-right: 800px;
  margin-top: 10px;
  border-radius: 10px;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.video-thumbnail img:hover {
  transform: scale(1.05);
}

.more1 {
  display: flex;
  margin-top: -150px;
  margin-left: 1100px;
  align-items: center;
}

.logom {
  width: 140px;
  height: 140px;
}

body {
  margin: 0;
  padding: 0;
}

.top-half-background {
  background-image: url('@/assets/background1.png');
  background-position: top center;
  background-size: cover;
  background-attachment: fixed;
  height: 100vh; /* Only covers the top half of the viewport */
  width: 100%;
}
</style>
