<template>
  <div class="min-h-screen bg-white flex items-center justify-center px-4">
    <div class="w-full max-w-md space-y-6">
      <!-- Заголовок -->
      <div class="text-center">
        <h1 class="text-3xl font-bold tracking-tight text-gray-900">Вход в аккаунт</h1>
        <p class="text-sm text-gray-500 mt-1">Введите свои данные, чтобы продолжить</p>
      </div>

      <!-- Форма -->
      <form @submit.prevent="login" class="bg-white border border-gray-200 shadow-sm rounded-xl p-6 space-y-4">
        <div>
          <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
          <input
            id="email"
            v-model="email"
            type="email"
            required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>
        <div>
          <label for="password" class="block text-sm font-medium text-gray-700">Пароль</label>
          <input
            id="password"
            v-model="password"
            type="password"
            required
            class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-lg shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500"
          />
        </div>

        <button
          type="submit"
          class="w-full bg-blue-600 text-white font-medium py-2 rounded-lg hover:bg-blue-700 transition"
        >
          Войти
        </button>

        <p v-if="error" class="text-red-600 text-sm text-center mt-2">{{ error }}</p>
      </form>

      <!-- Подвал (опционально) -->
      <p class="text-center text-sm text-gray-400">
        Нет аккаунта? <a href="#" class="text-blue-600 hover:underline">Зарегистрируйтесь</a>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

const emit = defineEmits(['loginSuccess'])

const email = ref('')
const password = ref('')
const error = ref(null)

const login = async () => {
  error.value = null
  try {
    const response = await axios.post('http://127.0.0.1:8000/api/auth/login/', {
      email: email.value,
      password: password.value
    })

    const { access, refresh } = response.data
    localStorage.setItem('access', access)
    localStorage.setItem('refresh', refresh)

    email.value = ''
    password.value = ''

    console.log('✅ Логин прошёл, токен сохранён')
    emit('loginSuccess')
  } catch (err) {
    console.error('❌ Ошибка входа:', err.response?.data || err)
    error.value = err.response?.data?.detail || 'Ошибка входа'
  }
}
</script>
