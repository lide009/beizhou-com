<template>
  <div class="min-h-screen bg-gray-50">
    <!-- ==================== 1. Hero 区域 ==================== -->
    <section class="relative bg-gradient-to-br from-primary via-secondary to-accent text-white py-20 pt-32 overflow-hidden">
      <!-- 背景装饰 -->
      <div class="absolute inset-0 opacity-10">
        <div class="absolute top-10 left-10 w-72 h-72 bg-white rounded-full blur-3xl"></div>
        <div class="absolute bottom-10 right-10 w-96 h-96 bg-white rounded-full blur-3xl"></div>
      </div>

      <div class="relative max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row items-center justify-between gap-12">
          <!-- 左侧文字 -->
          <div class="lg:w-1/2 text-center lg:text-left">
            <div class="inline-block px-4 py-1.5 bg-white/15 rounded-full text-blue-100 text-sm font-medium mb-6 backdrop-blur">
              国产高性能光刻胶 · 微流控芯片定制加工
            </div>
            <h1 class="text-4xl md:text-5xl lg:text-6xl font-bold mb-3 tracking-tight">
              {{ companyInfo.name }}
            </h1>
            <p class="text-lg md:text-xl text-blue-200 font-light tracking-wider mb-6">
              {{ companyInfo.nameEn }}
            </p>
            <p class="text-xl md:text-2xl text-white/90 font-medium mb-4 leading-relaxed">
              {{ companyInfo.description }}
            </p>
            <p class="text-base text-blue-100 mb-8 leading-relaxed max-w-lg mx-auto lg:mx-0">
              {{ companyInfo.experience }} · {{ companyInfo.facility }}
            </p>
            <div class="flex flex-wrap gap-4 justify-center lg:justify-start">
              <router-link
                to="/products"
                class="px-8 py-3.5 bg-white text-primary font-semibold rounded-lg hover:bg-gray-100 transition-all shadow-lg hover:shadow-xl transform hover:-translate-y-0.5"
              >
                了解产品
              </router-link>
              <router-link
                to="/contact"
                class="px-8 py-3.5 border-2 border-white/80 text-white font-semibold rounded-lg hover:bg-white hover:text-primary transition-all transform hover:-translate-y-0.5"
              >
                联系我们
              </router-link>
            </div>
          </div>

          <!-- 右侧产品卡片 -->
          <div class="lg:w-1/2 w-full max-w-md">
            <div class="bg-white/10 backdrop-blur-md rounded-2xl p-8 border border-white/20 shadow-2xl">
              <div class="text-center">
                <span class="inline-block px-3 py-1 bg-accent/40 rounded-full text-blue-100 text-xs font-medium mb-4">
                  核心产品
                </span>
                <div class="text-5xl md:text-6xl font-bold mb-3 tracking-tight">SU-8</div>
                <div class="text-xl md:text-2xl font-semibold mb-6">BZ3000 系列光刻胶</div>

                <!-- 核心卖点 -->
                <div class="space-y-3 text-left">
                  <div class="flex items-center gap-3 bg-white/10 rounded-lg px-4 py-3">
                    <span class="text-xl">🔥</span>
                    <div>
                      <p class="font-semibold text-sm">80°C 低温工艺</p>
                      <p class="text-blue-200 text-xs">显著降低热应力</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-3 bg-white/10 rounded-lg px-4 py-3">
                    <span class="text-xl">🎯</span>
                    <div>
                      <p class="font-semibold text-sm">1μm 分辨率</p>
                      <p class="text-blue-200 text-xs">满足高精度制造需求</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-3 bg-white/10 rounded-lg px-4 py-3">
                    <span class="text-xl">📐</span>
                    <div>
                      <p class="font-semibold text-sm">深宽比 ≥ 3:1</p>
                      <p class="text-blue-200 text-xs">媲美进口产品</p>
                    </div>
                  </div>
                  <div class="flex items-center gap-3 bg-white/10 rounded-lg px-4 py-3">
                    <span class="text-xl">💰</span>
                    <div>
                      <p class="font-semibold text-sm">价格仅为进口 1/4</p>
                      <p class="text-blue-200 text-xs">大幅降低研发试错成本</p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- 底部波浪过渡 -->
      <div class="absolute bottom-0 left-0 right-0">
        <svg viewBox="0 0 1440 80" fill="none" xmlns="http://www.w3.org/2000/svg">
          <path d="M0 80V40C240 0 480 0 720 20C960 40 1200 0 1440 20V80H0Z" fill="#F9FAFB"/>
        </svg>
      </div>
    </section>

    <!-- ==================== 2. 核心优势区域 ==================== -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-14">
          <span class="inline-block px-4 py-1.5 bg-primary/10 text-primary text-sm font-medium rounded-full mb-4">
            为什么选择我们
          </span>
          <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-4">
            SU-8 BZ3000 六大核心优势
          </h2>
          <p class="text-gray-500 max-w-2xl mx-auto">
            基于进口SU-8工艺经验自主研发，面向科研与产业的国产高性能厚胶解决方案
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
          <div
            v-for="(item, idx) in advantages"
            :key="idx"
            class="group bg-gray-50 hover:bg-primary hover:text-white rounded-xl p-6 transition-all duration-300 hover:shadow-xl hover:-translate-y-1 cursor-default"
          >
            <div class="w-12 h-12 bg-white rounded-xl flex items-center justify-center text-2xl mb-4 shadow-sm group-hover:scale-110 transition-transform">
              {{ item.icon }}
            </div>
            <h3 class="text-lg font-semibold mb-2">{{ item.title }}</h3>
            <p class="text-sm leading-relaxed"
               :class="idx % 2 === 0 ? 'text-gray-500 group-hover:text-blue-100' : 'text-gray-500 group-hover:text-blue-100'">
              {{ item.desc }}
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== 3. 业务范围区域 ==================== -->
    <section class="py-20 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-14">
          <span class="inline-block px-4 py-1.5 bg-accent/10 text-accent text-sm font-medium rounded-full mb-4">
            一站式服务
          </span>
          <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-4">
            我们的业务范围
          </h2>
          <p class="text-gray-500 max-w-2xl mx-auto">
            从光刻胶耗材到芯片定制加工，覆盖微流控科研全链条需求
          </p>
        </div>

        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-5 gap-5">
          <div
            v-for="(biz, idx) in businessAreas"
            :key="idx"
            class="group relative bg-white rounded-xl p-6 shadow-sm hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
          >
            <!-- 序号 -->
            <div class="w-10 h-10 bg-primary/10 text-primary rounded-lg flex items-center justify-center font-bold text-lg mb-4 group-hover:bg-primary group-hover:text-white transition-colors">
              {{ idx + 1 }}
            </div>
            <h3 class="text-lg font-semibold text-gray-800 mb-2">{{ biz.name }}</h3>
            <p class="text-sm text-gray-500 mb-4 leading-relaxed">{{ biz.desc }}</p>

            <!-- 链接 -->
            <router-link
              v-if="biz.link"
              :to="biz.link"
              class="inline-flex items-center gap-1.5 text-accent text-sm font-medium hover:text-primary transition-colors"
            >
              了解详情
              <svg class="w-4 h-4 group-hover:translate-x-1 transition-transform" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </router-link>
            <span
              v-else
              class="inline-flex items-center gap-1.5 text-gray-400 text-sm font-medium"
            >
              了解更多
            </span>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== 4. 合作机构区域 ==================== -->
    <section class="py-20 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-14">
          <span class="inline-block px-4 py-1.5 bg-primary/10 text-primary text-sm font-medium rounded-full mb-4">
            学术合作
          </span>
          <h2 class="text-3xl md:text-4xl font-bold text-gray-800 mb-4">
            合作机构
          </h2>
          <p class="text-gray-500 max-w-2xl mx-auto">
            与国内外顶尖科研机构深度合作，{{ companyInfo.papers }}
          </p>
        </div>

        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
          <div
            v-for="partner in partners"
            :key="partner.name"
            class="group bg-gray-50 rounded-xl p-8 text-center hover:shadow-lg transition-all duration-300 hover:-translate-y-1"
          >
            <div class="w-16 h-16 mx-auto mb-4 bg-white rounded-xl flex items-center justify-center shadow-md group-hover:scale-110 transition-transform overflow-hidden">
              <img :src="partner.logo" :alt="partner.name" class="w-12 h-12 object-contain">
            </div>
            <h4 class="text-gray-800 font-semibold text-sm md:text-base">{{ partner.name }}</h4>
          </div>
        </div>
      </div>
    </section>

    <!-- ==================== 5. 公众号区域 ==================== -->
    <section class="py-20 bg-gradient-to-br from-primary to-secondary text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col lg:flex-row items-center justify-between gap-12">
          <!-- 左侧信息 -->
          <div class="lg:w-1/2 text-center lg:text-left">
            <h2 class="text-3xl md:text-4xl font-bold mb-4">关注我们的公众号</h2>
            <p class="text-blue-100 text-lg mb-6 leading-relaxed max-w-md">
              获取最新产品信息、技术资讯和优惠活动
            </p>
            <div class="space-y-3">
              <div class="flex items-center gap-3 justify-center lg:justify-start text-blue-100">
                <svg class="w-5 h-5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                </svg>
                <span>产品发布与免费试用通知</span>
              </div>
              <div class="flex items-center gap-3 justify-center lg:justify-start text-blue-100">
                <svg class="w-5 h-5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                </svg>
                <span>光刻胶使用教程与技术指南</span>
              </div>
              <div class="flex items-center gap-3 justify-center lg:justify-start text-blue-100">
                <svg class="w-5 h-5 flex-shrink-0" fill="currentColor" viewBox="0 0 20 20">
                  <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"/>
                </svg>
                <span>微流控芯片工艺与行业资讯</span>
              </div>
            </div>
          </div>

          <!-- 右侧二维码 -->
          <div class="lg:w-1/2 flex justify-center lg:justify-end">
            <div class="bg-white p-5 rounded-2xl shadow-xl">
              <img src="/北州公众号二维码.jpg" alt="北州芯片科技公众号" class="w-48 h-48 rounded-xl object-contain">
            </div>
          </div>
        </div>

        <div class="text-center mt-8 pt-8 border-t border-white/10">
          <p class="text-blue-200">公众号名称：<span class="text-white font-semibold">{{ companyInfo.name }}</span></p>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { articles, companyInfo } from '../data/articles'

