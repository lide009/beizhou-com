<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <!-- ===== Section 1: 页面标题区 ===== -->
    <div class="bg-gradient-to-r from-primary to-secondary text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-20">
        <h1 class="text-3xl md:text-4xl font-bold mb-3">芯片加工服务</h1>
        <p class="text-lg md:text-xl text-blue-100">高精度微流控芯片定制加工 · 一站式解决方案</p>
        <div class="mt-6 flex flex-wrap gap-3">
          <span class="px-3 py-1 bg-white/20 rounded-full text-sm">芯片设计</span>
          <span class="px-3 py-1 bg-white/20 rounded-full text-sm">掩膜加工</span>
          <span class="px-3 py-1 bg-white/20 rounded-full text-sm">SU-8模具</span>
          <span class="px-3 py-1 bg-white/20 rounded-full text-sm">PDMS芯片</span>
          <span class="px-3 py-1 bg-white/20 rounded-full text-sm">质量检测</span>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-16">
      <!-- ===== Section 2: 微加工服务流程 ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-3 text-center">微加工服务流程</h2>
        <p class="text-gray-500 text-center mb-8 text-sm">从设计到交付，一站式完整服务</p>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-4">
          <div v-for="(step, i) in serviceSteps" :key="step.name" class="relative">
            <div class="bg-white rounded-xl shadow-md p-5 text-center h-full hover:shadow-lg transition-shadow border-t-4 border-accent">
              <div class="w-10 h-10 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-3 font-bold text-sm">
                {{ i + 1 }}
              </div>
              <h3 class="font-bold text-gray-800 mb-2 text-sm">{{ step.name }}</h3>
              <p class="text-gray-500 text-xs leading-relaxed">{{ step.desc }}</p>
            </div>
            <div v-if="i < serviceSteps.length - 1" class="hidden lg:block absolute -right-3 top-1/2 -translate-y-1/2 z-10">
              <svg class="w-6 h-6 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </div>
          </div>
        </div>
      </section>

      <!-- ===== Section 3: 服务与价格 ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">服务项目与价格</h2>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <!-- 高精度菲林掩膜 -->
          <div class="bg-white rounded-xl shadow-md p-6">
            <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 17V7m0 10a2 2 0 01-2 2H5a2 2 0 01-2-2V7a2 2 0 012-2h2a2 2 0 012 2m0 10a2 2 0 002 2h2a2 2 0 002-2M9 7a2 2 0 012-2h2a2 2 0 012 2m0 10V7m0 10a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2h-2a2 2 0 00-2 2"/>
              </svg>
            </div>
            <h3 class="font-bold text-gray-800 mb-2">高精度菲林掩膜</h3>
            <div class="text-2xl font-bold text-primary mb-2">低至 150 元/版</div>
            <ul class="space-y-1.5 text-sm text-gray-600">
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                <span>最小线宽：<strong>20 μm</strong></span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                <span>精度：约 <strong>5 μm</strong></span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                <span>适用于常规结构验证与基础实验</span>
              </li>
            </ul>
          </div>

          <!-- 高精度铬板掩膜 -->
          <div class="bg-white rounded-xl shadow-md p-6 border-2 border-accent">
            <div class="w-12 h-12 bg-accent/10 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
              </svg>
            </div>
            <h3 class="font-bold text-gray-800 mb-2">高精度铬板掩膜</h3>
            <div class="text-2xl font-bold text-accent mb-2">高精度首选</div>
            <ul class="space-y-1.5 text-sm text-gray-600">
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                <span>最小线宽：<strong>1.5 μm</strong></span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                <span>精度：<strong>0.5 μm</strong></span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                <span>适用于高分辨率通道、阵列器件</span>
              </li>
            </ul>
          </div>

          <!-- SU-8模具 + PDMS芯片 -->
          <div class="bg-white rounded-xl shadow-md p-6">
            <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4"/>
              </svg>
            </div>
            <h3 class="font-bold text-gray-800 mb-2">SU-8模具 + PDMS芯片</h3>
            <div class="text-2xl font-bold text-primary mb-2">模具低至 1500 元/版</div>
            <div class="text-lg font-semibold text-gray-700 mb-2">PDMS芯片低至 50 元/块</div>
            <ul class="space-y-1.5 text-sm text-gray-600">
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                <span>SU-8模具制作 + PDMS浇铸、切割、打孔</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                <span>对位键合 + 质检报告</span>
              </li>
            </ul>
          </div>
        </div>
      </section>

      <!-- ===== Section 4: 交付成果 ===== -->
      <section>
        <div class="bg-gradient-to-r from-blue-50 to-blue-100 rounded-xl p-8 border border-blue-200">
          <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">项目交付成果</h2>
          <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-6 gap-4">
            <div v-for="item in deliverables" :key="item" class="bg-white rounded-lg p-4 text-center shadow-sm">
              <div class="w-10 h-10 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-2">
                <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/>
                </svg>
              </div>
              <span class="text-sm font-medium text-gray-700">{{ item }}</span>
            </div>
          </div>
        </div>
      </section>

      <!-- ===== Section 5: 成品芯片产品 ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-3 text-center">成品芯片产品系列</h2>
        <p class="text-gray-500 text-center mb-8 text-sm">多款成熟微流控芯片产品，覆盖细胞培养、药物筛选、高通量富集等应用场景</p>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div v-for="chip in finishedChips" :key="chip.model" class="bg-white rounded-xl shadow-md p-6 hover:shadow-lg transition-shadow">
            <div class="flex items-center gap-2 mb-3">
              <div class="w-10 h-10 bg-primary text-white rounded-lg flex items-center justify-center font-bold text-sm">{{ chip.model.split('-')[1] }}</div>
              <div>
                <h3 class="font-bold text-gray-800 text-sm">{{ chip.model }}</h3>
                <span class="text-xs text-accent">{{ chip.type }}</span>
              </div>
            </div>
            <p class="text-gray-600 text-sm mb-3 leading-relaxed">{{ chip.desc }}</p>
            <div v-if="chip.reference" class="bg-gray-50 rounded-lg p-3 text-xs text-gray-500">
              <span class="text-gray-400">参考：</span>{{ chip.reference }}
            </div>
          </div>
        </div>
      </section>

      <!-- ===== Section 6: CTA ===== -->
      <section>
        <div class="bg-gradient-to-r from-primary to-secondary rounded-2xl shadow-xl overflow-hidden">
          <div class="px-6 py-12 md:px-12 md:py-16 text-center text-white">
            <h2 class="text-2xl md:text-3xl font-bold mb-4">需要定制微流控芯片？</h2>
            <p class="text-blue-100 text-lg mb-8">从设计到量产，我们提供一站式芯片加工服务</p>
            <router-link
              to="/contact"
              class="inline-block px-8 py-3 bg-white text-primary font-bold rounded-lg hover:bg-blue-50 transition-colors shadow-lg text-lg"
            >
              联系我们
            </router-link>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
