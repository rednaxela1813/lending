// frontend/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Landing from '../components/Landing.vue'
import LoginForm from '../components/LoginForm.vue'
import CounterpartyList from '../components/CounterpartyList.vue'

const routes = [
  { path: '/', component: Landing },
  { path: '/login', component: LoginForm },
  { path: '/dashboard', component: CounterpartyList },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

export default router
