<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <div class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <h1 class="text-3xl font-bold text-gray-800">文章中心</h1>
        <p class="text-gray-600 mt-2">来自公众号"北州芯片科技"的文章</p>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="flex flex-col md:flex-row gap-8">
        <div class="flex-1">
          <div class="bg-white rounded-xl shadow-md p-4 mb-6">
            <div class="flex flex-col md:flex-row gap-4">
              <div class="flex-1">
                <input 
                  v-model="searchQuery"
                  type="text" 
                  placeholder="搜索文章..."
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
                />
              </div>
              <button 
                @click="searchQuery = ''"
                class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 transition-colors"
              >
                重置
              </button>
            </div>
          </div>

          <div class="space-y-4">
            <div 
              v-for="article in filteredArticles" 
              :key="article.id"
              class="bg-white rounded-xl shadow-md p-6 hover:shadow-lg transition-shadow cursor-pointer"
              @click="$router.push(`/article/${article.id}`)"
            >
              <div class="flex items-start justify-between">
                <div class="flex-1">
                  <span class="inline-block px-3 py-1 bg-primary/10 text-primary text-xs font-medium rounded-full mb-3">
                    {{ article.category }}
                  </span>
                  <h3 class="text-xl font-semibold text-gray-800 mb-2 hover:text-primary">
                    {{ article.title }}
                  </h3>
                  <p class="text-gray-600 line-clamp-2 mb-4">{{ article.summary }}</p>
                  <div class="flex items-center justify-between">
                    <div class="flex items-center space-x-4 text-sm text-gray-400">
                      <span>{{ article.author }}</span>
                      <span>{{ article.pubDate }}</span>
                    </div>
                    <span class="text-primary text-sm font-medium">阅读全文 →</span>
                  </div>
                </div>
              </div>
            </div>

            <div v-if="filteredArticles.length === 0" class="text-center py-12">
              <div class="text-gray-400 mb-4">
                <svg class="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
              </div>
              <p class="text-gray-500">没有找到相关文章</p>
            </div>
          </div>
        </div>

        <div class="w-full md:w-64">
          <div class="bg-white rounded-xl shadow-md p-4 sticky top-24">
            <h3 class="font-semibold text-gray-800 mb-4">文章分类</h3>
            <ul class="space-y-2">
              <li 
                v-for="cat in categories" 
                :key="cat.en"
                @click="selectedCategory = cat.en"
                :class="[
                  'px-4 py-2 rounded-lg cursor-pointer transition-colors',
                  selectedCategory === cat.en ? 'bg-primary text-white' : 'hover:bg-gray-50 text-gray-600'
                ]"
              >
                {{ cat.name }}
                <span class="float-right text-sm">
                  {{ getCategoryCount(cat.en) }}
                </span>
              </li>
            </ul>
          </div>

          <div class="bg-white rounded-xl shadow-md p-4 mt-4">
            <h3 class="font-semibold text-gray-800 mb-4">最新文章</h3>
            <ul class="space-y-3">
              <li 
                v-for="article in latestArticles" 
                :key="article.id"
                @click="$router.push(`/article/${article.id}`)"
                class="cursor-pointer"
              >
                <div class="text-sm text-gray-800 hover:text-primary transition-colors">
                  {{ article.title }}
                </div>
                <div class="text-xs text-gray-400">{{ article.pubDate }}</div>
              </li>
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { articles, categories } from '../data/articles'

const searchQuery = ref('')
const selectedCategory = ref('all')

const filteredArticles = computed(() => {
  let result = articles

  if (selectedCategory.value !== 'all') {
    result = result.filter(article => article.categoryEn === selectedCategory.value)
  }

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(article => 
      article.title.toLowerCase().includes(query) ||
      article.summary.toLowerCase().includes(query) ||
      article.category.toLowerCase().includes(query)
    )
  }

  return result.reverse()
})

const latestArticles = computed(() => {
  return articles.slice(-5).reverse()
})

const getCategoryCount = (categoryEn) => {
  if (categoryEn === 'all') return articles.length
  return articles.filter(article => article.categoryEn === categoryEn).length
}
</script>
