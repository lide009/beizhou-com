<template>
  <footer class="bg-gray-900 text-white py-12">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="grid grid-cols-1 md:grid-cols-4 gap-8">
        <div class="col-span-1 md:col-span-2">
          <div class="flex items-center space-x-2 mb-4">
            <div class="w-10 h-10 bg-primary rounded-lg flex items-center justify-center">
              <span class="text-white font-bold text-lg">北</span>
            </div>
            <span class="text-xl font-bold">北州芯片科技</span>
          </div>
          <p class="text-gray-400 mb-4">
            北州芯片科技——专注于SU-8 BZ3000系列光刻胶的研发与销售。80℃低温工艺，高深宽比媲美进口，降本增效的国产替代新选择。
          </p>
          <div class="flex items-center space-x-4">
            <div class="w-12 h-12 bg-gray-800 rounded-lg flex items-center justify-center">
              <svg class="w-6 h-6 text-gray-400" fill="currentColor" viewBox="0 0 24 24">
                <path d="M8.691 2.188C3.891 2.188 0 5.476 0 9.53c0 2.212 1.17 4.203 3.002 5.55a.59.59 0 01.213.665l-.39 1.48c-.019.07-.048.141-.048.213 0 .163.13.295.29.295a.326.326 0 00.167-.054l1.903-1.114a.864.864 0 01.717-.098 10.16 10.16 0 002.837.403c4.801 0 8.692-3.287 8.692-7.342 0-4.054-3.891-7.339-8.692-7.339zm-3.11 4.216a.926.926 0 110-1.85.926.926 0 010 1.85zm2.24 0a.926.926 0 110-1.85.926.926 0 010 1.85zm1.658 3.317c-1.797 0-3.256 1.459-3.256 3.256 0 1.797 1.459 3.256 3.256 3.256 1.797 0 3.256-1.459 3.256-3.256 0-1.797-1.459-3.256-3.256-3.256zm-2.24 0a.926.926 0 110-1.85.926.926 0 010 1.85zm2.24 0a.926.926 0 110-1.85.926.926 0 010 1.85z"/>
              </svg>
            </div>
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
            <li><router-link to="/articles" class="text-gray-400 hover:text-white transition-colors">文章中心</router-link></li>
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
              <span class="text-gray-400">浙江省温州市</span>
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
