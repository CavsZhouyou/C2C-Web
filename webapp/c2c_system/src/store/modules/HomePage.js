/*
 * @Author: zhouyou@werun 
 * @Descriptions: 首页全局状态管理 
 * @Date: 2018-07-10 09:21:44 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-12 09:40:35
 */


import * as types from '../mutation-type';
import CookieUtils from '../../js/cookieUtil';

const defaultImg = require("../../assets/head-img.jpg");

const HomePage = {
    state: {
        userId: CookieUtils.getCookie("c2c_user_id"),
        roleId: CookieUtils.getCookie("c2c_role_id"),
        headImg: CookieUtils.getCookie("c2c_head_img") || defaultImg,
        nickName: CookieUtils.getCookie("c2c_nick_name"),
    },
    mutations: {
        [types.UPDATE_USER_ID](state) {
            state.userId = CookieUtils.getCookie("c2c_user_id");
        },
        [types.UPDATE_ROLE_ID](state) {
            state.roleId = CookieUtils.getCookie("c2c_role_id");
        },
        [types.UPDATE_HEAD_IMG](state, img) {
            CookieUtils.setCookie("c2c_head_img", img);
            state.headImg = img;
        },
        [types.UPDATE_NICK_NAME](state, name) {
            CookieUtils.setCookie("c2c_nick_name", name);
            state.nickName = name;
        },

    },
    actions: {
        updateUserId({
            commit,
            state
        }) {
            commit(types.UPDATE_USER_ID);
        },
        updateRoleId({
            commit,
            state
        }) {
            commit(types.UPDATE_ROLE_ID);
        },
        updateHeadImg({
            commit,
            state
        }, img) {
            commit(types.UPDATE_HEAD_IMG, img);
        },
        updateNickName({
            commit,
            state
        }, name) {
            commit(types.UPDATE_NICK_NAME, name);
        },
    },
    getters: {
        userId: state => state.userId,
        roleId: state => state.roleId,
        headImg: state => state.headImg,
        nickName: state => state.nickName
    },
}


export default HomePage;