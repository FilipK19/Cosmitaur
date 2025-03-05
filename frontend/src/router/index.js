import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutCosmitaur from '@/views/AboutCosmitaur.vue'
import RecentVideos from '@/views/RecentVideos.vue'
import AboutAOR from '@/views/AboutAOR.vue'
import AboutWOWs from '@/views/AboutWOWs.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/aboutCosmitaur',
    name: 'aboutCosmitaur',
    component: AboutCosmitaur
  },
  {
    path: '/recentVideos',
    name: 'recentVideos',
    component: RecentVideos
  },
  {
    path: '/aboutAOR',
    name: 'aboutAOR',
    component: AboutAOR
  },
  {
    path: '/aboutWOWs',
    name: 'aboutWOWs',
    component: AboutWOWs
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
