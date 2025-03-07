<template>
  <nav>
    <img src="@/assets/logo.jpg" class="mlogo">
    <router-link to="/">Home</router-link>
    <router-link to="/aboutCosmitaur">About Cosmitaur</router-link>
    <router-link to="/recentVideos">Recent Videos</router-link>
    <router-link to="/aboutAOR">About AOR</router-link>
    <router-link to="/aboutWOWs">About WOWs</router-link>
  </nav>
  <router-view/>
</template>

<style>
#app {
  text-align: center;
}

nav {
  position: fixed;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 30px;
  background-color: #ffffff;
  width: 100%;
  z-index: 1000;
  top: 0; /* Ensure it stays at the top */
  left: 0;
  right: 0;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
  text-decoration: none;
}

.mlogo {
  width: 40px;
  height: 40px;
}
</style>
