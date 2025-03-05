<template>
  <nav>
    <img src="@/assets/logo.jpg" class="logo">
    <router-link to="/">Home</router-link> |
    <router-link to="/aboutCosmitaur">About Cosmitaur</router-link> |
    <router-link to="/recentVideos">Recent Videos</router-link> |
    <router-link to="/aboutAOR">About AOR</router-link> |
    <router-link to="/aboutWOWs">About WOWs</router-link>
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  display: flex;
  justify-content: flex-start;
  align-items: center;
  gap: 10px;
  margin-left: -2%;
  margin-top: -2%;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

.logo {
  width: 40px;
  height: 40px;
}
</style>
