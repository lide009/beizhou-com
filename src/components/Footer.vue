<template>
  <footer class="bg-gray-900 text-white py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div class="col-span-1 md:col-span-2">
          <div class="flex items-center space-x-3 mb-4">
            <img :src="new URL('/北州logo.jpg', import.meta.url).href" alt="北州芯片科技" class="w-10 h-10 rounded-lg object-cover" />
            <span class="text-xl font-bold">北州芯片科技</span>
          </div>
          <p class="text-gray-400 mb-4">
            北州芯片科技——专注于SU-8 BZ3000系列光刻胶的研发与销售。80℃低温工艺，高深宽比媲美进口，降本增效的国产替代新选择。
          </p>
          <div class="flex items-center space-x-4">
            <img :src="new URL('/北州公众号二维码.jpg', import.meta.url).href" alt="公众号二维码" class="w-12 h-12 rounded-lg object-cover" />
            <div class="text-sm">
              <div class="text-gray-300 font-medium">公众号</div>
              <div class="text-gray-500">北州芯片科技</div>
            </div>
          </div>
        </div>

        <div>
          <h3 class="text-lg font-semibold mb-4">快速链接</h3>
          <ul class="space-y-2">
            <li><router-link to="/" class="text-gray-400 hover:text-white transition-colors">首页</router-link></li>
            <li><router-link to="/products" class="text-gray-400 hover:text-white transition-colors">产品中心</router-link></li>
            <li><router-link to="/services" class="text-gray-400 hover:text-white transition-colors">芯片加工</router-link></li>
            <li><router-link to="/about" class="text-gray-400 hover:text-white transition-colors">关于我们</router-link></li>
            <li><router-link to="/contact" class="text-gray-400 hover:text-white transition-colors">联系我们</router-link></li>
          </ul>
        </div>

        <div>
          <h3 class="text-lg font-semibold mb-4">联系方式</h3>
          <ul class="space-y-3">
            <li class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/>
              </svg>
              <span class="text-gray-400">beizhou_info@163.com</span>
            </li>
            <li class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 5a2 2 0 012-2h3.28a1 1 0 01.948.684l1.498 4.493a1 1 0 01-.502 1.21l-2.257 1.13a11.042 11.042 0 005.516 5.516l1.13-2.257a1 1 0 011.21-.502l4.493 1.498a1 1 0 01.684.949V19a2 2 0 01-2 2h-1C9.716 21 3 14.284 3 6V5z"/>
              </svg>
              <span class="text-gray-400">0577-88017546</span>
            </li>
            <li class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17.657 16.657L13.414 20.9a1.998 1.998 0 01-2.827 0l-4.244-4.243a8 8 0 1111.314 0z"/>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 11a3 3 0 11-6 0 3 3 0 016 0z"/>
              </svg>
              <span class="text-gray-400">浙江省温州市龙湾区浙南科技城</span>
            </li>
          </ul>
        </div>
      </div>

      <div class="border-t border-gray-800 mt-8 pt-8 text-center text-gray-500 text-sm">
        <p>© 2024 北州芯片科技 版权所有</p>
      </div>
    </div>
  </footer>
</template>
