/*
 * @Author: zhouyou@werun 
 * @Descriptions: 房屋列表页面 
 * @Date: 2018-07-05 20:34:30 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-10 20:57:09
 */



<template>
    <div id="house-list-page">
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
                    <span>
                        <a href="">帮助</a>
                    </span>
                </div>
            </div>
        </div>
        <div class="search-bar">
            <div class="line address">
                <ul class="clearfix">
                    <li class="search-item title">
                        <span>位置</span>
                    </li>
                    <li>
                        <el-select v-model="city" placeholder="城市" class="select-box">
                            <el-option v-for="item in cityOptions" :key="item.value" :label="item.label" :value="item.value">
                            </el-option>
                        </el-select>
                    </li>
                    <li>
                        <el-select v-model="town" placeholder="区/县" class="select-box">
                            <el-option v-for="item in townOptions" :key="item.value" :label="item.label" :value="item.value">
                            </el-option>
                        </el-select>
                    </li>
                    <li>
                        <el-select v-model="street" placeholder="街道/镇" class="select-box">
                            <el-option v-for="item in streetOptions" :key="item.value" :label="item.label" :value="item.value">
                            </el-option>
                        </el-select>
                    </li>
                </ul>
            </div>
            <div class="line time">
                <ul class="clearfix">
                    <li class="search-item title">
                        <span>租房时间</span>
                    </li>
                    <li>
                        <el-date-picker v-model="value7" type="daterange" align="right" unlink-panels range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期" :picker-options="pickerOptions2">
                        </el-date-picker>
                    </li>
                </ul>
            </div>

            <div class="line search-option">
                <ul class="clearfix">
                    <li class="search-item" v-for="(item, index) in priceSearchList" :key="index" :class="{title:index===0}" @click="addClass('priceSelectIndex',index)">
                        <span :class="{selectItem: index === priceSelectIndex}">{{item}}</span>
                    </li>
                </ul>
            </div>
            <div class="line search-option">
                <ul class="clearfix">
                    <li class="search-item" v-for="(item, index) in areaSearchList" :key="index" :class="{title:index===0}" @click="addClass('areaSelectIndex',index)">
                        <span :class="{selectItem: index === areaSelectIndex}">{{item}}</span>
                    </li>
                </ul>
            </div>
            <div class="line search-option">
                <ul class="clearfix">
                    <li class="search-item" v-for="(item, index) in typeSearchList" :key="index" :class="{title:index===0}" @click="addClass('typeSelectIndex',index)">
                        <span :class="{selectItem: index === typeSelectIndex}">{{item}}</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="photo-content">
            <div class="photo-content-title clearfix">
                <h2 class="title">威海</h2>
                <div class="search-box">
                    <i class="el-icon-search search-icon" size="medium"></i>
                    <input class="search-input" type="text">
                    <button class="search">搜索</button>
                </div>
            </div>

            <div class="photo-container clearfix">
                <div class="photo-box first">
                    <el-carousel trigger="hover" height="200px">
                        <el-carousel-item v-for="(item,index) in photos1" :key="index">
                            <img :src="item" alt="">
                        </el-carousel-item>
                    </el-carousel>
                    <div class="info">
                        <br>
                        <span class="price">￥ 562 元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">148条评价</span>
                        </span>
                        <br><br>
                        <span>
                            【DUDUSA·画】春熙路/太古里/兰桂坊...
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;独立房间 1室1床1卫
                        </span>
                        <img src="../assets/19.jpg" alt="" class="head-img">
                    </div>
                </div>
                <div class="photo-box">
                    <el-carousel trigger="hover" height="200px">
                        <el-carousel-item v-for="(item,index) in photos2" :key="index">
                            <img :src="item" alt="">
                        </el-carousel-item>
                    </el-carousel>
                    <div class="info">
                        <br>
                        <span class="price">￥ 562 元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">148条评价</span>
                        </span>
                        <br><br>
                        <span>
                            【DUDUSA·画】春熙路/太古里/兰桂坊...
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;独立房间 1室1床1卫
                        </span>
                        <img src="../assets/19.jpg" alt="" class="head-img">
                    </div>
                </div>
                <div class="photo-box">
                    <el-carousel trigger="hover" height="200px">
                        <el-carousel-item v-for="(item,index) in photos3" :key="index">
                            <img :src="item" alt="">
                        </el-carousel-item>
                    </el-carousel>
                    <div class="info">
                        <br>
                        <span class="price">￥ 562 元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">148条评价</span>
                        </span>
                        <br><br>
                        <span>
                            【DUDUSA·画】春熙路/太古里/兰桂坊...
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;独立房间 1室1床1卫
                        </span>
                        <img src="../assets/19.jpg" alt="" class="head-img">
                    </div>
                </div>
                <div class="photo-box first">
                    <router-link to="./HouseDetailPage">
                        <el-carousel trigger="hover" height="200px">
                            <el-carousel-item v-for="(item,index) in photos4" :key="index">
                                <img :src="item" alt="">
                            </el-carousel-item>
                        </el-carousel>
                    </router-link>
                    <div class="info">
                        <br>
                        <span class="price">￥ 562 元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">148条评价</span>
                        </span>
                        <br><br>
                        <span>
                            【DUDUSA·画】春熙路/太古里/兰桂坊...
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;独立房间 1室1床1卫
                        </span>
                        <img src="../assets/19.jpg" alt="" class="head-img">
                    </div>
                </div>
                <div class="photo-box ">
                    <el-carousel trigger="hover" height="200px">
                        <el-carousel-item v-for="(item,index) in photos1" :key="index">
                            <img :src="item" alt="">
                        </el-carousel-item>
                    </el-carousel>
                    <div class="info">
                        <br>
                        <span class="price">￥ 562 元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">148条评价</span>
                        </span>
                        <br><br>
                        <span>
                            【DUDUSA·画】春熙路/太古里/兰桂坊...
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;独立房间 1室1床1卫
                        </span>
                        <img src="../assets/19.jpg" alt="" class="head-img">
                    </div>
                </div>
                <div class="photo-box">
                    <el-carousel trigger="hover" height="200px">
                        <el-carousel-item v-for="(item,index) in photos2" :key="index">
                            <img :src="item" alt="">
                        </el-carousel-item>
                    </el-carousel>
                    <div class="info">
                        <br>
                        <span class="price">￥ 562 元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">148条评价</span>
                        </span>
                        <br><br>
                        <span>
                            【DUDUSA·画】春熙路/太古里/兰桂坊...
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;独立房间 1室1床1卫
                        </span>
                        <img src="../assets/19.jpg" alt="" class="head-img">
                    </div>
                </div>
                <div class="photo-box first">
                    <el-carousel trigger="hover" height="200px">
                        <el-carousel-item v-for="(item,index) in photos3" :key="index">
                            <img :src="item" alt="">
                        </el-carousel-item>
                    </el-carousel>
                    <div class="info">
                        <br>
                        <span class="price">￥ 562 元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">148条评价</span>
                        </span>
                        <br><br>
                        <span>
                            【DUDUSA·画】春熙路/太古里/兰桂坊...
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;独立房间 1室1床1卫
                        </span>
                        <img src="../assets/19.jpg" alt="" class="head-img">
                    </div>
                </div>
                <div class="photo-box">
                    <el-carousel trigger="hover" height="200px">
                        <el-carousel-item v-for="(item,index) in photos4" :key="index">
                            <img :src="item" alt="">
                        </el-carousel-item>
                    </el-carousel>
                    <div class="info">
                        <br>
                        <span class="price">￥ 562 元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">148条评价</span>
                        </span>
                        <br><br>
                        <span>
                            【DUDUSA·画】春熙路/太古里/兰桂坊...
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;独立房间 1室1床1卫
                        </span>
                        <img src="../assets/19.jpg" alt="" class="head-img">
                    </div>
                </div>
                <div class="photo-box">
                    <el-carousel trigger="hover" height="200px">
                        <el-carousel-item v-for="(item,index) in photos1" :key="index">
                            <img :src="item" alt="">
                        </el-carousel-item>
                    </el-carousel>
                    <div class="info">
                        <br>
                        <span class="price">￥ 562 元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">148条评价</span>
                        </span>
                        <br><br>
                        <span>
                            【DUDUSA·画】春熙路/太古里/兰桂坊...
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;独立房间 1室1床1卫
                        </span>
                        <img src="../assets/19.jpg" alt="" class="head-img">
                    </div>
                </div>
            </div>

        </div>
        <transition name="fade">
            <regist-box v-show="isRegistShow" v-on:callback="registToggle()"></regist-box>
        </transition>
        <transition name="fade">
            <login-box v-show="isLoginShow" v-on:callback="loginToggle()"></login-box>
        </transition>
    </div>