// 微加工服务流程（来自 article id=1）
const serviceSteps = [
  { name: '芯片结构设计', desc: '芯片结构设计与图纸绘制' },
  { name: '掩膜加工', desc: '光刻掩膜加工（菲林/铬板）' },
  { name: 'SU-8模具', desc: 'SU-8模具制作与质检' },
  { name: 'PDMS加工', desc: '浇铸、切割、打孔、对位、键合' },
  { name: '质量检测', desc: '质量检测与性能验证' },
  { name: '批量生产', desc: '后续批量生产服务' }
]

// 交付成果（来自 article id=1）
const deliverables = ['设计图纸', '光刻掩膜', '硅片模具', 'PDMS芯片', '质检报告', '量产支持']

// 成品芯片产品（来自 article id=2）
const finishedChips = [
  {
    model: 'BZh-Chip001',
    type: '细胞培养与药物筛选',
    desc: '可实现多种哺乳动物细胞培养，进行药物筛选。适用于高通量细胞迁移实验和组合化学环境下的药物评价。',
    reference: 'High-throughput cell migration assay under combinatorial chemical environments by a novel 24-well-plate based device. Biomedical Microdevices, 2020, 22, 40'
  },
  {
    model: 'BZh-Chip002',
    type: '高通量富集培养筛选',
    desc: '动物细胞的高通量富集、培养及筛选。基于单层微流控器件实现自加载和细胞培养功能。',
    reference: 'Self-loading and cell culture in one layer microfluidic devices. Biomedical Microdevices, 2009, 11, 679-684'
  },
  {
    model: 'BZh-Chip003',
    type: '哺乳动物细胞培养',
    desc: '哺乳动物细胞的培养与分析，适用于细胞生物学基础研究和药物测试。'
  }
]
</script>