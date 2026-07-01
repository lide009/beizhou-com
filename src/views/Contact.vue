<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <div class="bg-white shadow-sm">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        <h1 class="text-3xl font-bold text-gray-800">联系我们</h1>
        <p class="text-gray-600 mt-2">欢迎与我们取得联系</p>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div class="bg-white rounded-xl shadow-md p-6">
          <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
            <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
            </svg>
          </div>
          <h3 class="font-semibold text-gray-800 mb-2">邮箱</h3>
          <p class="text-gray-600">beizhou_info@163.com</p>
          <p class="text-gray-400 text-sm mt-2">工作日 8:30 - 17:30</p>
        </div>

        <div class="bg-white rounded-xl shadow-md p-6">
          <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
            <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
            </svg>
          </div>
          <h3 class="font-semibold text-gray-800 mb-2">电话</h3>
          <p class="text-gray-600">0577-88017546</p>
          <p class="text-gray-600">18940884096</p>
          <p class="text-gray-400 text-sm mt-2">工作日 8:30 - 17:30</p>
        </div>

        <div class="bg-white rounded-xl shadow-md p-6">
          <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
            <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
            </svg>
          </div>
          <h3 class="font-semibold text-gray-800 mb-2">地址</h3>
          <p class="text-gray-600">浙江省温州市</p>
        </div>
      </div>

      <div class="mt-8 bg-white rounded-xl shadow-md p-8">
        <h2 class="text-2xl font-bold text-gray-800 mb-6">留言咨询</h2>
        <form @submit.prevent="handleSubmit" class="max-w-xl">
          <div class="mb-4">
            <label class="block text-gray-700 font-medium mb-2">姓名</label>
            <input 
              v-model="form.name"
              type="text" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
              placeholder="请输入您的姓名"
              required
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-medium mb-2">邮箱</label>
            <input 
              v-model="form.email"
              type="email" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
              placeholder="请输入您的邮箱"
              required
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-medium mb-2">电话</label>
            <input 
              v-model="form.phone"
              type="tel" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent"
              placeholder="请输入您的电话"
            />
          </div>
          <div class="mb-6">
            <label class="block text-gray-700 font-medium mb-2">留言内容</label>
            <textarea 
              v-model="form.message"
              rows="4" 
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary focus:border-transparent resize-none"
              placeholder="请输入您的留言内容"
              required
            ></textarea>
          </div>
          <button 
            type="submit"
            :disabled="isSubmitting"
            class="px-6 py-3 bg-primary text-white font-semibold rounded-lg hover:bg-secondary transition-colors disabled:opacity-50 disabled:cursor-not-allowed"
          >
            {{ isSubmitting ? '提交中...' : '提交留言' }}
          </button>
        </form>
        <div v-if="showSuccess" class="mt-4 p-4 bg-green-50 border border-green-200 rounded-lg text-green-700">
          感谢您的留言！我们已收到您的信息，会尽快与您联系。
        </div>
        <div v-if="showError" class="mt-4 p-4 bg-red-50 border border-red-200 rounded-lg text-red-700">
          {{ errorMsg }}
        </div>
      </div>

      <div class="mt-8 bg-primary rounded-xl p-8 text-white">
        <h2 class="text-2xl font-bold mb-4 text-center">关注公众号</h2>
        <div class="flex flex-col md:flex-row items-center justify-center gap-8">
          <div class="bg-white p-4 rounded-xl">
            <img :src="qrCodeUrl" alt="公众号二维码" class="w-48 h-48 rounded-lg object-cover" />
          </div>
          <div class="text-center md:text-left">
            <p class="text-blue-100 mb-4">公众号名称：北州芯片科技</p>
            <p class="text-blue-100">也欢迎您在公众号对话框私信留言，谢谢！</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { reactive, ref } from 'vue'

const qrCodeUrl = new URL('/北州公众号二维码.jpg', import.meta.url).href

const form = reactive({
  name: '',
  email: '',
  phone: '',
  message: ''
})

const showSuccess = ref(false)
const showError = ref(false)
const isSubmitting = ref(false)
const errorMsg = ref('')

// Web3Forms 密钥（请替换为你的真实密钥）
const ACCESS_KEY = '4fa8b824-f992-47d7-b842-371536fcb035'

const handleSubmit = async () => {
  isSubmitting.value = true
  showSuccess.value = false
  showError.value = false

  try {
    const response = await fetch('https://api.web3forms.com/submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        access_key: ACCESS_KEY,
        subject: `【北州芯片科技】咨询留言 - ${form.name}`,
        from_name: form.name,
        name: form.name,
        email: form.email,
        phone: form.phone,
        message: form.message
      })
    })

    const result = await response.json()

    if (result.success) {
      showSuccess.value = true
      form.name = ''
      form.email = ''
      form.phone = ''
      form.message = ''
    } else {
      showError.value = true
      errorMsg.value = result.message || '提交失败，请稍后再试'
    }
  } catch (err) {
    showError.value = true
    errorMsg.value = '网络错误，请检查网络后重试'
  } finally {
    isSubmitting.value = false
  }
}
</script>
