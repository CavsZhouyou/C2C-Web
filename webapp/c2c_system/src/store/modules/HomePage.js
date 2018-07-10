/*
 * @Author: zhouyou@werun 
 * @Descriptions: 首页全局状态管理 
 * @Date: 2018-07-10 09:21:44 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-10 15:14:24
 */


import * as types from '../mutation-type';
import CookieUtils from '../../js/cookieUtil';

const HomePage = {
    state: {
        userId: CookieUtils.getCookie("c2c_user_id"),
    },
    mutations: {
        [types.UPDATE_USER_ID](state) {
            state.userId = CookieUtils.getCookie("c2c_user_id");
        }
    },
    actions: {
        updateUserId({
            commit,
            state
        }) {
            commit(types.UPDATE_USER_ID);
        }
    },
    getters: {
        userId: state => state.userId
    },
}


export default HomePage;