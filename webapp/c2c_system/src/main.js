import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from './js/axios';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import 'vue2-animate/dist/vue2-animate.min.css';

Vue.config.productionTip = false

Vue.use(ElementUI);

// import utils
Vue.prototype.$axios = axios;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')