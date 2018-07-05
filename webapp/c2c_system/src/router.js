import Vue from 'vue'
import Router from 'vue-router'
import HomePage from './views/HomePage.vue'
import HouseListPage from './views/HouseListPage'

Vue.use(Router)

export default new Router({
  routes: [{
    path: '/',
    name: 'HomePage',
    component: HomePage
  }, {
    path: '/HouseList',
    name: "HouseList",
    component: HouseListPage
  }]
})