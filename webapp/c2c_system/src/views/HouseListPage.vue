/*
 * @Author: zhouyou@werun 
 * @Descriptions: 房屋列表页面 
 * @Date: 2018-07-05 20:34:30 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-12 11:21:03
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
                        <el-select v-model="city" placeholder="城市" class="select-box" @change="getCounty()">
                            <el-option v-for="item in cityOptions" :key="item.value" :label="item.label" :value="item.value">
                            </el-option>
                        </el-select>
                    </li>
                    <li>
                        <el-select v-model="county" placeholder="区/县" class="select-box" @change="getStreet()">
                            <el-option v-for="item in countyOptions" :key="item.value" :label="item.label" :value="item.value">
                            </el-option>
                        </el-select>
                    </li>
                    <li>
                        <el-select v-model="street" placeholder="街道/镇" class="select-box" @change="getBuilding()">
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
                        <el-date-picker v-model="dateRange" type="daterange" align="right" unlink-panels range-separator="至" start-placeholder="开始日期" end-placeholder="结束日期" :picker-options="pickerOptions2">
                        </el-date-picker>
                    </li>
                </ul>
            </div>

            <div class="line search-option">
                <ul class="clearfix">
                    <li class="search-item" v-for="(item, index) in priceSearchList" :key="index" :class="{title:index===0}" @click="addClass('priceSelectIndex',index)">
                        <span :class="{selectItem: index === priceSelectIndex}">{{item.label}}</span>
                    </li>
                </ul>
            </div>
            <div class="line search-option">
                <ul class="clearfix">
                    <li class="search-item" v-for="(item, index) in areaSearchList" :key="index" :class="{title:index===0}" @click="addClass('areaSelectIndex',index)">
                        <span :class="{selectItem: index === areaSelectIndex}">{{item.label}}</span>
                    </li>
                </ul>
            </div>
            <div class="line search-option">
                <ul class="clearfix">
                    <li class="search-item" v-for="(item, index) in typeSearchList" :key="index" :class="{title:index===0}" @click="addClass('typeSelectIndex',index)">
                        <span :class="{selectItem: index === typeSelectIndex}">{{item.label}}</span>
                    </li>
                </ul>
            </div>
        </div>
        <div class="photo-content">
            <div class="photo-content-title clearfix">
                <h2 class="title">{{title}}</h2>
                <div class="search-box">
                    <i class="el-icon-search search-icon" size="medium"></i>
                    <input class="search-input" type="text">
                    <button class="search">搜索</button>
                </div>
            </div>

            <div class="photo-container clearfix">
                <div class="photo-box" :class="{first: (index+1) %3 ===1}" v-for="(building, index) in buildingList" :key="index">
                    <el-carousel trigger="hover" height="200px">
                        <el-carousel-item v-for="(item,index) in building.acc_images" :key="index">
                            <img :src="item" alt="" @click="viewBuildingDetail(building.acc_id)">
                        </el-carousel-item>
                    </el-carousel>
                    <div class="info">
                        <br>
                        <span class="price">￥{{building.acc_price}}元每晚</span>
                        <span>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <i class="el-icon-star-on"></i>
                            <span class="remark">{{building.acc_comment}}条评价</span>
                        </span>
                        <br><br>
                        <span>
                            &nbsp;{{building.acc_address}}
                        </span>
                        <br><br>
                        <span class="remark">
                            &nbsp;房屋类型：{{building.acc_type}}
                        </span>
                        <span class="remark">
                            &nbsp;房屋面积：{{building.acc_capacity}}
                        </span>
                        <img :src="building.headico" alt="" class="head-img">
                    </div>
                </div>
                <!-- <div class="photo-box">
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
                </div> -->
            </div>
            <div class="load" @click="getBuildingList()" v-show="!isEnd">
                加载更多
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
            cityOptions: [],
            county: "",
            countyOptions: [],
            street: "",
            streetOptions: [],

            priceSelectIndex: 1,
            priceSearchList: [
                { label: "价格（元/日）", min: 0, max: 0 },
                { label: "不限", min: 0, max: 0 },
                { label: "100以下", min: 0, max: 100 },
                { label: "100-300", min: 101, max: 300 },
                { label: "300-500", min: 301, max: 500 },
                { label: "500以上", min: 501, max: 0 }
            ],

            areaSelectIndex: 1,
            areaSearchList: [
                { label: "面积（m2）", min: 0, max: 0 },
                { label: "不限", min: 0, max: 0 },
                { label: "100以下", min: 0, max: 100 },
                { label: "100-200", min: 101, max: 200 },
                { label: "200-300", min: 201, max: 300 },
                { label: "300以上", min: 301, max: 0 }
            ],

            typeSelectIndex: 1,
            typeSearchList: [
                { value: 0, label: "房源类型" },
                { value: 0, label: "不限" },
                { value: 1, label: "公寓" },
                { value: 2, label: "民宿" },
                { value: 3, label: "客栈" },
                { value: 4, label: "酒店" },
                { value: 5, label: "独栋别墅" }
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
            dateRange: "",

            start: 0,
            isEnd: false,
            buildingList: [],

            title: "城市",

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
        setTitle: function() {
            this.title = this.cityOptions[this.city - 1].label;
        },
        addClass: function(selectPriceIndex, index) {
            this[selectPriceIndex] = index;
            this.start = 0;
            this.getBuildingList();
        },

        getCity: function() {
            const self = this;

            this.$axios.post("/c2c/city").then(function(response) {
                var data = response.data;

                if (data.success) {
                    self.cityOptions = data.citys;
                }
            });
        },
        getCounty: function() {
            const self = this;

            this.setTitle();

            var postData = {
                city_id: this.city
            };

            this.$axios.post("/c2c/county", postData).then(function(response) {
                var data = response.data;

                if (data.success) {
                    self.countyOptions = data.counties;
                }
            });
        },
        getStreet: function() {
            const self = this;

            var postData = {
                county_id: this.county
            };

            this.$axios.post("/c2c/street", postData).then(function(response) {
                var data = response.data;

                if (data.success) {
                    self.streetOptions = data.streets;
                }
            });
        },

        getBuilding: function() {
            this.index = 0;
            this.getBuildingList();
        },

        getBuildingList: function() {
            const self = this;

            var postData = {
                index: this.start,
                count: 9,
                city_id: this.city || 0,
                county_id: this.county || 0,
                street_id: this.street || 0,
                start: Date.parse(this.dateRange[0]),
                end: Date.parse(this.dateRange[1]),
                min_price: this.priceSearchList[this.priceSelectIndex].min,
                max_price: this.priceSearchList[this.priceSelectIndex].max,
                min_capacity: this.areaSearchList[this.areaSelectIndex].min,
                max_capacity: this.areaSearchList[this.areaSelectIndex].max,
                acc_type: this.typeSearchList[this.typeSelectIndex].value
            };

            this.$axios.post("/c2c/filter", postData).then(function(response) {
                var data = response.data;

                if (data.success) {
                    if (self.start === 0) {
                        self.buildingList = data.accommodations;
                    } else {
                        self.buildingList = self.buildingList.concat(
                            data.accommodations
                        );
                    }

                    self.start += 9;

                    if (data.empty) {
                        self.isEnd = true;
                    }
                }
            });
        },

        viewBuildingDetail: function(buildingId) {
            this.$router.push("/HouseDetailPage/" + buildingId);
        }
    },
    created() {
        this.getCity();
        this.getBuildingList();
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
            .title {
                text-align: left;
                pointer-events: none;
                cursor: default;
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

                    span {
                        font-size: 14px;
                    }

                    .remark {
                        color: #757373;
                    }

                    .head-img {
                        position: absolute;
                        margin-left: 100px;
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

        .load {
            margin-top: 50px;
            margin-bottom: 50px;
            text-align: center;
            font-style: italic;
            font-size: 20.9984px;
            color: #c5c5c5;
            cursor: pointer;
        }
    }
}
</style>
