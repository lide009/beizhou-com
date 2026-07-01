<template>
  <nav class="bg-white shadow-md fixed top-0 left-0 right-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <router-link to="/" class="flex items-center space-x-2">
            <img src="/北州logo.jpg" alt="北州芯片科技" class="w-10 h-10 rounded-lg object-cover">
            <span class="text-xl font-bold text-gray-800">北州芯片科技</span>
          </router-link>
        </div>

        <div class="hidden md:flex items-center space-x-8">
          <router-link 
            v-for="item in navItems" 
            :key="item.name"
            :to="item.path"
            class="text-gray-600 hover:text-primary transition-colors duration-200 font-medium"
          >
            {{ item.name }}
          </router-link>
        </div>

        <div class="hidden md:flex items-center relative">
          <div class="relative">
            <svg class="w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
            </svg>
            <input 
              v-model="searchQuery"
              @keyup.enter="handleSearch"
              type="text" 
              placeholder="搜索产品、服务..." 
              class="w-64 pl-10 pr-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary transition-all"
            >
          </div>
        </div>

        <button 
          @click="mobileMenuOpen = !mobileMenuOpen"
          class="md:hidden p-2 rounded-lg hover:bg-gray-100"
        >
          <svg class="w-6 h-6 text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path v-if="!mobileMenuOpen" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"/>
            <path v-else stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/>
          </svg>
        </button>
      </div>
    </div>

    <div v-if="mobileMenuOpen" class="md:hidden bg-white border-t">
      <div class="px-4 py-3">
        <div class="relative mb-4">
          <svg class="w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"/>
          </svg>
          <input 
            v-model="searchQuery"
            @keyup.enter="handleSearch"
            type="text" 
            placeholder="搜索产品、服务..." 
            class="w-full pl-10 pr-4 py-2 border border-gray-200 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary/50 focus:border-primary"
          >
        </div>
        <div class="space-y-1">
          <router-link 
            v-for="item in navItems" 
            :key="item.name"
            :to="item.path"
            @click="mobileMenuOpen = false"
            class="block px-4 py-2 text-gray-600 hover:bg-gray-50 rounded-lg"
          >
            {{ item.name }}
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const mobileMenuOpen = ref(false)
const searchQuery = ref('')

const navItems = [
  { name: '首页', path: '/' },
  { name: '产品中心', path: '/products' },
  { name: '芯片加工', path: '/services' },
  { name: '关于我们', path: '/about' },
  { name: '联系我们', path: '/contact' }
]

const handleSearch = () => {
  if (searchQuery.value.trim()) {
    router.push('/products')
  }
}
</script>
