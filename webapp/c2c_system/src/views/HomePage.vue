/*
 * @Author: zhouyou@werun 
 * @Descriptions: 主页
 * @Date: 2018-07-05 20:33:56 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-10 20:54:26
 */

<template>
  <div id="home-page">
    <div class="header">
      <div class="container clearfix">
        <!-- <div class="left-bar">
          <span class="city">
            <a href="">重庆&nbsp;&nbsp;&nbsp; [点击切换]</a>
          </span>
        </div> -->
        <div class="left-bar">
          <span>
            <a href="">首页</a>
          </span>
          <span>
            <a href="">社区</a>
          </span>
          <span>
            <a href="">帮助</a>
          </span>
        </div>
        <div class="right-bar">
          <span v-if="userId">
            <router-link to="/PersonalCenterPage">个人中心</router-link>
          </span>
          <span v-if="userId">
            <a href="" @click.prevent="logout()">退出</a>
          </span>
          <span v-if="!userId">
            <a href="" @click.prevent="registToggle()">注册</a>
          </span>
          <span v-if="!userId">
            <a href="" @click.prevent="loginToggle()">登录</a>
          </span>
        </div>
      </div>
    </div>
    <el-carousel trigger="hover" height="640px">
      <el-carousel-item v-for="(item,index) in photos" :key="index">
        <img :src="item" alt="">
      </el-carousel-item>
    </el-carousel>
    <div class="search-box">
      <i class="el-icon-search search-icon" size="medium"></i>
      <input class="search-input" type="text">
      <button class="search">搜索</button>
    </div>
    <div class="city-photo-box clearfix">
      <h2>热门短租城市</h2>
      <span class="remark">和你在另一个地方遇见美好</span>
      <div class="photo-container clearfix">
        <div class="photo-box">
          <a href="">
            <img src="../assets/8.jpg" alt="北京">
            <span class="title">北京</span>
          </a>
        </div>
        <div class="photo-box">
          <a href=""><img src="../assets/17.jpg" alt="上海">
            <span class="title">上海</span>
          </a>

        </div>
        <div class="photo-box">
          <a href=""> <img src="../assets/9.jpg" alt="成都">
            <span class="title">成都</span>
          </a>

        </div>
        <div class="photo-box">
          <a href=""><img src="../assets/16.jpg" alt="三亚">
            <span class="title">三亚</span>
          </a>

        </div>
        <div class="photo-box">
          <a href=""><img src="../assets/12.jpg" alt="杭州">
            <span class="title">杭州</span>
          </a>

        </div>
        <div class="photo-box">
          <a href=""> <img src="../assets/11.jpg" alt="广州">
            <span class="title">广州</span>
          </a>

        </div>
        <div class="photo-box">
          <a href=""> <img src="../assets/18.jpg" alt="厦门">
            <span class="title">厦门</span>
          </a>
        </div>
        <div class="photo-box">
          <router-link to="./HouseListPage"><img src="../assets/10.jpg" alt="重庆">
            <span class="title">重庆</span>
          </router-link>
        </div>
      </div>
      <transition name="fade">
        <regist-box v-show="isRegistShow" v-on:callback="registToggle()"></regist-box>
      </transition>
      <transition name="fade">
        <login-box v-show="isLoginShow" v-on:callback="loginToggle()"></login-box>
      </transition>

    </div>
  </div>

</template>


<script>
const url1 = require("../assets/4.jpg");
const url2 = require("../assets/5.jpg");
const url3 = require("../assets/6.jpg");
const url4 = require("../assets/7.jpg");

import qs from "qs";
import { mapGetters } from "vuex";
import LoginBox from "../components/LoginBox";
import RegistBox from "../components/RegistBox";

const HomePage = {
    data: function() {
        return {
            photos: [url1, url2, url3, url4],
            isRegistShow: false,
            isLoginShow: false
        };
    },
    components: {
        LoginBox: LoginBox,
        RegistBox: RegistBox
    },
    computed: {
        ...mapGetters(["userId"])
    },
    methods: {
        registToggle: function() {
            this.isRegistShow = !this.isRegistShow;
        },
        loginToggle: function() {
            this.isLoginShow = !this.isLoginShow;
        },
        logout: function() {
            const self = this;

            this.$axios.post("/c2c/logout").then(function(response) {
                var data = response.data;

                if (data.success) {
                    // logout success
                    self.$cookie.deleteAllCookies();
                    self.$router.push("/");
                }
            });
        }
    }
};

export default HomePage;
</script>

<style lang="scss" scoped>
#home-page {
    width: 100%;

    .header {
        position: absolute;
        z-index: 10;
        top: 0px;
        width: 100%;
        height: 40px;
        background: rgba(0, 0, 0, 0.3);

        .container {
            margin: 0 auto;
            width: 1300px;
            color: #fff;
            font-size: 16px;
            line-height: 40px;

            span {
                margin-left: 20px;
            }

            a {
                color: #fff;
            }

            a:hover {
                color: #ff5a5f;
            }

            .left-bar {
                float: left;
            }

            .right-bar {
                float: right;
            }
        }
    }

    .search-box {
        position: absolute;
        z-index: 10;
        top: 470px;
        left: 0;
        right: 0;
        margin: 0 auto;

        .search-icon {
            position: absolute;
            margin-top: 13px;
            margin-left: 15px;
            font-size: 30px;
        }

        .search-input {
            width: 950px;
            height: 50px;
            font-size: 20px;
            padding-left: 50px;
        }

        .search {
            position: absolute;
            margin-left: -110px;
            margin-top: 7px;
            border: none;
            border-radius: 5px;
            width: 100px;
            height: 40px;
            background: #ff5a5f;
            color: #fff;
        }
    }

    .city-photo-box {
        margin-bottom: 100px;

        h2 {
            font-size: 36px;
            margin-bottom: 15px;
        }

        .remark {
            font-size: 16px;
            color: #5b5a5a;
        }

        .photo-container {
            width: 1200px;
            margin: 0 auto;
            margin-top: 20px;

            .photo-box {
                display: inline-block;
                float: left;
                width: 300px;
                height: 180px;
                background: #000;

                a:hover img {
                    filter: alpha(Opacity=80);
                    -moz-opacity: 0.8;
                    opacity: 0.8;
                }

                img {
                    width: 300px;
                    height: 180px;
                }

                .title {
                    position: absolute;
                    margin-left: -190px;
                    margin-top: 55px;
                    font-size: 36px;
                    color: #fff;
                }
            }
        }
    }
}
</style>

