<template>
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
  margin-top: 10px;
  margin-right: 1000px;
}

h1 {
  font-size: 120px;
  font-style: italic;
  font-weight: 100;
  margin-top: -160px;
  margin-left: 500px;
}

.video-thumbnail img {
  width: 100%;
  height: 100%;
  max-width: 500px;
  max-height: 250px;
  margin-right: 800px;
  margin-top: 50px;
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
  width: 180px;
  height: 180px;
}
</style>
