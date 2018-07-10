import Vue from 'vue'
import Vuex from 'vuex'
import HomePage from './store/modules/HomePage'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    HomePage
  }
})