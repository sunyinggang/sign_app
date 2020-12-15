// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
// 移动端适配
import 'lib-flexible/flexible.js'
//人脸识别
import face from 'face-ca'
import { NavBar } from 'vant'
import { Loading } from 'vant';
import { Cell, CellGroup } from 'vant';
import { List } from 'vant';
import { Col, Row } from 'vant';
import { Popup } from 'vant';
import { Button } from 'vant';

import 'vant/lib/index.css';
console.log(face)
face.install(Vue,{
  msg:'Hellworld'
})
Vue.use(NavBar);
Vue.use(Loading);
Vue.use(Cell);
Vue.use(CellGroup);
Vue.use(List);
Vue.use(Col);
Vue.use(Row);
Vue.use(Popup);
Vue.use(Button);

Vue.config.productionTip = false
Vue.prototype.$ajax = axios
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
