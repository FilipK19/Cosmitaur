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
      <div>
        <p class="v-type">Gaming:</p>
        <p class="v-type">Funny:</p>
        <p class="v-type">Space:</p>
      </div>
      <div class="gridrv-v">
        <div 
          v-for="(video, index) in videos" 
          :key="index" 
          class="video-thumbnail thumb_rv">
          <a :href="video.link" target="_blank" class="link">
          <img :src="video.thumbnail" :alt="'Video ' + video.id" />
          <span class="caption cpos">{{video.title}}</span>
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
      videos: [],
    };
  },
  methods: {
    async fetchUrls() {
      try {
        const response = await fetch('http://localhost:8000/url');
        const data = await response.json();
        
        if (data.urls) {
          // Transform the object into an array of video objects
          this.videos = Object.keys(data.urls).map((key) => {
            const { id: videoId, title: videoTitle } = data.urls[key];
            return {
              id: videoId,
              title: videoTitle,
              link: `https://www.youtube.com/watch?v=${videoId}`,
              thumbnail: `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`
            };
          });
        } else {
          console.error('No URLs found in response');
        }
      } catch (error) {
        console.error('Error fetching URLs:', error);
      }
    }
  },
  mounted() {
    this.fetchUrls();
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
  transition: transform 0.5s ease, filter 0.5s ease;
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
  margin-bottom: 100px;
}

.v-type {
  font-size: 25px;
  margin-top: 80px;
  margin-bottom: 220px;
}

.recent_videos {
  padding-bottom: 300px;
  background-color: #dddddd;
}

#section2-rv {
  top: 100vh;
}

.video-thumbnail.thumb_rv,
.video-thumbnail.thumb_rv .link {
  position: relative;
  display: inline-block;
}

.cpos {
  position: absolute;
  inset: 0; 
  display: flex;
  justify-content: center;
  align-items: center;
  pointer-events: none;
}
</style>