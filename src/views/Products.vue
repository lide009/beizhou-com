<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <!-- ===== Section 1: 页面标题区 ===== -->
    <div class="bg-gradient-to-r from-primary to-secondary text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-20">
        <h1 class="text-3xl md:text-4xl font-bold mb-3">SU-8 BZ系列国产环氧基负性光刻胶</h1>
        <div class="mt-6 flex flex-wrap gap-3">
          <span class="px-3 py-1 bg-white/20 rounded-full text-sm">膜厚覆盖 1.5-95 μm</span>
          <span class="px-3 py-1 bg-white/20 rounded-full text-sm">保质期 13 个月</span>
          <span class="px-3 py-1 bg-white/20 rounded-full text-sm">80°C 低温工艺</span>
        </div>
      </div>
    </div>

    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12 space-y-16">
      <!-- ===== Section 2: 产品概述与特性（双栏布局） ===== -->
      <section>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <!-- 左栏：产品概述 + 性能验证 -->
          <div class="space-y-6">
            <div class="bg-white rounded-xl shadow-md p-6 md:p-8">
              <h2 class="text-2xl font-bold text-gray-800 mb-4 flex items-center gap-2">
                <svg class="w-6 h-6 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                产品概述
              </h2>
              <div class="space-y-3 text-gray-600">
                <div class="flex items-start gap-3">
                  <span class="w-20 text-sm font-semibold text-gray-500 flex-shrink-0">产品类型</span>
                  <span>环氧基负性光刻胶</span>
                </div>
                <div class="flex items-start gap-3">
                  <span class="w-20 text-sm font-semibold text-gray-500 flex-shrink-0">膜厚范围</span>
                  <span>1.5-95 μm</span>
                </div>
                <div class="flex items-start gap-3">
                  <span class="w-20 text-sm font-semibold text-gray-500 flex-shrink-0">保质期</span>
                  <span>13 个月</span>
                </div>
                <div class="flex items-start gap-3">
                  <span class="w-20 text-sm font-semibold text-gray-500 flex-shrink-0">兼容性</span>
                  <span>与进口SU-8工艺高度兼容，可快速导入现有工艺线。支持多层套刻工艺，无需大规模工艺重构</span>
                </div>
              </div>
            </div>

            <div class="bg-gradient-to-r from-blue-50 to-blue-100 rounded-xl shadow-sm p-6 md:p-8 border border-blue-200">
              <h3 class="text-lg font-bold text-primary mb-3 flex items-center gap-2">
                <svg class="w-5 h-5 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                </svg>
                性能验证
              </h3>
              <p class="text-gray-700">
                产品性能经<strong>北京大学微加工与微流控平台</strong>测试验证并认可。使用说明书由相关专家团队指导编撰，内容全面、细节清晰、实操性强。
              </p>
            </div>
          </div>

          <!-- 右栏：6大优势 2x3网格 -->
          <div>
            <h2 class="text-2xl font-bold text-gray-800 mb-6 flex items-center gap-2">
              <svg class="w-6 h-6 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/>
              </svg>
              六大核心优势
            </h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div v-for="item in advantages" :key="item.icon" class="bg-white rounded-xl shadow-md p-5 hover:shadow-lg transition-shadow border-t-4 border-accent">
                <div class="flex items-center gap-2 mb-2">
                  <div class="w-8 h-8 bg-primary/10 rounded-lg flex items-center justify-center flex-shrink-0">
                    <svg class="w-5 h-5 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="item.icon"/>
                    </svg>
                  </div>
                  <h3 class="font-bold text-gray-800 text-sm md:text-base">{{ item.title }}</h3>
                </div>
                <p class="text-gray-600 text-sm">{{ item.desc }}</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ===== Section 3: 产品型号参数表 ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">产品型号与参数</h2>
        <div class="bg-white rounded-xl shadow-md overflow-hidden">
          <div class="overflow-x-auto">
            <table class="w-full text-sm md:text-base">
              <thead>
                <tr class="bg-gradient-to-r from-primary to-secondary text-white">
                  <th class="px-6 py-4 text-left font-semibold">型号</th>
                  <th class="px-6 py-4 text-left font-semibold">匀胶厚度范围</th>
                  <th class="px-6 py-4 text-left font-semibold">典型应用</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(p, i) in productModels" :key="p.model" class="border-b border-gray-100 hover:bg-blue-50/50 transition-colors" :class="i % 2 === 0 ? 'bg-white' : 'bg-gray-50/50'">
                  <td class="px-6 py-4 font-semibold text-primary">{{ p.model }}</td>
                  <td class="px-6 py-4 text-gray-700">{{ p.thickness }}</td>
                  <td class="px-6 py-4 text-gray-700">{{ p.application }}</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </section>

      <!-- ===== Section 4: 产品优势 ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">产品优势</h2>
        <div class="grid grid-cols-1 lg:grid-cols-3 gap-6">
          <!-- 价格对比卡片 -->
          <div class="bg-white rounded-xl shadow-md overflow-hidden flex flex-col">
            <div class="bg-gradient-to-r from-primary to-secondary px-6 py-4">
              <div class="flex items-center gap-2">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <h3 class="text-white font-semibold">价格优势</h3>
              </div>
            </div>
            <div class="p-6 flex flex-col flex-1">
              <div class="space-y-4 flex-1">
                <div v-for="item in priceComparison" :key="item.spec" class="flex items-center justify-between pb-4 border-b border-gray-100 last:border-0 last:pb-0">
                  <span class="text-gray-600 font-medium">{{ item.spec }}</span>
                  <span class="text-primary font-bold">{{ item.beizhou }}</span>
                </div>
              </div>
              <div class="mt-4 bg-green-50 rounded-lg p-3 text-center">
                <span class="text-green-600 font-bold">约进口品牌价格的1/4</span>
                <p class="text-green-500 text-xs mt-1">大幅降低研发试错成本</p>
              </div>
            </div>
          </div>

          <!-- 货期优势卡片 -->
          <div class="bg-white rounded-xl shadow-md overflow-hidden flex flex-col">
            <div class="bg-gradient-to-r from-green-500 to-green-600 px-6 py-4">
              <div class="flex items-center gap-2">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <h3 class="text-white font-semibold">货期优势</h3>
              </div>
            </div>
            <div class="p-6 flex flex-col flex-1">
              <div class="flex items-center justify-center gap-6 flex-1">
                <div class="text-center">
                  <div class="text-3xl font-bold text-gray-400">2个月+</div>
                  <p class="text-gray-500 text-sm mt-1">进口SU-8</p>
                </div>
                <div class="text-gray-300 text-2xl">→</div>
                <div class="text-center">
                  <div class="text-4xl font-extrabold text-green-600">2周</div>
                  <p class="text-gray-500 text-sm mt-1">北州SU-8</p>
                </div>
              </div>
              <div class="mt-4 bg-green-50 rounded-lg p-3 text-center">
                <span class="text-green-600 font-bold">快85%</span>
                <p class="text-green-500 text-xs mt-1">快速响应科研需求</p>
              </div>
            </div>
          </div>

          <!-- 供应链优势卡片 -->
          <div class="bg-white rounded-xl shadow-md overflow-hidden flex flex-col">
            <div class="bg-gradient-to-r from-accent to-blue-500 px-6 py-4">
              <div class="flex items-center gap-2">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                </svg>
                <h3 class="text-white font-semibold">供应链可控</h3>
              </div>
            </div>
            <div class="p-6 flex flex-col flex-1">
              <ul class="space-y-3 flex-1">
                <li class="flex items-start gap-2">
                  <span class="w-2 h-2 bg-accent rounded-full mt-2 flex-shrink-0"></span>
                  <span class="text-gray-600 text-sm">国产自主供应，不受国际形势影响</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="w-2 h-2 bg-accent rounded-full mt-2 flex-shrink-0"></span>
                  <span class="text-gray-600 text-sm">无进口限制，供应稳定可靠</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="w-2 h-2 bg-accent rounded-full mt-2 flex-shrink-0"></span>
                  <span class="text-gray-600 text-sm">快速响应定制需求，服务更贴心</span>
                </li>
              </ul>
              <div class="mt-4 bg-blue-50 rounded-lg p-3 text-center">
                <span class="text-blue-600 font-bold">稳定可靠</span>
                <p class="text-blue-500 text-xs mt-1">科研生产无后顾之忧</p>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ===== Section 5: 工艺流程（8步） ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-3 text-center">标准工艺流程</h2>
        <p class="text-gray-500 text-center mb-8 text-sm">SU-8 BZ系列操作流程简洁明了，与进口SU-8工艺高度兼容</p>
        <div class="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-4 gap-4">
          <div v-for="(step, i) in processSteps" :key="step.name" class="relative">
            <div class="bg-white rounded-xl shadow-md p-5 text-center h-full hover:shadow-lg transition-shadow border-t-4 border-accent">
              <div class="w-10 h-10 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-3 font-bold text-sm">
                {{ i + 1 }}
              </div>
              <h3 class="font-bold text-gray-800 mb-2 text-sm">{{ step.name }}</h3>
              <p class="text-gray-500 text-xs leading-relaxed">{{ step.desc }}</p>
            </div>
          </div>
        </div>
      </section>

      <!-- ===== Section 6: 安全须知 ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">安全须知</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-5">
          <!-- 个人防护 -->
          <div class="bg-white rounded-xl shadow-md p-6 border-l-4 border-blue-500">
            <div class="flex items-center gap-2 mb-3">
              <svg class="w-6 h-6 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
              </svg>
              <h3 class="font-bold text-gray-800">个人防护</h3>
            </div>
            <ul class="space-y-2 text-sm text-gray-600">
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-blue-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>手部</strong>：丁基橡胶手套</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-blue-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>眼部</strong>：化学护目镜或面罩</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-blue-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>身体</strong>：防静电工作服</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-blue-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>呼吸</strong>：必要时佩戴防有机蒸汽滤毒盒</span>
              </li>
            </ul>
          </div>

          <!-- 储存条件 -->
          <div class="bg-white rounded-xl shadow-md p-6 border-l-4 border-green-500">
            <div class="flex items-center gap-2 mb-3">
              <svg class="w-6 h-6 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4"/>
              </svg>
              <h3 class="font-bold text-gray-800">储存条件</h3>
            </div>
            <ul class="space-y-2 text-sm text-gray-600">
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-green-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span>阴凉、干燥、避光环境，直立<strong>密封存放</strong></span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-green-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>远离</strong>光线、酸类、热源和火源</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-green-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span>长期储存<strong>4-10°C</strong>，使用前恢复至<strong>20-25°C</strong></span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-green-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span>保质期<strong>13 个月</strong>（4°C 储存）</span>
              </li>
            </ul>
          </div>

          <!-- 急救措施 -->
          <div class="bg-white rounded-xl shadow-md p-6 border-l-4 border-yellow-500">
            <div class="flex items-center gap-2 mb-3">
              <svg class="w-6 h-6 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"/>
              </svg>
              <h3 class="font-bold text-gray-800">急救措施</h3>
            </div>
            <ul class="space-y-2 text-sm text-gray-600">
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-yellow-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>皮肤</strong>：肥皂水冲洗，脱去污染衣物</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-yellow-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>眼睛</strong>：清水冲洗至少15分钟，立即就医</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-yellow-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>吸入</strong>：移至空气新鲜处，保持呼吸通畅</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-yellow-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>食入</strong>：切勿催吐，立即漱口并就医</span>
              </li>
            </ul>
          </div>
        </div>
      </section>

      <!-- ===== Section 7: 淘宝店购买 ===== -->
      <section>
        <div class="bg-gradient-to-r from-orange-500 to-orange-600 rounded-2xl shadow-xl overflow-hidden">
          <div class="px-6 py-12 md:px-12 md:py-16">
            <div class="flex flex-col lg:flex-row items-center justify-center gap-8">
              <div class="text-white text-center lg:text-left">
                <div class="inline-block bg-white/20 text-white text-sm font-semibold px-4 py-1 rounded-full mb-4">
                  淘宝店购买
                </div>
                <h2 class="text-2xl md:text-3xl font-bold mb-4">淘宝店：北州芯片科技</h2>
                <p class="text-orange-100 text-lg mb-2">SU-8光刻胶、显影液、PDMS等耗材</p>
                <p class="text-orange-200 text-sm mb-6">手机淘宝扫一扫右侧二维码进店选购</p>
                <button @click="goContact" class="px-6 py-2 bg-white text-orange-600 font-bold rounded-lg hover:bg-orange-50 transition-colors shadow-lg">
                  联系客服咨询
                </button>
              </div>
              <div class="bg-white p-4 rounded-xl text-center">
                <img :src="taobaoQrUrl" alt="北州芯片科技淘宝店二维码" class="w-48 h-48 rounded-lg object-contain" />
                <p class="text-gray-500 text-sm mt-2">淘宝店：北州芯片科技</p>
              </div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script setup>
