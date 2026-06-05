<template>
  <nav class="bg-white shadow-md fixed top-0 left-0 right-0 z-50">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex items-center justify-between h-16">
        <div class="flex items-center">
          <router-link to="/" class="flex items-center space-x-2">
            <div class="w-10 h-10 bg-primary rounded-lg flex items-center justify-center">
              <span class="text-white font-bold text-lg">北</span>
            </div>
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
          <button 
            @click="showWechatMenu = !showWechatMenu"
            class="flex items-center space-x-2 px-4 py-2 bg-primary text-white rounded-lg hover:bg-secondary transition-colors"
          >
            <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
              <path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 01.213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 00.167-.054l1.903-1.114a.864.864 0 01.717-.098 10.16 10.16 0 002.837.403c4.801 0 8.692-3.287 8.692-7.342 0-4.054-3.891-7.339-8.692-7.339zm-3.11 4.216a.926.926 0 110-1.85.926.926 0 010 1.85zm2.24 0a.926.926 0 110-1.85.926.926 0 010 1.85zm1.658 3.317c-1.797 0-3.256 1.459-3.256 3.256 0 1.797 1.459 3.256 3.256 3.256 1.797 0 3.256-1.459 3.256-3.256 0-1.797-1.459-3.256-3.256-3.256zm-2.24 0a.926.926 0 110-1.85.926.926 0 010 1.85zm2.24 0a.926.926 0 110-1.85.926.926 0 010 1.85z"/>
            </svg>
            <span>公众号菜单</span>
          </button>
          
          <div 
            v-if="showWechatMenu"
            class="absolute top-full right-0 mt-2 w-64 bg-white rounded-lg shadow-xl border border-gray-100 py-2 z-50"
          >
            <div v-for="menu in wechatMenu" :key="menu.name" class="border-b border-gray-100 last:border-b-0">
              <div class="px-4 py-2 bg-gray-50 font-semibold text-gray-700">{{ menu.name }}</div>
              <div 
                v-for="child in menu.children" 
                :key="child.name"
                @click="handleWechatMenuClick(child)"
                class="px-4 py-2 hover:bg-blue-50 cursor-pointer text-gray-600 hover:text-primary transition-colors"
              >
                {{ child.name }}
              </div>
            </div>
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
      <div class="px-4 py-2 space-y-2">
        <router-link 
          v-for="item in navItems" 
          :key="item.name"
          :to="item.path"
          @click="mobileMenuOpen = false"
          class="block px-4 py-2 text-gray-600 hover:bg-gray-50 rounded-lg"
        >
          {{ item.name }}
        </router-link>
        <div class="border-t pt-2 mt-2">
          <div class="text-sm font-semibold text-gray-500 px-4 mb-2">公众号菜单</div>
          <div v-for="menu in wechatMenu" :key="menu.name">
            <div class="px-4 py-2 bg-gray-50 text-sm font-semibold">{{ menu.name }}</div>
            <div 
              v-for="child in menu.children" 
              :key="child.name"
              @click="handleWechatMenuClick(child)"
              class="px-6 py-2 hover:bg-blue-50 cursor-pointer text-gray-600 text-sm"
            >
              {{ child.name }}
            </div>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { wechatMenu } from '../data/menu'

const router = useRouter()
const showWechatMenu = ref(false)
const mobileMenuOpen = ref(false)

const navItems = [
  { name: '首页', path: '/' },
  { name: '产品中心', path: '/products' },
  { name: '芯片加工', path: '/services' },
  { name: '关于我们', path: '/about' },
  { name: '联系我们', path: '/contact' },
  { name: '文章中心', path: '/articles' }
]

const handleWechatMenuClick = (item) => {
  showWechatMenu.value = false
  mobileMenuOpen.value = false
  
  if (item.link) {
    router.push(item.link)
  } else if (item.articleId) {
    router.push(`/article/${item.articleId}`)
  }
}
</script>
