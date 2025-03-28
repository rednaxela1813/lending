<template>
  <div class="p-6 space-y-6">
    <div class="flex justify-between items-center">
      <h1 class="text-2xl font-bold">Контрагенты</h1>
      <button @click="logout" class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded">
        Выйти
      </button>
    </div>

    <!-- Кнопка "Добавить контрагента" -->
    <div class="text-right">
      <button
        @click="showForm = !showForm"
        class="bg-green-600 text-white px-4 py-2 rounded hover:bg-green-700 transition"
      >
        {{ showForm ? 'Отмена' : 'Добавить контрагента' }}
      </button>
    </div>

    <!-- Условное отображение формы -->
    <AddCounterpartyForm v-if="showForm" @created="handleCreated" />

    <!-- Список контрагентов -->
    <table class="min-w-full border border-gray-300 text-sm">
      <thead class="bg-gray-100">
        <tr>
          <th class="p-2 border">Название</th>
          <th class="p-2 border">Тип</th>
          <th class="p-2 border">Телефон</th>
          <th class="p-2 border">Email</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in counterparties" :key="item.public_id" class="hover:bg-gray-50">
          <td class="p-2 border">{{ item.name }}</td>
          <td class="p-2 border">{{ item.type }}</td>
          <td class="p-2 border">{{ item.contact_phone }}</td>
          <td class="p-2 border">{{ item.contact_email }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import AddCounterpartyForm from './AddCounterpartyForm.vue'

const emit = defineEmits(['logout'])

const counterparties = ref([])
const showForm = ref(false)

const fetchCounterparties = async () => {
  const token = localStorage.getItem('access')
  if (!token) return

  try {
    const response = await axios.get('http://127.0.0.1:8000/api/counterparty/', {
      headers: {
        Authorization: `Bearer ${token}`
      }
    })
    counterparties.value = response.data
  } catch (error) {
    console.error('Ошибка загрузки контрагентов:', error)
  }
}

const handleCreated = () => {
  fetchCounterparties()
  showForm.value = false
}

const logout = () => {
  localStorage.removeItem('access')
  localStorage.removeItem('refresh')
  emit('logout')
}

onMounted(fetchCounterparties)
</script>