import { articles } from '../data/articles'
import { useRouter } from 'vue-router'

const router = useRouter()

const taobaoQrUrl = new URL('/淘宝店铺二维码-仅二维码.jpg', import.meta.url).href

// ===== 6大优势（来自 articles id=5 OCR数据） =====
const advantages = [
  {
    icon: 'M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z',
    title: '80°C低温工艺',
    desc: '仅需80°C完成关键烘烤步骤，显著降低热应力，有效减少脱模问题，对热敏材料基底更友好'
  },
  {
    icon: 'M3 4h2l3 10h10l3-10h1M10 21a2 2 0 100-4 2 2 0 000 4zm8 0a2 2 0 100-4 2 2 0 000 4z',
    title: '最小分辨率1μm',
    desc: '满足高精度MEMS结构与微流控器件的制造需求'
  },
  {
    icon: 'M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4',
    title: '局部深宽比接近 3:1',
    desc: '能够制造非常高的局部深宽比结构，满足厚膜应用需求'
  },
  {
    icon: 'M8 9l4-4 4 4m0 6l-4 4-4-4',
    title: '侧壁垂直度优异',
    desc: '垂直侧壁，70μm 高度内 >85°，确保微结构精度'
  },
  {
    icon: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z',
    title: '基底附着力优异',
    desc: '通过多轮配方改进，增强附着力，适用于多层套刻工艺'
  },
  {
    icon: 'M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z',
    title: '高光学透过率',
    desc: '360nm以上具有非常高的光学透射率，适合较厚薄膜光刻'
  }
]

