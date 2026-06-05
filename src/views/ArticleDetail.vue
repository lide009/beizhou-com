<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div v-if="article" class="bg-white rounded-xl shadow-md overflow-hidden">
        <div class="p-8">
          <span class="inline-block px-3 py-1 bg-primary/10 text-primary text-xs font-medium rounded-full mb-4">
            {{ article.category }}
          </span>
          <h1 class="text-3xl font-bold text-gray-800 mb-4">{{ article.title }}</h1>
          <div class="flex items-center space-x-4 text-gray-400 text-sm mb-8">
            <span>{{ article.author }}</span>
            <span>·</span>
            <span>{{ article.pubDate }}</span>
          </div>
          
          <div class="prose max-w-none">
            <div v-html="renderedContent"></div>
          </div>

          <!-- id=6 和 id=9 特殊提示：内容未从公众号提取 -->
          <div v-if="article.id === 6 || article.id === 9" class="mt-6 bg-amber-50 border border-amber-300 rounded-lg p-4 flex items-start space-x-3">
            <svg class="w-6 h-6 text-amber-500 flex-shrink-0 mt-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
            </svg>
            <p class="text-amber-800 text-sm leading-relaxed">
              本文内容尚未从公众号提取，请点击<strong>"查看原文"</strong>链接阅读完整文章。
            </p>
          </div>

          <div v-if="article.pages && article.pages.length > 0" class="mt-8 border-t pt-6">
            <h3 class="text-lg font-semibold text-gray-800 mb-2">原文完整内容（来自公众号PDF）</h3>
            <p class="text-gray-500 text-sm mb-4">以下为公众号文章的完整扫描件，供详细参考。</p>
            <div class="space-y-4">
              <img 
                v-for="(page, index) in article.pages" 
                :key="index"
                :src="`/articles/${page}`" 
                :alt="`${article.title} - 第${index + 1}页`"
                class="w-full rounded-lg shadow-md border border-gray-200"
                loading="lazy"
              />
            </div>
          </div>
        </div>

        <div class="px-8 py-4 bg-gray-50 border-t">
          <div class="flex items-center justify-between">
            <span class="text-gray-500 text-sm">文章来源：公众号"北州芯片科技"</span>
            <div class="flex items-center space-x-4">
              <a 
                v-if="article.link"
                :href="article.link" 
                target="_blank"
                class="text-primary text-sm font-medium hover:underline flex items-center"
              >
                <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 6H6a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2v-4M14 4h6m0 0v6m0-6L10 14"/>
                </svg>
                查看原文
              </a>
              <router-link to="/articles" class="text-primary text-sm font-medium hover:underline">
                返回文章列表 →
              </router-link>
            </div>
          </div>
        </div>
      </div>

      <div v-else class="text-center py-12">
        <div class="text-gray-400 mb-4">
          <svg class="w-16 h-16 mx-auto" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.172 16.172a4 4 0 015.656 0M9 10h.01M15 10h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
          </svg>
        </div>
        <p class="text-gray-500">文章不存在</p>
        <router-link to="/articles" class="inline-block mt-4 text-primary hover:underline">
          返回文章列表
        </router-link>
      </div>

      <div class="mt-8 bg-white rounded-xl shadow-md p-6">
        <h3 class="font-semibold text-gray-800 mb-4">相关文章</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
          <div 
            v-for="related in relatedArticles" 
            :key="related.id"
            class="flex items-center space-x-4 p-4 bg-gray-50 rounded-lg cursor-pointer hover:bg-gray-100 transition-colors"
            @click="$router.push(`/article/${related.id}`)"
          >
            <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
              <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/>
              </svg>
            </div>
            <div>
              <h4 class="text-gray-800 font-medium hover:text-primary">{{ related.title }}</h4>
              <p class="text-gray-400 text-sm">{{ related.pubDate }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import { articles } from '../data/articles'

const route = useRoute()
const article = ref(null)

const renderedContent = computed(() => {
  if (!article.value) return ''
  
  let content = article.value.content
    .replace(/^### (.*$)/gim, '<h3 class="text-xl font-semibold text-gray-800 mt-6 mb-3">$1</h3>')
    .replace(/^## (.*$)/gim, '<h2 class="text-2xl font-bold text-gray-800 mt-8 mb-4">$1</h2>')
    .replace(/\*\*(.*?)\*\*/g, '<strong class="font-semibold text-gray-800">$1</strong>')
    .replace(/【待补充[^】]*】/g, '<span class="inline-block px-3 py-1 bg-orange-50 border border-orange-200 text-orange-600 text-sm rounded italic">$&</span>')
    .replace(/\n/g, '<br>')
    .replace(/\|-+-\|/g, '</thead><tbody>')
    .replace(/\|([^|]+)\|([^|]+)\|([^|]+)\|([^|]+)\|/g, '<tr><td class="px-4 py-3">$1</td><td class="px-4 py-3">$2</td><td class="px-4 py-3">$3</td><td class="px-4 py-3">$4</td></tr>')
  
  if (content.includes('tbody>')) {
    content = '<table class="w-full text-sm border-collapse"><thead><tr class="bg-gray-50"><th class="px-4 py-3 text-left font-semibold text-gray-700">型号</th><th class="px-4 py-3 text-left font-semibold text-gray-700">粘度</th><th class="px-4 py-3 text-left font-semibold text-gray-700">膜厚范围</th><th class="px-4 py-3 text-left font-semibold text-gray-700">应用领域</th></tr>' + content + '</tbody></table>'
  }
  
  return content
})

const relatedArticles = computed(() => {
  if (!article.value) return []
  
  return articles
    .filter(a => a.category === article.value.category && a.id !== article.value.id)
    .slice(0, 4)
})

onMounted(() => {
  const id = parseInt(route.params.id)
  article.value = articles.find(a => a.id === id)
})
</script>
