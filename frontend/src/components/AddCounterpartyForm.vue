<template>
    <form @submit.prevent="submit" class="mb-6 p-4 bg-white rounded shadow space-y-4">
      <div>
        <label class="block text-sm font-medium">Название</label>
        <input v-model="form.name" required class="w-full border px-3 py-2 rounded" />
      </div>
  
      <div>
        <label class="block text-sm font-medium">Тип</label>
        <select v-model="form.type" required class="w-full border px-3 py-2 rounded">
          <option value="client">Клиент</option>
          <option value="supplier">Поставщик</option>
        </select>
      </div>
  
      <div>
        <label class="block text-sm font-medium">Телефон</label>
        <input v-model="form.contact_phone" class="w-full border px-3 py-2 rounded" />
      </div>
  
      <div>
        <label class="block text-sm font-medium">Email</label>
        <input v-model="form.contact_email" type="email" class="w-full border px-3 py-2 rounded" />
      </div>
  
      <div>
        <label class="block text-sm font-medium">Адрес</label>
        <input v-model="form.address" class="w-full border px-3 py-2 rounded" />
      </div>
  
      <div>
        <label class="block text-sm font-medium">Менеджер</label>
        <input v-model="form.manager" class="w-full border px-3 py-2 rounded" />
      </div>
  
      <div>
        <label class="block text-sm font-medium">Заметка</label>
        <textarea v-model="form.note" class="w-full border px-3 py-2 rounded"></textarea>
      </div>
  
      <button type="submit" class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700">
        Добавить
      </button>
  
      <p v-if="error" class="text-red-600 mt-2">{{ error }}</p>
    </form>
  </template>
  
  <script setup>
  import { ref } from 'vue'
  import axios from 'axios'
  
  const emit = defineEmits(['created'])
  
  const form = ref({
    name: '',
    type: 'client',
    contact_phone: '',
    contact_email: '',
    address: '',
    manager: '',
    note: ''
  })
  
  const error = ref(null)
  
  const submit = async () => {
    error.value = null
    const token = localStorage.getItem('access')
  
    try {
      await axios.post('http://127.0.0.1:8000/api/counterparty/', form.value, {
        headers: {
          Authorization: `Bearer ${token}`
        }
      })
      emit('created') // уведомляем родителя
      Object.keys(form.value).forEach((key) => form.value[key] = '') // очищаем форму
    } catch (err) {
      console.error('Ошибка создания контрагента:', err)
      error.value = 'Ошибка создания. Проверьте поля.'
    }
  }
  </script>
  