import Vue from 'vue'
import App from './App'

import cuCustom from './colorui/components/cu-custom.vue'
Vue.component('cu-custom',cuCustom)

import course from './pages/course/course.vue'
Vue.component('course',course)

import curriculum from './pages/course/curriculum.vue'
Vue.component('curriculum',curriculum)

import user from './pages/user/user.vue'
Vue.component('user',user)


Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
  ...App
})
app.$mount()