</template>




<script>
const url1 = require("../assets/1.png");
const url2 = require("../assets/2.png");
const url3 = require("../assets/3.png");
const url4 = require("../assets/13.png");

import { mapGetters } from "vuex";
import LoginBox from "../components/LoginBox";
import RegistBox from "../components/RegistBox";

const HouseListPage = {
    data: function() {
        return {
            photos1: [url1, url2, url3, url4],
            photos2: [url2, url3, url4, url1],
            photos3: [url3, url4, url1, url2],
            photos4: [url4, url1, url2, url3],

            city: "",
            cityOptions: [
                { value: 1, label: "威海市" },
                { value: 2, label: "北京市" },
                { value: 3, label: "重庆市" }
            ],
            town: "",
            townOptions: [
                { value: 1, label: "环翠区" },
                { value: 2, label: "荣成市" },
                { value: 3, label: "乳山市" },
                { value: 4, label: "文登区" },
                { value: 5, label: "其他区" }
            ],
            street: "",
            streetOptions: [
                { value: 1, label: "怡园街道" },
                { value: 2, label: "张村镇" },
                { value: 3, label: "温泉镇" },
                { value: 4, label: "西苑街道" },
                { value: 5, label: "竹岛街道" }
            ],

            priceSelectIndex: 1,
            priceSearchList: [
                "价格（元/日）",
                "不限",
                "100以下",
                "100-200",
                "200-300",
                "300-500",
                "500以上"
            ],

            areaSelectIndex: 1,
            areaSearchList: [
                "面积（m2）",
                "不限",
                "100以下",
                "100-200",
                "200-300",
                "300以上"
            ],

            typeSelectIndex: 1,
            typeSearchList: [
                "特色房型",
                "不限",
                "公寓",
                "名宿",
                "独栋别墅",
                "客栈",
                "酒店"
            ],

            pickerOptions2: {
                shortcuts: [
                    {
                        text: "最近一周",
                        onClick(picker) {
                            const end = new Date();
                            const start = new Date();
                            start.setTime(
                                start.getTime() - 3600 * 1000 * 24 * 7
                            );
                            picker.$emit("pick", [start, end]);
                        }
                    },
                    {
                        text: "最近一个月",
                        onClick(picker) {
                            const end = new Date();
                            const start = new Date();
                            start.setTime(
                                start.getTime() - 3600 * 1000 * 24 * 30
                            );
                            picker.$emit("pick", [start, end]);
                        }
                    },
                    {
                        text: "最近三个月",
                        onClick(picker) {
                            const end = new Date();
                            const start = new Date();
                            start.setTime(
                                start.getTime() - 3600 * 1000 * 24 * 90
                            );
                            picker.$emit("pick", [start, end]);
                        }
                    }
                ]
            },
            value6: "",
            value7: "",

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
        },

        addClass: function(selectPriceIndex, index) {
            this[selectPriceIndex] = index;
        }
    }
};

