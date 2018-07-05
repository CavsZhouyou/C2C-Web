/*
 * @Author: zhouyou@werun 
 * @Descriptions: 房屋列表页面 
 * @Date: 2018-07-05 20:34:30 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-05 21:43:09
 */



<template>
    <div id="house-list-page">
        <div class="header">
            <div class="container clearfix">
                <div class="left-bar">
                    <span class="city">
                        <a href="">重庆&nbsp;&nbsp;&nbsp; [点击切换]</a>
                    </span>
                </div>
                <div class="right-bar">
                    <span v-if="isLogined">
                        <a href="">个人中心</a>
                    </span>
                    <span v-if="!isLogined">
                        <a href="" @click.prevent="registToggle()">注册</a>
                    </span>
                    <span v-if="!isLogined">
                        <a href="" @click.prevent="loginToggle()">登录</a>
                    </span>
                    <span>
                        <a href="">帮助</a>
                    </span>
                </div>
            </div>
        </div>
        <div class="photo-content">
            <div class="photo-content-title clearfix">
                <h2 class="title">重庆</h2>
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
    </div>
</template>




<script>
const url1 = require("../assets/1.png");
const url2 = require("../assets/2.png");
const url3 = require("../assets/3.png");
const url4 = require("../assets/13.png");

const HouseListPage = {
    data: function() {
        return {
            photos1: [url1, url2, url3, url4],
            photos2: [url2, url3, url4, url1],
            photos3: [url3, url4, url1, url2],
            photos4: [url4, url1, url2, url3]
        };
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
