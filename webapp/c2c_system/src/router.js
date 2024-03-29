import Vue from 'vue'
import Router from 'vue-router'
import HomePage from './views/HomePage.vue'
import HouseListPage from './views/HouseListPage'
import HouseDetailPage from './views/HouseDetailPage'
import PersonalCenterPage from './views/PersonalCenterPage'
import UserManagePage from './views/UserManagePage'
import ReleaseDisclaimerPage from './views/ReleaseDisclaimerPage'
import ReleaseTravelInformationPage from './views/ReleaseTravelInformationPage'
import ReleaseBuildingRecommendPage from './views/ReleaseBuildingRecommendPage'
import ViewReserveOrderPage from './views/ViewReserveOrderPage'
import ViewAllOrdersPage from './views/ViewAllOrdersPage'
import ViewBuildingOrdersPage from './views/VIewBuildingOrdersPage'
import ViewBuildingPage from './views/ViewBuildingPage'
import ReleaseBuildingPage from './views/ReleaseBuildingPage'
import ReleaseOrderPage from './views/ReleaseOrderPage'
import PersonalDataPage from './views/PersonalDataPage'
import ChangePasswordPage from './views/ChangePasswordPage'
import ModifyBuildingPage from './views/ModifyBuildingPage'

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
    path: '/HouseDetailPage/:buildingId',
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
      },
      {
        path: 'ReleaseTravelInformationPage',
        name: "ReleaseTravelInformationPage",
        component: ReleaseTravelInformationPage,
      },
      {
        path: 'ReleaseBuildingRecommendPage',
        name: "ReleaseBuildingRecommendPage",
        component: ReleaseBuildingRecommendPage,
      },
      {
        path: 'ViewReserveOrderPage',
        name: "ViewReserveOrderPage",
        component: ViewReserveOrderPage,
      },
      {
        path: 'ViewAllOrdersPage',
        name: "ViewAllOrdersPage",
        component: ViewAllOrdersPage,
      },
      {
        path: 'ViewBuildingOrdersPage',
        name: "ViewBuildingOrdersPage",
        component: ViewBuildingOrdersPage,
      },
      {
        path: 'ViewBuildingPage',
        name: "ViewBuildingPage",
        component: ViewBuildingPage,
      },
      {
        path: 'ModifyBuildingPage/:buildingId',
        name: "ModifyBuildingPage",
        component: ModifyBuildingPage,
      },
      {
        path: 'ReleaseBuildingPage',
        name: "ReleaseBuildingPage",
        component: ReleaseBuildingPage,
      },
      {
        path: 'ReleaseOrderPage/:buildingId',
        name: "ReleaseOrderPage",
        component: ReleaseOrderPage,
      },
      {
        path: 'PersonalDataPage',
        name: "PersonalDataPage",
        component: PersonalDataPage,
      },
      {
        path: 'ChangePasswordPage',
        name: "ChangePasswordPage",
        component: ChangePasswordPage,
      }
    ]
  }]
})