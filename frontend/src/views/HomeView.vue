<template>
  <div class="background" id="section1">
    <div class="home">
      <img src="@/assets/logo.jpg" class="logo logo1">
      <h1>Cosmitaur</h1>
    </div>
    <div v-if="hvideos.videoId1" class="video-thumbnail thumb1">
      <p class="video-label label1">New video:</p>
      <a :href="hvideos.videoId1.link" target="_blank" class="link">
        <img :src="hvideos.videoId1.thumbnail"/>
        <span class="caption cpos_m">{{hvideos.videoId1.title}}</span>
      </a>
    </div>
    <div class="more more1">
      <p>Learn more →</p>
      <router-link to="/aboutCosmitaur">
        <img src="@/assets/logo.jpg" class="logom">
      </router-link>
    </div>
    More info ↓
  </div>
  <div class="background" id="section2">
    <h2>Cosmitaur videos</h2>
    <div class="grid">
      <div v-if="hvideos.videoId2" class="video-thumbnail thumbm thumb2">
        <p class="video-label label2">Gaming:</p>
        <a :href="hvideos.videoId2.link" target="_blank" class="link">
          <img :src="hvideos.videoId2.thumbnail"/>
          <span class="caption cpos_cv">{{hvideos.videoId2.title}}</span>
        </a>
      </div>
      <div v-if="hvideos.videoId3" class="video-thumbnail thumbm thumb3">
        <p class="video-label label2">Funny moments:</p>
        <a :href="hvideos.videoId3.link" target="_blank" class="link">
          <img :src="hvideos.videoId3.thumbnail"/>
          <span class="caption cpos_cv cpos_cv2">{{hvideos.videoId3.title}}</span>
        </a>
      </div>
      <div v-if="hvideos.videoId4" class="video-thumbnail thumbm thumb4">
        <p class="video-label label2 label4">Space:</p>
        <a :href="hvideos.videoId4.link" target="_blank" class="link">
          <img :src="hvideos.videoId4.thumbnail"/>
          <span class="caption cpos_cv cpos_cv3">{{hvideos.videoId4.title}}</span>
        </a>
      </div>
      <div class="more more2">
        <p>Learn more →</p>
        <router-link to="/recentVideos">
          <img src="@/assets/logo.jpg" class="logom">
        </router-link>
      </div>
    </div>
  </div>
  <div class="background" id="section3">
    <div class="home2">
      <img src="@/assets/logo2.jpg" class="logo logo1">
      <h3>Academy of Revenge</h3>
    </div>
  <div class="grid2">
    <div class="info">
      <p>- Leading WOWs clan</p>
      <p>- Friendly members</p>
      <p>- Weekly clan battles</p>
      <p>- Welcoming members</p>
    </div>
    <div>
      <div class="more more3 more4">
          <p>Learn more →</p>
          <router-link to="/aboutAOR">
            <img src="@/assets/logo2.jpg" class="logom">
          </router-link>
      </div>
      <div class="more more3">
          <p>Join the community →</p>
          <a href="https://discord.com/invite/3QqPtfW">
            <img src="@/assets/logo3.jpg" class="logom logom2">
          </a>
      </div>
    </div>
  </div>
  </div>
  <div class="background" id="section4">
    <h4>World of Warships</h4>
    <div class="grid2 grid3">
      <div class="info2">
        <div class="info">
          <p>- Sail the high seas</p>
          <p>- Battle with legendary warships</p>
          <p>- Command the sea</p>
        </div>
        <div class="more more3">
            <p>Clan stats →</p>
            <img src="@/assets/logo6.jpg" class="logom">
        </div>
      </div>
    <div class="extra">
      <div class="more more3 more5">
          <p>Learn more →</p>
          <router-link to="/aboutCosmitaur">
            <img src="@/assets/logo4.jpg" class="logom">
          </router-link>
      </div>
      <div class="more more3">
          <p>WOWs the game →</p>
          <a href="https://worldofwarships.eu/">
            <img src="@/assets/logo5.jpg" class="logom logom2">
          </a>
      </div>
    </div>
  </div>
  </div>
  <div class="background" id="section5">
    <h5>Contact us</h5>
    <div class="home3">
      <img src="@/assets/logo.jpg" class="logo logo2">
      <img src="@/assets/logo2.jpg" class="logo logo2">
    </div>
    <div class="contact">
      <div class="container">
        <label for="nameInput" class="tlabel">Name:</label>
        <input type="text" id="nameInput" v-model="name" class="tbox" />
      </div>
      <div class="container">
        <label for="emailInput" class="tlabel">email:</label>
        <input type="text" id="emailInput" v-model="email" class="tbox" />
      </div>
      <div class="container">
        <label for="messageInput" class="tlabel">Message:</label>
        <input type="text" id="messageInput" v-model="message" class="tbox tbox3" />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      hvideos: {},
    };
  },
  methods: {
    async fetc_homevideos() {
      try {
        const response = await fetch('http://localhost:8000/homevideos');
        const data = await response.json();
        
        if (data.home_videos) {
          // Transform the object into an array of video objects
          Object.keys(data.home_videos).forEach((key) => {
            const { id: videoId, title: videoTitle } = data.home_videos[key];
            this.hvideos[key] = {
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
        console.error('Error fetching URLs:', error);
      }
    }
  },
  mounted() {
    this.fetc_homevideos();
  }
}
</script>

<style>
.logo {
  width: 200px;
  height: 200px;
  border-radius: 50%;
}

.logo1 {
  margin-top: 80px;
  margin-right: 1000px;
}

h1, h2, h3, h4, h5 {
  font-family: "Poppins", sans-serif;
  font-style: italic;
}

h1, h3 {
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

h3 {
  font-size: 80px;
  margin-top: -140px;
}

h4 {
  font-size: 80px;
  margin-top: 100px;
  font-weight: 200;
}

h5 {
  font-weight: 100;
  font-size: 70px;
  margin-right: 1000px;
}

.video-thumbnail img {
  width: 100%;
  height: 100%;
  border-radius: 10px;
  object-fit: cover;
  filter: brightness(100%);
  transform: scale(1);
  transition: transform 0.5s ease, filter 0.5s ease;
}

.video-thumbnail img:hover {
  filter: brightness(50%);
  transform: scale(1.05);
}

.video-thumbnail {
  position: relative;
}

.video-thumbnail .caption{
  position: absolute;
  inset: 0;
  display: flex;
  text-shadow: 0 2px 4px rgb(0 0 0 / .6);

  color: #fff;
  font-weight: 600;

  opacity: 0;
  transition: opacity .5s ease;
  pointer-events: none;
}

.cpos_m {
  margin-top: 210px;
  margin-left: 210px;
  font-size: 28px;
}

.cpos_cv {
  position: absolute;
  inset: 0; 
  display: flex;
  justify-content: center;
  align-items: center;
  pointer-events: none;
  font-size: 20px;
  margin-top: 50px;
  max-width: 300px;
  margin-left: 270px;
}

.cpos_cv2 {
  margin-top: 40px;
}

.cpos_cv3 {
  margin-top: 80px;
}

.video-thumbnail .link:hover .caption{
  opacity: 1;
}

.video-label {
  font-size: 28px;
  font-weight: bold;
  padding: 5px 10px;
  position: absolute;
}

.label1 {
  top: 30px;
  margin-left: 150px;
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
  margin-top: 100px;
  margin-right: 900px;
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

.grid2 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
}

.grid3{
  margin-top: -20px;
}

.home3 {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  max-width: 700px;
  margin-left: 900px;
  margin-top: -250px;
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

.more {
  display: flex;
  align-items: center;
  font-size: 25px;
  position: relative;
  z-index: 10; /*stack on top */
}

.more1 {
  margin-top: -150px;
  margin-left: 1200px;
}

.more2 {
  margin-top: 140px;
  margin-left: 300px;
}

.more3 {
  margin-left: 200px;
  margin-top: 50px;
}

.more4 {
  padding-left: 80px;
}

.more5 {
  padding-left: 55px;
}

.logom {
  width: 140px;
  height: 140px;
}

.logom2 {
  width: 220px;
}

body {
  margin: 0;
  padding: 0;
}

.background {
  background-position: top center;
  background-size: cover;
  background-attachment: fixed;
  height: 100vh; /* Only covers the top half of the viewport */
  width: 100%;
  position: absolute;
  background-attachment: scroll; /* Change from fixed to scroll */
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

#section5 {
  background-image: url('@/assets/background4.png');
  top: 400vh;
}

.home2 {
  margin-top: 30px;
}

.info {
  padding-left: 200px;
  margin-top: 100px;
  font-size: 28px;
  display: flex;
  flex-direction: column;
  align-items: start;
}

.info2 {
  margin-top: -50px;
}

p {
  margin: 14px; /* Removes default margin */
}

.extra {
  margin-top: 30px;
}

.contact {
  margin-right: 1500px;
  padding-left: 150px;
}

.container {
  display: flex;
  flex-direction: column;
  margin-bottom: 40px;
}

.tlabel {
  font-size: 16px;
  font-weight: bold;
  margin-bottom: 5px;
}

.tbox {
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 400px;
  height: 25px;
}

.tbox3 {
  height: 150px;
}

</style>
