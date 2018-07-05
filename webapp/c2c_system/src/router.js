import Vue from 'vue'
import Router from 'vue-router'
import HomePage from './views/HomePage.vue'
import HouseListPage from './views/HouseListPage'
import HouseDetailPage from './views/HouseDetailPage'

Vue.use(Router)

export default new Router({
  routes: [{
    path: '/',
    name: 'HomePage',
    component: HomePage
  }, {
    path: '/HouseListPage',
    name: "HouseListPage",
    component: HouseListPage
  }, {
    path: '/HouseDetailPage',
    name: "HouseDetailPage",
    component: HouseDetailPage
  }]
})