// ============ 核心优势（数据来自文章 id=5） ============
const advantages = [
  {
    icon: '🔥',
    title: '80°C 低温工艺',
    desc: '仅需80°C完成关键烘烤步骤，显著降低热应力，有效减少脱模问题，对热敏材料基底更友好'
  },
  {
    icon: '🎯',
    title: '分辨率 1μm',
    desc: '满足高精度MEMS结构与微流控器件的制造需求，实现精密图形转移'
  },
  {
    icon: '📐',
    title: '深宽比 ≥ 3:1',
    desc: '能够制造非常高的深宽比结构，性能媲美进口产品'
  },
  {
    icon: '📏',
    title: '侧壁垂直度优异',
    desc: '近乎垂直的侧壁图形，保证微结构精确性和工艺一致性'
  },
  {
    icon: '🔗',
    title: '基底附着力优异',
    desc: '通过多轮配方改进，增强与多种基底的结合力，提升工艺良率'
  },
  {
    icon: '💡',
    title: '高光学透过率',
    desc: '360nm以上具有非常高的光学透射率，适合较厚薄膜及光学应用场景'
  }
]

// ============ 业务范围（数据来自文章 id=10） ============
const businessAreas = [
  {
    name: '微加工服务',
    desc: '芯片设计、掩膜加工、光刻加工、PDMS工艺等一站式服务',
    link: '/services'
  },
  {
    name: '成品芯片',
    desc: '细胞培养分析、药物筛选、高通量富集等微流控芯片产品',
    link: '/services'
  },
  {
    name: '试剂耗材',
    desc: '光刻胶、显影液、硅片、铬板、PDMS、玻璃基底等耗材',
    link: '/products'
  },
  {
    name: '配套仪器',
    desc: '程控泵/注射泵、芯片恒温培养装置等实验配套设备',
    link: '/products'
  },
  {
    name: '体外诊断',
    desc: '肿瘤体外诊断、数字PCR分析微流芯片系统研发',
    link: null
  }
]

const partners = [
  { name: '北京大学', logo: new URL('/pku-logo.png', import.meta.url).href },
  { name: '浙江大学', logo: new URL('/zju-logo.png', import.meta.url).href },
  { name: '西安交通大学', logo: new URL('/xjtu-logo.png', import.meta.url).href },
  { name: '温州医科大学', logo: new URL('/wmu-logo.png', import.meta.url).href },
  { name: '中国科学院', logo: new URL('/cas-logo.png', import.meta.url).href },
  { name: '国科温州研究院', logo: new URL('/ucas-logo.png', import.meta.url).href },
  { name: '北京师范大学', logo: new URL('/bnu-logo.png', import.meta.url).href },
  { name: '首都医科大学', logo: new URL('/ccmu-logo.png', import.meta.url).href }
]
</script>