/*
 * @Author: zhouyou@werun 
 * @Descriptions: 个人中心页面 
 * @Date: 2018-07-06 08:29:15 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-11 15:32:52
 */


<template>
    <div id="personal-center-page">
        <div class="header">
            <div class="header-content">
                <div class="container clearfix">
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
                        <img :src="headImg" alt="" class="head-img">
                        <span class="name">{{nickName}}</span>
                        <span>
                            <a href="" @click.prevent="logout()">退出</a>
                        </span>
                    </div>
                </div>
            </div>
        </div>
        <div class="content clearfix">

            <div class="container">
                <transition name="fade" enter-active-class="fadeInLeft" leave-active-class="fadeOutRight" mode="out-in">
                    <router-view></router-view>
                </transition>

            </div>
            <div class="sidebar">
                <ul>
                    <li v-if="roleId==1" :class="{clicked: index === 1}" @click="addClass(1)">
                        <router-link to="/PersonalCenterPage/UserManagePage">用户管理</router-link>
                    </li>
                    <li v-if="roleId==2" :class="{clicked: index === 2}" @click="addClass(2)">
                        <router-link to="/PersonalCenterPage/ReleaseDisclaimerPage">发布免责声明</router-link>
                    </li>
                    <li v-if="roleId==2" :class="{clicked: index === 3}" @click="addClass(3)">
                        <router-link to="/PersonalCenterPage/ReleaseTravelInformationPage">发布旅游信息</router-link>
                    </li>
                    <li v-if="roleId==2" :class="{clicked: index === 4}" @click="addClass(4)">
                        <router-link to="/PersonalCenterPage/ReleaseBuildingRecommendPage">发布住宿推荐信息</router-link>
                    </li>
                    <li v-if="roleId==2" :class="{clicked: index === 5}" @click="addClass(5)">
                        <router-link to="/PersonalCenterPage/ViewReserveOrderPage">查看预订单</router-link>
                    </li>
                    <li v-if="roleId==3" :class="{clicked: index === 6}" @click="addClass(6)">
                        <router-link to="/PersonalCenterPage/ReleaseBuildingPage">发布房源信息</router-link>
                    </li>
                    <li v-if="roleId==3" :class="{clicked: index === 7}" @click="addClass(7)">
                        <router-link to="/PersonalCenterPage/ViewBuildingPage">查看已发布房源</router-link>
                    </li>
                    <li v-if="roleId==3" :class="{clicked: index === 8}" @click="addClass(8)">
                        <router-link to="/PersonalCenterPage/ViewBuildingOrdersPage">查看房源订单</router-link>
                    </li>
                    <li v-if="roleId==100" :class="{clicked: index === 9}" @click="addClass(9)">
                        <router-link to="/PersonalCenterPage/ReleaseOrderPage">发布预定订单</router-link>
                    </li>
                    <li v-if="roleId==4" :class="{clicked: index === 10}" @click="addClass(10)">
                        <router-link to="/PersonalCenterPage/ViewAllOrdersPage">查看所有订单</router-link>
                    </li>
                    <li :class="{clicked: index === 11}" @click="addClass(11)">
                        <router-link to="/PersonalCenterPage/PersonalDataPage">个人资料</router-link>
                    </li>
                    <li :class="{clicked: index === 12}" @click="addClass(12)">
                        <router-link to="/PersonalCenterPage/ChangePasswordPage">修改密码</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>


<script>
import { mapActions } from "vuex";
import { mapGetters } from "vuex";

const PersonalCenterPage = {
    data: function() {
        return {
            index: 0
        };
    },
    computed: {
        ...mapGetters(["roleId", "headImg", "nickName"])
    },
    methods: {
        ...mapActions(["updateUserId"]),

        logout: function() {
            const self = this;

            this.$axios.post("/c2c/logout").then(function(response) {
                var data = response.data;

                if (data.success) {
                    // logout success
                    self.$cookie.deleteAllCookies();
                    self.updateUserId();
                    self.$router.push("/");
                    location.reload();
                }
            });
        },

        addClass: function(index) {
            this.index = index;
        }
    }
};

export default PersonalCenterPage;
</script>


<style lang="scss" scoped>
#personal-center-page {
    .header {
        background: url("../assets/bg.png");
        .header-content {
            height: 50px;
            line-height: 50px;
            background: rgba(0, 0, 0, 0.1);

            .container {
                width: 1100px;
                margin: 0 auto;

                a {
                    color: #fff;
                    font-weight: bold;
                }

                a:hover {
                    color: #ff5a5f;
                }

                .left-bar {
                    float: left;

                    span {
                        margin-right: 20px;
                    }
                }

                .right-bar {
                    float: right;
                    span {
                        margin-left: 20px;
                        color: #fff;
                    }

                    .head-img {
                        width: 40px;
                        height: 40px;
                        border-radius: 20px;
                        vertical-align: middle;
                    }
                }
            }
        }
    }

    .content {
        position: relative;
        background: #f2f2f2;
        min-height: 880px;

        .sidebar {
            position: absolute;
            top: 20px;
            left: 350px;

            ul {
                list-style: none;

                li {
                    margin-bottom: 6px;
                    width: 150px;
                    height: 40px;
                    background: #fff;
                    line-height: 40px;
                    font-weight: bold;

                    a {
                        display: inline-block;
                        width: 150px;
                        height: 40px;
                        font-size: 14px;
                        color: #667d94;
                    }

                    a:hover {
                        background: #3891d7;
                        color: #fff;
                    }
                }
            }

            li {
                width: 150px;
                height: 40px;
                background: #fff;

                a {
                    color: #667d94;
                }
            }
        }

        .clicked {
            a {
                background: #3891d7;
                color: #fff !important;
            }
        }

        .container {
            margin: 0 auto;
            margin-top: 30px;
            width: 800px;
            min-height: 800px;
            border-radius: 20px;
            background: #fff;
        }
    }
}
</style>
