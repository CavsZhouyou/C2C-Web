import Vue from 'vue'
import Router from 'vue-router'
import HomePage from './views/HomePage.vue'
import HouseListPage from './views/HouseListPage'
import HouseDetailPage from './views/HouseDetailPage'
import PersonalCenterPage from './views/PersonalCenterPage'
import UserManagePage from './views/UserManagePage'
import ReleaseDisclaimerPage from './views/ReleaseDisclaimerPage'

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
  }, {
    path: '/PersonalCenterPage',
    name: 'PersonalCenterPage',
    component: PersonalCenterPage,
    children: [{
      path: 'UserManagePage',
      name: 'UserManagePage',
      component: UserManagePage
    }, {
      path: 'ReleaseDisclaimerPage',
      name: "ReleaseDisclaimerPage",
      component: ReleaseDisclaimerPage
    }]
  }]
})