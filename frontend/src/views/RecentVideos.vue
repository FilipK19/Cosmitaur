<template>
  <div class="background" id="section1">
    <AosWrapper>
    <div class="videos">
      <img src="@/assets/logo.jpg" class="logo logo1">
      <h1>Cosmitaur</h1>
    </div>
    <div class="info">
      <p>- Gaming videos, WOWs, GTA, Minecraft...</p>
      <p>- Funny videos</p>
      <p>- Space videos</p> 
    </div>
    </AosWrapper>
  </div>
  <div class="background recent_videos" id="section2-rv">
    <div class="gridrv">
      <div>
        <AosWrapper>
          <p class="v-type">Gaming:</p>
        </AosWrapper>
        <AosWrapper>
          <p class="v-type">Funny:</p>
        </AosWrapper>
        <AosWrapper>
          <p class="v-type">Space:</p>
        </AosWrapper>
      </div>
      <div class="gridrv-v">
        <div 
          v-for="(video, index) in videos" 
          :key="index" 
          class="video-thumbnail thumb_rv">
          <AosWrapper>
            <a :href="video.link" target="_blank" class="link">
            <img :src="video.thumbnail" :alt="'Video ' + video.id" />
            <span class="caption cpos">{{video.title}}</span>
            </a>
          </AosWrapper>
        </div>
      </div>
    </div>
  </div>
  </template>

<script>
import AosWrapper from '@/components/AosWrapper.vue';

export default {
  components: {
    AosWrapper,
  },
  data () {
    return {
      videos: [],
    };
  },
  methods: {
    async fetch_rvvideos() {
      try {
        const response = await fetch('http://localhost:8000/rvvideos');
        const data = await response.json();
        
        if (data.rv_videos) {
          // Transform the object into an array of video objects
          this.videos = Object.keys(data.rv_videos).map((key) => {
            const { id: videoId, title: videoTitle } = data.rv_videos[key];
            return {
              id: videoId,
              title: videoTitle,
              link: `https://www.youtube.com/watch?v=${videoId}`,
              thumbnail: `https://img.youtube.com/vi/${videoId}/hqdefault.jpg`
            };
          });
        } else {
          console.error('No videos found in response');
        }
      } catch (error) {
        console.error('Error fetching videos:', error);
      }
    }
  },
  mounted() {
    this.fetch_rvvideos();
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
  background-color: #f1f1ef;
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
  font-size: 25px;
}
</style>