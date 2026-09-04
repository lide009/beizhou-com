<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <!-- ===== 页面标题区 ===== -->
    <div class="bg-gradient-to-r from-primary to-secondary text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 md:py-16 text-center">
        <h1 class="text-3xl md:text-4xl font-bold mb-3">微流控芯片定制询价工具</h1>
        <p class="text-blue-100 text-lg max-w-2xl mx-auto">
          五步填写芯片需求，自动生成参考报价、加工难度评估与验收标准
        </p>
      </div>
    </div>

    <!-- ===== 内嵌询价工具 ===== -->
    <div class="max-w-3xl mx-auto px-4 sm:px-6 lg:px-8 py-10">
      <div class="bg-white rounded-2xl shadow-lg overflow-hidden">
        <iframe
          ref="frameRef"
          :src="toolUrl"
          :style="{ height: frameHeight + 'px' }"
          class="w-full border-0 block"
          title="北州芯片科技微流控芯片定制询价工具"
        ></iframe>
      </div>
      <p class="text-center text-gray-400 text-sm mt-4">
        报价仅供参考，最终价格以双方协商确认为准 · 单次费用满600元包邮
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const frameRef = ref(null)
// 初始高度给一个合理值，工具加载后自动同步真实高度
const frameHeight = ref(700)

// dev 与生产环境的资源前缀不同，用 BASE_URL 保证两种模式都能加载
const toolUrl = import.meta.env.BASE_URL + 'inquiry.html'

function handleMessage(e) {
  if (!e.data) return
  if (e.data.type === 'inquiry-height' && e.data.height) {
    frameHeight.value = Math.max(600, e.data.height)
  } else if (e.data.type === 'inquiry-scroll-top') {
    frameRef.value?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
}

onMounted(() => window.addEventListener('message', handleMessage))
onBeforeUnmount(() => window.removeEventListener('message', handleMessage))
</script>
