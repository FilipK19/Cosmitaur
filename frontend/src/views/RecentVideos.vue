<template>
  <div class="background" id="section1">
    <div class="videos">
      <img src="@/assets/logo.jpg" class="logo logo1">
      <h1>Cosmitaur</h1>
    </div>
    <div class="info">
      <p>- Gaming videos, WOWs, GTA, Minecraft...</p>
      <p>- Funny videos</p>
      <p>- Space videos</p> 
    </div>
  </div>
  <div class="background recent_videos" id="section2-rv">
    <div class="gridrv">
      <p1>Gaming:</p1>
      <div class="gridrv-v">
        <div class="video-thumbnail thumb_rv">
          <a :href="youtubelink" target="_blank" class="link">
            <img :src="thumbnailUrl" :alt="videoTitle" />
          </a>
        </div>
        <div class="video-thumbnail thumb_rv">
          <a :href="youtubelink2" target="_blank" class="link">
            <img :src="thumbnailUrl2" :alt="videoTitle" />
          </a>
        </div>
        <div class="video-thumbnail thumb_rv">
          <a :href="youtubelink3" target="_blank" class="link">
            <img :src="thumbnailUrl3" :alt="videoTitle" />
          </a>
        </div>
      </div>
    </div>
    <div class="gridrv">
      <p1>Funny:</p1>
      <div class="gridrv-v">
        <div class="video-thumbnail thumb_rv">
          <a :href="youtubelink4" target="_blank" class="link">
            <img :src="thumbnailUrl4" :alt="videoTitle" />
          </a>
        </div>
        <div class="video-thumbnail thumb_rv">
          <a :href="youtubelink5" target="_blank" class="link">
            <img :src="thumbnailUrl5" :alt="videoTitle" />
          </a>
        </div>
        <div class="video-thumbnail thumb_rv">
          <a :href="youtubelink6" target="_blank" class="link">
            <img :src="thumbnailUrl6" :alt="videoTitle" />
          </a>
        </div>
      </div>
    </div>
    <div class="gridrv">
      <p1>Space:</p1>
      <div class="gridrv-v">
        <div class="video-thumbnail thumb_rv">
          <a :href="youtubelink7" target="_blank" class="link">
            <img :src="thumbnailUrl7" :alt="videoTitle" />
          </a>
        </div>
        <div class="video-thumbnail thumb_rv">
          <a :href="youtubelink8" target="_blank" class="link">
            <img :src="thumbnailUrl8" :alt="videoTitle" />
          </a>
        </div>
        <div class="video-thumbnail thumb_rv">
          <a :href="youtubelink9" target="_blank" class="link">
            <img :src="thumbnailUrl9" :alt="videoTitle" />
          </a>
        </div>
      </div>
    </div>
  </div>
  </template>

<script>
export default {
  data () {
    return {
      videoId: "q_TG6vNJPJE",
      videoId2: "FAB1xEe1A1c",
      videoId3: "4BpSUmOVr_4",
      videoId4: "dSlxRQ_u8RE",
      videoId5: "pe9OQaaiqNI",
      videoId6: "enQrOaZLC70",
      videoId7: "PQfkvC6RASA",
      videoId8: "GtUaeNQCqmM",
      videoId9: "QNv2aCh7MHc",
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
    youtubelink5() {
      return `https://www.youtube.com/watch?v=${this.videoId5}`
    },
    youtubelink6() {
      return `https://www.youtube.com/watch?v=${this.videoId6}`
    },
    youtubelink7() {
      return `https://www.youtube.com/watch?v=${this.videoId7}`
    },
    youtubelink8() {
      return `https://www.youtube.com/watch?v=${this.videoId8}`
    },
    youtubelink9() {
      return `https://www.youtube.com/watch?v=${this.videoId9}`
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
    },
    thumbnailUrl5() {
      return `https://img.youtube.com/vi/${this.videoId5}/hqdefault.jpg`
    },
    thumbnailUrl6() {
      return `https://img.youtube.com/vi/${this.videoId6}/hqdefault.jpg`
    },
    thumbnailUrl7() {
      return `https://img.youtube.com/vi/${this.videoId7}/hqdefault.jpg`
    },
    thumbnailUrl8() {
      return `https://img.youtube.com/vi/${this.videoId8}/hqdefault.jpg`
    },
    thumbnailUrl9() {
      return `https://img.youtube.com/vi/${this.videoId9}/hqdefault.jpg`
    }
  }
}
</script>

<style>
body {
  overflow-x: hidden; /* Hide scrollbars */
}

.video-thumbnail img {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  object-fit: cover;
  transition: transform 0.5s ease;
}

.thumb_rv img {
  height: 200px;
  width: 400px;
}

.gridrv {
  margin-top: 100px;
  display: grid;
  grid-template-columns: repeat(2, 200px);
  margin-bottom: 150px;
}

.gridrv-v {
  display: grid;
  grid-template-columns: repeat(3, 0);
  column-gap: 500px;
}

p1 {
  font-size: 25px;
  margin-top: 60px;
}

.recent_videos {
  padding-bottom: 300px;
  background-color: #dddddd;
}

#section2-rv {
  top: 100vh;
}
</style>