export default HouseListPage;
</script>


<style lang="scss" scoped>
#house-list-page {
    width: 100%;

    .header {
        width: 100%;
        height: 40px;

        .container {
            margin: 0 auto;
            width: 1300px;
            color: #000;
            font-size: 16px;
            line-height: 40px;

            .city {
                margin: 0;
            }

            span {
                margin-left: 20px;
            }

            a {
                color: #000;
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

    .search-bar {
        margin: 0 auto;
        margin-top: 30px;
        width: 1300px;

        .line {
            border-bottom: 1px solid #bbb;
        }

        ul {
            list-style: none;
            padding: 0;

            li {
                float: left;
                width: 120px;
                height: 30px;
                line-height: 30px;
                cursor: pointer;
            }
        }

        .address {
            li {
                width: 140px;
                height: 40px;
                text-align: left;
            }

            .select-box {
                width: 120px;

                input {
                    margin-right: 100px;
                    width: 120px;
                }
            }
        }

        .time {
            li {
                width: 140px;
                height: 40px;
                text-align: left;
            }

            .el-range-editor {
                width: 500px;
            }
        }

        .search-option {
            li:hover {
                span {
                    display: inline-block;
                    border-radius: 10px;
                    width: 80px;
                    height: 30px;
                    background: #1296db;
                    color: #fff;
                }
            }

            .title {
                text-align: left;
            }

            .selectItem {
                display: inline-block;
                border-radius: 10px;
                width: 80px;
                height: 30px;
                background: #1296db;
                color: #fff;
            }
        }
    }

    .photo-content {
        margin: 0 auto;
        margin-top: 30px;
        width: 1300px;

        .photo-content-title {
            padding-bottom: 15px;
            border-bottom: 1px solid #bbb;

            h2 {
                float: left;
                margin: 0;
                font-size: 48px;
            }

            .search-box {
                float: right;
                .search-icon {
                    position: absolute;
                    margin-top: 28px;
                    margin-left: 8px;
                    font-size: 30px;
                }

                .search-input {
                    margin-top: 20px;
                    width: 400px;
                    height: 40px;
                    padding-left: 50px;
                    font-size: 20px;
                }

                .search {
                    position: absolute;
                    margin-left: -105px;
                    margin-top: 25px;
                    border: none;
                    border-radius: 5px;
                    width: 100px;
                    height: 35px;
                    background: #ff5a5f;
                    color: #fff;
                }
            }
        }

        .photo-container {
            width: 1300px;

            .photo-box {
                float: left;
                margin-left: 50px;
                margin-top: 30px;
                margin-bottom: 10px;
                width: 400px;

                img {
                    width: 400px;
                    height: 220px;
                }

                .info {
                    text-align: left;

                    .price {
                        margin-right: 125px;
                        font-weight: bold;
                    }

                    .el-icon-star-on {
                        color: #00847f;
                    }

                    .remark {
                        color: #757373;
                    }

                    .head-img {
                        position: absolute;
                        margin-left: 150px;
                        margin-top: -45px;
                        border-radius: 40px;
                        width: 80px;
                        height: 80px;
                    }
                }
            }
            .first {
                margin-left: 0;
            }
        }
    }
}
</style>
