/*
 * @Author: zhouyou@werun 
 * @Descriptions: 个人中心页面 
 * @Date: 2018-07-06 08:29:15 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-06 14:05:47
 */


<template>
    <div id="personal-center-page">
        <div class="header">
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
                    <img src="../assets/19.jpg" alt="" class="head-img">
                    <span class="name">Lakers</span>
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
                    <li>
                        <router-link to="/PersonalCenterPage/UserManagePage">用户管理</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/ReleaseDisclaimerPage">发布免责声明</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/ReleaseTravelInformationPage">发布旅游信息</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/ReleaseBuildingRecommendPage">发布住宿推荐信息</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/ViewReserveOrderPage">查看预订单</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/ReleaseBuildingPage">发布房源信息</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/ViewBuildingPage">查看已发布房源</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/ViewBuildingOrdersPage">查看房源订单</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/ReleaseOrderPage">发布预定订单</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/ViewAllOrdersPage">查看所有订单</router-link>
                    </li>
                    <li>
                        <router-link to="/PersonalCenterPage/PersonalDataPage">个人资料</router-link>
                    </li>
                    <li>
                        <router-link to="">修改密码</router-link>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</template>


<script>
const PersonalCenterPage = {};

export default PersonalCenterPage;
</script>


<style lang="scss" scoped>
#personal-center-page {
    .header {
        height: 60px;
        line-height: 60px;

        .container {
            width: 1100px;
            margin: 0 auto;

            a {
                color: #000;
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
