<template>
  <div class="min-h-screen bg-gray-50 pt-20">
    <!-- ===== Section 1: 页面标题区 ===== -->
    <div class="bg-gradient-to-r from-primary to-secondary text-white">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-16 md:py-20">
        <h1 class="text-3xl md:text-4xl font-bold mb-3">产品中心</h1>
        <p class="text-lg md:text-xl text-blue-100">SU-8 BZ3000系列国产环氧基负性光刻胶</p>
        <div class="mt-6 flex flex-wrap gap-3">
          <span class="px-3 py-1 bg-white/20 rounded-full text-sm">膜厚覆盖 1.3 — 110 μm</span>
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
                  <span>1.3 — 110 μm</span>
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
                产品性能经<strong>北京大学微加工与微流控平台教授课题组</strong>测试验证并认可。使用说明书由相关专家团队指导编撰，内容全面、细节清晰、实操性强。
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

      <!-- ===== Section 4: 价格优势 ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">价格优势</h2>
        <div class="grid grid-cols-1 lg:grid-cols-5 gap-6">
          <!-- 价格对比表 -->
          <div class="lg:col-span-3 bg-white rounded-xl shadow-md overflow-hidden border border-gray-100">
            <div class="bg-gradient-to-r from-primary to-secondary px-6 py-4">
              <h3 class="text-white font-semibold text-lg">SU-8光刻胶综合对比</h3>
            </div>
            <div class="overflow-x-auto">
              <table class="w-full text-sm md:text-base">
                <thead>
                  <tr class="bg-gray-50">
                    <th class="px-6 py-3 text-left font-semibold text-gray-600 border-b-2 border-gray-200">项目</th>
                    <th class="px-6 py-3 text-center font-semibold text-primary border-b-2 border-primary">北州SU-8光刻胶</th>
                    <th class="px-6 py-3 text-center font-semibold text-gray-500 border-b-2 border-gray-200">进口SU-8光刻胶</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(row, i) in priceComparison" :key="row.spec" :class="i % 2 === 0 ? 'bg-white' : 'bg-gray-50/50'" class="hover:bg-blue-50 transition-colors">
                    <td class="px-6 py-4 font-medium text-gray-700">{{ row.spec }}</td>
                    <td class="px-6 py-4 text-center">
                      <span v-if="row.spec === '货期'" class="inline-block bg-green-100 text-green-600 font-bold px-3 py-1 rounded-full">{{ row.beizhou }}</span>
                      <span v-else class="inline-block bg-primary/10 text-primary font-bold px-3 py-1 rounded-full">{{ row.beizhou }}</span>
                    </td>
                    <td class="px-6 py-4 text-center text-gray-500">{{ row.importPrice }}</td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>

          <!-- 优势卡片 -->
          <div class="lg:col-span-2 space-y-4">
            <div class="bg-gradient-to-br from-primary to-secondary text-white rounded-xl shadow-lg p-6 text-center">
              <div class="text-5xl font-extrabold mb-2">75%</div>
              <p class="text-blue-100">价格比进口SU-8低</p>
              <p class="text-blue-200 text-sm mt-1">大幅降低研发试错成本</p>
            </div>
            <div class="bg-white rounded-xl shadow-md p-6 border-l-4 border-green-500">
              <div class="flex items-center gap-3 mb-3">
                <svg class="w-6 h-6 text-green-600 flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"/>
                </svg>
                <h3 class="font-bold text-gray-800">货期优势</h3>
              </div>
              <div class="flex items-center justify-between">
                <div class="text-center">
                  <span class="text-3xl font-extrabold text-green-600">2周</span>
                  <p class="text-xs text-gray-500 mt-1">北州SU-8</p>
                </div>
                <div class="text-gray-300 text-xl">→</div>
                <div class="text-center">
                  <span class="text-2xl font-bold text-gray-400">2个月+</span>
                  <p class="text-xs text-gray-500 mt-1">进口SU-8</p>
                </div>
              </div>
            </div>
            <div class="bg-white rounded-xl shadow-md p-6 border-l-4 border-blue-500">
              <div class="flex items-center gap-3 mb-3">
                <svg class="w-6 h-6 text-accent flex-shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"/>
                </svg>
                <h3 class="font-bold text-gray-800">供应链可控</h3>
              </div>
              <p class="text-gray-600 text-sm">国产自主供应，不受国际形势和进口限制影响，稳定可靠</p>
            </div>
          </div>
        </div>
      </section>

      <!-- ===== Section 5: 工艺流程（7步） ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-3 text-center">标准工艺流程</h2>
        <p class="text-gray-500 text-center mb-8 text-sm">SU-8 BZ3000系列操作流程简洁明了，与进口SU-8工艺高度兼容</p>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-7 gap-4">
          <div v-for="(step, i) in processSteps" :key="step.name" class="relative">
            <div class="bg-white rounded-xl shadow-md p-5 text-center h-full hover:shadow-lg transition-shadow border-t-4 border-accent">
              <div class="w-10 h-10 bg-primary text-white rounded-full flex items-center justify-center mx-auto mb-3 font-bold text-sm">
                {{ i + 1 }}
              </div>
              <h3 class="font-bold text-gray-800 mb-2 text-sm">{{ step.name }}</h3>
              <p class="text-gray-500 text-xs leading-relaxed">{{ step.desc }}</p>
            </div>
            <!-- 箭头连接符（除最后一个外） -->
            <div v-if="i < processSteps.length - 1" class="hidden lg:block absolute -right-3 top-1/2 -translate-y-1/2 z-10">
              <svg class="w-6 h-6 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/>
              </svg>
            </div>
          </div>
        </div>
      </section>

      <!-- ===== Section 6: 安全须知 ===== -->
      <section>
        <h2 class="text-2xl font-bold text-gray-800 mb-6 text-center">安全须知</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-5">
          <!-- 危险标识 -->
          <div class="bg-white rounded-xl shadow-md p-6 border-l-4 border-red-500">
            <div class="flex items-center gap-2 mb-3">
              <svg class="w-6 h-6 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L4.082 16.5c-.77.833.192 2.5 1.732 2.5z"/>
              </svg>
              <h3 class="font-bold text-gray-800">危险标识</h3>
            </div>
            <ul class="space-y-2 text-sm text-gray-600">
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-red-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>H227</strong>：可燃液体（丙类，闪点>60°C）</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-orange-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>H315</strong>：造成皮肤刺激</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-orange-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span><strong>H319</strong>：造成严重眼刺激</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-gray-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span class="text-gray-400 text-xs">不属于危险化学品（闪点75-90°C）</span>
              </li>
            </ul>
          </div>

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
                <span>阴凉、通风库房，<strong>4-25°C</strong></span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-green-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span>避光保存，<strong>远离热源和火源</strong></span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-green-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span>容器严格<strong>密封</strong>，与氧化剂分开存放</span>
              </li>
              <li class="flex items-start gap-2">
                <span class="w-2 h-2 bg-green-400 rounded-full mt-1.5 flex-shrink-0"></span>
                <span>长期储存推荐<strong>4°C</strong></span>
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
                <h2 class="text-2xl md:text-3xl font-bold mb-4">北州芯片科技淘宝店</h2>
                <p class="text-orange-100 text-lg mb-2">SU-8光刻胶、显影液、PDMS等耗材</p>
                <p class="text-orange-200 text-sm mb-6">点击下方二维码进入淘宝店选购</p>
                <button @click="goContact" class="px-6 py-2 bg-white text-orange-600 font-bold rounded-lg hover:bg-orange-50 transition-colors shadow-lg">
                  联系客服咨询
                </button>
              </div>
              <div class="bg-white p-4 rounded-xl">
                <div class="w-48 h-48 bg-gray-100 rounded-lg flex items-center justify-center">
                  <div class="text-center">
                    <svg class="w-20 h-20 mx-auto text-orange-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"/>
                    </svg>
                    <p class="text-gray-500 text-sm mt-2">淘宝店二维码</p>
                    <p class="text-gray-400 text-xs">后续补充</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- ===== Section 8: 试剂耗材（来自 article id=3） ===== -->
      <section>
        <div class="text-center mb-10">
          <h2 class="text-2xl font-bold text-gray-800 mb-3">试剂耗材</h2>
          <p class="text-gray-500">批发零售光刻胶、显影液、PDMS、铬板、硅片等微纳加工耗材，可分装销售</p>
        </div>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-5">
          <div v-for="item in consumables" :key="item.name" class="bg-white rounded-xl shadow-md p-6 hover:shadow-lg transition-shadow">
            <div class="w-10 h-10 bg-accent/10 rounded-lg flex items-center justify-center mb-4">
              <svg class="w-5 h-5 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19.428 15.428a2 2 0 00-1.022-.547l-2.387-.477a6 6 0 00-3.86.517l-.318.158a6 6 0 01-3.86.517L6.05 15.21a2 2 0 00-1.806.547M8 4h8l-1 1v5.172a2 2 0 00.586 1.414l5 5c1.26 1.26.367 3.414-1.415 3.414H4.828c-1.782 0-2.674-2.154-1.414-3.414l5-5A2 2 0 009 10.172V5L8 4z"/>
              </svg>
            </div>
            <h3 class="font-bold text-gray-800 mb-2">{{ item.name }}</h3>
            <p class="text-gray-500 text-sm mb-3 leading-relaxed">{{ item.desc }}</p>
            <div v-if="item.brand" class="text-xs text-gray-400">品牌：{{ item.brand }}</div>
          </div>
        </div>
      </section>

      <!-- ===== Section 9: 配套仪器（来自 article id=4） ===== -->
      <section>
        <div class="text-center mb-10">
          <h2 class="text-2xl font-bold text-gray-800 mb-3">配套仪器</h2>
          <p class="text-gray-500">经销多种微流实验配套仪器，满足科研与产业需求</p>
        </div>
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <!-- 程控泵/注射泵 -->
          <div class="bg-white rounded-xl shadow-md p-6">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-12 h-12 bg-primary/10 rounded-lg flex items-center justify-center">
                <svg class="w-6 h-6 text-primary" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/>
                </svg>
              </div>
              <div>
                <h3 class="font-bold text-gray-800">程控泵 / 注射泵</h3>
                <span class="text-xs text-accent">TS-1B / W0109-1B</span>
              </div>
            </div>
            <div class="space-y-3 text-sm text-gray-600">
              <p><strong>程控泵</strong> — 多功能程控仪，可用于物理、化学、生物、医学及工程等领域的教学和科研，将复杂的流体操作智能化。支持在线操作（计算机图形界面）和离线操作（面板旋钮及按键）。</p>
              <p><strong>注射泵 TS-1B/W0109-1B</strong> — 四通道推拉模式注射泵，可安装多种规格标准注射器。精确的行程控制，超宽线速度范围（7.9 μm/min — 79.4 mm/min），最大行程 90mm，行程分辨率 0.165 μm。</p>
            </div>
          </div>

          <!-- 芯片恒温培养装置 -->
          <div class="bg-white rounded-xl shadow-md p-6">
            <div class="flex items-center gap-3 mb-4">
              <div class="w-12 h-12 bg-accent/10 rounded-lg flex items-center justify-center">
                <svg class="w-6 h-6 text-accent" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 18.657A8 8 0 016.343 7.343S7 9 9 10c0-2 .5-5 2.986-7C14 5 16.09 5.777 17.656 7.343A7.975 7.975 0 0120 13a7.975 7.975 0 01-2.343 5.657z"/>
                </svg>
              </div>
              <div>
                <h3 class="font-bold text-gray-800">芯片用恒温培养装置</h3>
                <span class="text-xs text-accent">活细胞成像必备</span>
              </div>
            </div>
            <div class="space-y-2 text-sm text-gray-600">
              <p>在显微镜载物台上调控细胞培养所需的温度、湿度及 CO₂，实现从短期到长期（2周以上）的活细胞成像。</p>
              <ul class="space-y-1 mt-2">
                <li class="flex items-start gap-2">
                  <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                  <span>样品实时温度反馈功能，创造和 CO₂ 培养箱同等的温度环境</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                  <span>内置水槽设计，保持高湿度</span>
                </li>
                <li class="flex items-start gap-2">
                  <span class="w-1.5 h-1.5 bg-accent rounded-full mt-1.5 flex-shrink-0"></span>
                  <span>多种扩展应用产品配置，应对多种应用场景</span>
                </li>
              </ul>
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
    title: '深宽比 ≥ 3:1',
    desc: '能够制造非常高的深宽比结构，满足厚膜应用需求'
  },
  {
    icon: 'M8 9l4-4 4 4m0 6l-4 4-4-4',
    title: '侧壁垂直度优异',
    desc: '近乎垂直的侧壁图形，确保微结构精度'
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

// ===== 产品型号数据（来自 articles id=5 OCR数据） =====
const productModels = [
  { model: 'SU-8 BZ3002', thickness: '1.3 — 4 μm', application: '薄膜结构' },
  { model: 'SU-8 BZ3005', thickness: '3.8 — 12 μm', application: '标准微结构' },
  { model: 'SU-8 BZ3015', thickness: '12 — 36 μm', application: '厚膜微结构' },
  { model: 'SU-8 BZ3050', thickness: '38 — 110 μm', application: '超厚膜/高深宽比结构' }
]

// ===== 价格对比数据（来自 articles id=5 OCR数据） =====
const priceComparison = [
  { spec: '500 mL', beizhou: '0.4万元', importPrice: '1.2 — 1.4万元' },
  { spec: '100 mL', beizhou: '1千元', importPrice: '3 — 4千元' },
  { spec: '货期', beizhou: '2周', importPrice: '2个月以上' }
]

// ===== 工艺流程步骤（来自 articles id=7 OCR数据） =====
const processSteps = [
  { name: '基片准备', desc: '基片清洁干燥，建议190°C加热5分钟去除水分子吸附' },
  { name: '旋涂', desc: '500rpm/10s预涂 + 3000rpm/30s高速旋涂匀胶' },
  { name: '前烘', desc: '水平热板80°C烘烤3-50分钟（依膜厚而定）' },
  { name: '曝光', desc: 'i-line(365nm)紫外曝光，能量250-900 mJ/cm²' },
  { name: '后烘', desc: '曝光后80°C烘烤4-10分钟，应可见掩模版潜像' },
  { name: '显影', desc: 'SU-8显影液浸没式/喷淋式显影1-15分钟' },
  { name: '冲洗干燥', desc: '新鲜显影液喷淋冲洗约10秒，氮气吹干' }
]

// ===== 试剂耗材数据（来自 article id=3） =====
const consumables = [
  {
    name: 'SU-8 3050 光刻胶',
    desc: '基于环氧树脂的近紫外负性光刻胶，固化膜具有出色的热稳定和机械稳定性，耐溶剂和酸碱腐蚀，适合制造永久性结构',
    brand: 'MicroChem'
  },
  {
    name: 'SU-8 显影液',
    desc: 'SU-8专用显影液，主要成分为2-甲氧基-1-丙醇乙酸酯、乙酸-1-甲氧基-2-丙基酯',
    brand: 'MicroChem'
  },
  {
    name: 'PDMS 迈图 RTV615',
    desc: '双组分硅橡胶，透明、介电稳定性，固化前为中等粘度液体，固化后为有韧性弹性体',
    brand: '迈图 RTV615'
  },
  {
    name: '其他耗材',
    desc: '铬板、硅片、玻璃基底、导管等多种微纳加工耗材，支持分装销售'
  }
]

function goContact() {
  router.push('/contact')
}

function goManual() {
  router.push('/article/7')
}
</script>