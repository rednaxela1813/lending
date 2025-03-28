<template>
    <div class="bg-white min-h-screen px-6 pt-16">
      <div class="max-w-5xl mx-auto text-center">
        <h1 class="text-4xl sm:text-6xl font-bold text-gray-900">
          Современный учёт для малого бизнеса
        </h1>
        <p class="mt-6 text-lg text-gray-600">
          Управляй своими финансами, клиентами и поставщиками — всё в одном месте.
        </p>
        <div class="mt-8 flex justify-center gap-4">
          <RouterLink
            to="/login"
            class="bg-blue-600 text-white px-6 py-3 rounded-lg text-lg hover:bg-blue-700 transition"
          >
            Начать сейчас
          </RouterLink>
          <a
            href="#"
            class="bg-gray-100 text-gray-800 px-6 py-3 rounded-lg text-lg hover:bg-gray-200 transition"
          >
            Подробнее
          </a>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { RouterLink } from 'vue-router'
  </script>
  