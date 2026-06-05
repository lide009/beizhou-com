<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Section 1: 页面标题区 -->
    <section class="bg-gradient-to-r from-primary to-secondary text-white py-20 pt-32">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
        <h1 class="text-4xl md:text-5xl font-bold mb-4">关于我们</h1>
        <p class="text-xl text-blue-200">{{ companyInfo.name }} · {{ companyInfo.nameEn }}</p>
      </div>
    </section>

    <!-- Section 2: 公司概况（双栏布局） -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-12">
          <!-- 左栏：文字描述 -->
          <div>
            <h2 class="text-2xl font-bold text-gray-800 mb-6">公司概况</h2>
            <div class="space-y-4 text-gray-600 leading-relaxed">
              <p>{{ companyInfo.description }}</p>
              <p>{{ companyInfo.experience }}</p>
              <p>{{ companyInfo.facility }}</p>
              <p>{{ companyInfo.papers }}</p>
            </div>
          </div>

          <!-- 右栏：数据卡片 -->
          <div class="grid grid-cols-2 gap-4">
            <div class="bg-gradient-to-br from-primary to-secondary rounded-xl p-6 text-white text-center">
              <div class="text-4xl font-bold mb-2">20年</div>
              <div class="text-blue-200 text-sm">微加工经验</div>
            </div>
            <div class="bg-gradient-to-br from-primary to-secondary rounded-xl p-6 text-white text-center">
              <div class="text-4xl font-bold mb-2">千级</div>
              <div class="text-blue-200 text-sm">百平米超净间</div>
            </div>
            <div class="bg-gradient-to-br from-primary to-secondary rounded-xl p-6 text-white text-center">
              <div class="text-4xl font-bold mb-2">4家</div>
              <div class="text-blue-200 text-sm">合作机构</div>
            </div>
            <div class="bg-gradient-to-br from-primary to-secondary rounded-xl p-6 text-white text-center">
              <div class="text-4xl font-bold mb-2">近百篇</div>
              <div class="text-blue-200 text-sm">论文支持</div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 3: 核心业务（5个卡片） -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-800 mb-4">核心业务</h2>
          <p class="text-gray-600">五大业务板块，全方位服务微流控科研与产业需求</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-5 gap-6">
          <!-- 业务1：微加工服务 → /article/1 -->
          <router-link
            v-for="(biz, index) in businesses"
            :key="index"
            :to="biz.link"
            :class="[
              'bg-white rounded-xl shadow-md p-6 transition-all duration-300',
              biz.link ? 'hover:shadow-lg hover:-translate-y-1 cursor-pointer' : ''
            ]"
          >
            <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center mb-4">
              <span class="text-primary font-bold text-lg">{{ index + 1 }}</span>
            </div>
            <h3 class="font-semibold text-gray-800 mb-2">{{ biz.title }}</h3>
            <p class="text-gray-600 text-sm">{{ biz.desc }}</p>
          </router-link>
        </div>
      </div>
    </section>

    <!-- Section 4: 合作机构 -->
    <section class="py-16 bg-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-800 mb-4">合作机构</h2>
          <p class="text-gray-600">与国内外顶尖科研机构建立紧密合作关系</p>
        </div>
        <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
          <div
            v-for="partner in companyInfo.partners"
            :key="partner"
            class="bg-gray-50 rounded-xl p-8 text-center hover:shadow-md transition-shadow"
          >
            <div class="w-16 h-16 bg-primary/10 rounded-full flex items-center justify-center mx-auto mb-4">
              <svg class="w-8 h-8 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4" />
              </svg>
            </div>
            <h3 class="font-semibold text-gray-800">{{ partner }}</h3>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 5: 资质与认可 -->
    <section class="py-16 bg-gray-50">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold text-gray-800 mb-4">资质与认可</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
          <div class="bg-white rounded-xl shadow-md p-8 text-center">
            <div class="w-14 h-14 bg-primary/10 rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
              </svg>
            </div>
            <p class="text-gray-600 leading-relaxed">
              产品经<strong>北京大学微加工与微流控平台教授课题组</strong>测试验证并认可
            </p>
          </div>
          <div class="bg-white rounded-xl shadow-md p-8 text-center">
            <div class="w-14 h-14 bg-primary/10 rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253" />
              </svg>
            </div>
            <p class="text-gray-600 leading-relaxed">
              使用说明书由<strong>相关专家团队指导编撰</strong>，内容全面、细节清晰、实操性强
            </p>
          </div>
          <div class="bg-white rounded-xl shadow-md p-8 text-center">
            <div class="w-14 h-14 bg-primary/10 rounded-lg flex items-center justify-center mx-auto mb-4">
              <svg class="w-7 h-7 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
              </svg>
            </div>
            <p class="text-gray-600 leading-relaxed">
              团队过往支持<strong>近百篇高质量论文发表</strong>，获客户广泛认可和高度评价
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- Section 6: 联系方式 -->
    <section class="py-16 bg-gradient-to-r from-primary to-secondary text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="text-center mb-12">
          <h2 class="text-3xl font-bold mb-4">联系我们</h2>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8 max-w-4xl mx-auto">
          <div class="text-center">
            <div class="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center mx-auto mb-3">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
              </svg>
            </div>
            <div class="text-blue-200 text-sm mb-1">邮箱</div>
            <div class="font-medium">{{ contactInfo.email }}</div>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center mx-auto mb-3">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z" />
              </svg>
            </div>
            <div class="text-blue-200 text-sm mb-1">座机</div>
            <div class="font-medium">{{ contactInfo.phone }}</div>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center mx-auto mb-3">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 18h.01M8 21h8a2 2 0 002-2V5a2 2 0 00-2-2H8a2 2 0 00-2 2v14a2 2 0 002 2z" />
              </svg>
            </div>
            <div class="text-blue-200 text-sm mb-1">手机</div>
            <div class="font-medium">{{ contactInfo.mobile }}</div>
          </div>
          <div class="text-center">
            <div class="w-12 h-12 bg-white/10 rounded-full flex items-center justify-center mx-auto mb-3">
              <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z" />
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z" />
              </svg>
            </div>
            <div class="text-blue-200 text-sm mb-1">地址</div>
            <div class="font-medium">{{ contactInfo.address }}</div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { articles, companyInfo } from '../data/articles'

// 五大核心业务（数据来自文章id=10的业务范围）
const businesses = [
  {
    title: '微加工服务',
    desc: '芯片设计、掩膜加工、光刻加工、PDMS工艺',
    link: '/services'
  },
  {
    title: '成品芯片',
    desc: '细胞/细菌培养分析芯片，趋化/耐药性分析芯片',
    link: '/services'
  },
  {
    title: '试剂耗材',
    desc: '光刻胶、显影液、硅片、铬板、PDMS、玻璃基底',
    link: '/products'
  },
  {
    title: '配套仪器',
    desc: '程控泵/注射泵、恒温培养装置',
    link: '/products'
  },
  {
    title: '体外诊断',
    desc: '肿瘤体外诊断、数字PCR分析微流芯片系统研发',
    link: ''
  }
]

// 联系方式
const contactInfo = {
  email: 'beizhou_info@163.com',
  phone: '0577-88017546',
  mobile: '18940884096',
  address: '浙江省温州市'
}
</script>