// ===== 产品型号数据（来自 2026-8-28 版使用说明书 表1） =====
const productModels = [
  { model: 'SU-8 BZ 02', thickness: '1.5-6.2 μm', application: '薄膜结构' },
  { model: 'SU-8 BZ 05', thickness: '3.1-14 μm', application: '标准微结构' },
  { model: 'SU-8 BZ 15', thickness: '10-38 μm', application: '厚膜微结构' },
  { model: 'SU-8 BZ 25', thickness: '16-65 μm', application: '厚膜/高深宽比结构' },
  { model: 'SU-8 BZ 50', thickness: '24-95 μm', application: '超厚膜/高深宽比结构' }
]

// ===== 价格对比数据 =====
const priceComparison = [
  { spec: '500 mL', beizhou: '4000元' },
  { spec: '100 mL', beizhou: '1000元' }
]

// ===== 工艺流程步骤（来自 2026-8-28 版使用说明书） =====
const processSteps = [
  { name: '基片准备', desc: '基片清洁干燥，190°C加热5分钟以上去除水分子吸附' },
  { name: '旋涂', desc: '500rpm/10s预涂 + 3000rpm/30s高速旋涂匀胶' },
  { name: '前烘', desc: '水平热板80°C烘烤3-50分钟（依膜厚而定，BZ 50建议95°C）' },
  { name: '曝光', desc: 'i-line(365nm)紫外曝光，能量80-550 mJ/cm²（依膜厚而定）' },
  { name: '后烘', desc: '曝光后80°C烘烤4-11分钟，应可见掩模版潜像' },
  { name: '显影', desc: 'SU-8显影液浸没式/喷淋式显影0.2-12分钟' },
  { name: '冲洗干燥', desc: '新鲜显影液喷淋冲洗约10秒，氮气吹干' },
  { name: '坚膜', desc: '80°C热板坚膜20-30分钟（可选），提升交联度与附着力' }
]

function goContact() {
  router.push('/contact')
}

function goManual() {
  router.push('/article/7')
}
</script>