<template>
  <router-view />
  <div class="min-h-screen bg-gradient-to-br from-gray-100 to-gray-200 flex items-center justify-center p-4">
    <div class="w-full max-w-xl">
      <div class="text-center text-sm text-gray-500 mb-4">
        isAuthenticated: {{ isAuthenticated }}
      </div>
      <LoginForm v-if="!isAuthenticated" @loginSuccess="checkAuth" />
      <CounterpartyList v-else @logout="checkAuth" />
    </div>
  </div>
</template>


<script setup lang="ts">
import { ref, Ref, watch } from 'vue'
import LoginForm from './components/LoginForm.vue'
import CounterpartyList from './components/CounterpartyList.vue'

const isAuthenticated = ref(!!localStorage.getItem('access'))

watch(isAuthenticated, (val) => {
  console.log('👀 isAuthenticated изменён:', val)
})

const checkAuth = () => {
  const token = localStorage.getItem('access')
  console.log('🔁 Проверяем токен:', token)
  isAuthenticated.value = !!token
  console.log('🔁 isAuthenticated.value теперь:', isAuthenticated.value)
}
</script>
