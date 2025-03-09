<template>
  <div class="background" id="section1">
    <div class="home">
      <img src="@/assets/logo.jpg" class="logo">
      <h1>Cosmitaur</h1>
    </div>
    <div class="video-thumbnail thumb1">
      <p class="video-label label1">New video:</p>
      <a :href="youtubelink" target="_blank">
        <img :src="thumbnailUrl" :alt="videoTitle" />
      </a>
    </div>
    <div class="more more1">
      <p>Learn more →</p>
      <img src="@/assets/logo.jpg" class="logom">
    </div>
    More info ↓
  </div>
  <div class="background" id="section2">
    <h2>Cosmitaur videos</h2>
    <div class="grid">
      <div class="video-thumbnail thumbm thumb2">
        <p class="video-label label2">Gaming:</p>
        <a :href="youtubelink2" target="_blank">
          <img :src="thumbnailUrl2" :alt="videoTitle" />
        </a>
      </div>
      <div class="video-thumbnail thumbm thumb3">
        <p class="video-label label2">Funny moments:</p>
        <a :href="youtubelink3" target="_blank">
          <img :src="thumbnailUrl3" :alt="videoTitle" />
        </a>
      </div>
      <div class="video-thumbnail thumbm thumb4">
        <p class="video-label label2 label4">Space:</p>
        <a :href="youtubelink4" target="_blank">
          <img :src="thumbnailUrl4" :alt="videoTitle" />
        </a>
      </div>
      <div class="more more2">
        <p>Learn more →</p>
        <img src="@/assets/logo.jpg" class="logom">
      </div>
    </div>
  </div>
  <div class="background" id="section3">
    <h3>Academy of revenge</h3>
  </div>
  <div class="background" id="section4">
    <h4>Academy of revenge</h4>
  </div>
</template>

<script>
export default {
  data () {
    return {
      videoId: "1weAWiePcsQ",
      videoId2: "GtUaeNQCqmM",
      videoId3: "dSlxRQ_u8RE",
      videoId4: "PQfkvC6RASA",
      videoTitle: "A map of all steam users… Part 3"
    }
  },
  computed: {
    youtubelink() {
      return `https://www.youtube.com/watch?v=${this.videoId}`
    },
    youtubelink2() {
      return `https://www.youtube.com/watch?v=${this.videoId2}`
    },
    youtubelink3() {
      return `https://www.youtube.com/watch?v=${this.videoId3}`
    },
    youtubelink4() {
      return `https://www.youtube.com/watch?v=${this.videoId4}`
    },
    thumbnailUrl() {
      return `https://img.youtube.com/vi/${this.videoId}/hqdefault.jpg`
    },
    thumbnailUrl2() {
      return `https://img.youtube.com/vi/${this.videoId2}/hqdefault.jpg`
    },
    thumbnailUrl3() {
      return `https://img.youtube.com/vi/${this.videoId3}/hqdefault.jpg`
    },
    thumbnailUrl4() {
      return `https://img.youtube.com/vi/${this.videoId4}/hqdefault.jpg`
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

h1, h2 {
  font-family: "Poppins", sans-serif;
  font-style: italic;
}

h1 {
  font-size: 130px;
  margin-top: -180px;
  margin-left: 450px;
  font-weight: 200;
}

h2 {
  font-size: 70px;
  font-weight: 100;
  margin: 0;
  margin-top: 75px;
}

.video-thumbnail img {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.video-label {
  font-size: 28px;
  font-weight: bold;
  padding: 5px 10px;
  position: absolute;
}
.video-thumbnail {
  position: relative;
  display: inline-block;
}

.label1 {
  top: 30px;
}

.label2 {
  left: 260px;
  top: 10px;
}

.label4 {
  top: 30px;
}

.thumb1 img {
  max-width: 500px;
  max-height: 250px;
  margin-right: 800px;
  margin-top: 100px;
}

.thumbm img {
  max-width: 320px;
  max-height: 170px;
}

.grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  grid-template-rows: repeat(2, 1fr);
}

.thumb2 img {
  margin-top: 80px;
}

.thumb3 img {
  margin-top: 80px;
}

.thumb4 img {
  margin-top: 100px;
}

.video-thumbnail img:hover {
  transform: scale(1.05);
}

.more {
  display: flex;
  align-items: center;
  font-size: 25px;
}

.more1 {
  margin-top: -150px;
  margin-left: 1200px;
}

.more2 {
  margin-top: 140px;
  margin-left: 300px;
}

.logom {
  width: 140px;
  height: 140px;
}

body {
  margin: 0;
  padding: 0;
}

.background {
  background-image: url('@/assets/background1.png');
  background-position: top center;
  background-size: cover;
  background-attachment: fixed;
  height: 100vh; /* Only covers the top half of the viewport */
  width: 100%;
  position: absolute;
}

#section1 {
  background-image: url('@/assets/background1.png');
}

#section2 {
  background-image: url('@/assets/background2.png');
  top: 100vh;
}

#section3 {
  background-image: url('@/assets/background3.png');
  top: 200vh;
}

#section4 {
  background-image: url('@/assets/background3.png');
  top: 300vh;
}
</style>
