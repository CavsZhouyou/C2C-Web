/*
 * @Author: zhouyou@werun 
 * @Descriptions: 房屋详情页面 
 * @Date: 2018-07-05 21:58:39 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-11 21:14:21
 */


<template>
    <div id="house-detail-page">
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
        <div class="img-show">
            <el-carousel trigger="hover" height="500px">
                <el-carousel-item v-for="(item,index) in defaultData.acc_images" :key="index">
                    <img :src="item" alt="">
                </el-carousel-item>
            </el-carousel>
        </div>
        <div class="content">
            <div class="line">
                <span class="remark">&nbsp;&nbsp;&nbsp;&nbsp;威海市 · 整套独户房里的独立房间</span>
                <h1>{{defaultData.acc_address}}</h1>
            </div>
            <div class="line">
                <h3>房源信息</h3>
                <span>房屋类型：{{defaultData.acc_type_name}}</span>
                <span>房屋面积：{{defaultData.acc_capacity}}</span>
                <span>房屋价格：{{defaultData.acc_price}}</span>
                <br>
                <br>
            </div>
            <div class="line">
                <h3>关于此房源</h3>
                <p>
                    {{defaultData.acc_description}}
                </p>
                <!-- <p>欢迎来到DUDUSA</p>
                <p>1. 这里有个小型画室,可以和我们一起画油画,画盘子,画包包等很多好玩的东西(画画是收费项目,住宿客人有折扣) </p>
                <p>2. 这是一个二楼的阁楼间,虽然空高不高,但是应有尽有,配有小米4k电视机,您可以在线看电视电影甚至可以打王者荣耀等手机游戏!您也可以玩任天堂红白游戏机、桌游等,我们配了一个超大龙猫床垫,可爱温馨,阁楼是开放式的,有帘子,女生可以放心。</p>
                <p>3. 卫生间在楼下,是和雨房间共用,24小时热水,厨房有各种生活必需品满足您自己做饭洗衣的需求,提供免费Wi-Fi,一次性牙膏牙刷,床上用品和毛巾都是一客一换,干净卫生。</p>
                <p>4. 枕芯全部采用希尔顿酒店专供枕芯,舒适安稳!</p>
                <p>5. 房屋有一个超大露台,远眺成都电视塔,闹市区有一方天地,闹中取静,沏一壶茶悠然自得,让您的劳累一闪而过</p>
                <p>6. 房屋位置绝佳,位于成都市中心,楼下便是太古里入口,成都时尚汇聚之地,走路5分钟就到IFS,有各大景区直通车,再往前走5分钟就到春熙路,各种小吃琳琅满目!走路10分钟到兰桂坊酒吧一条街,体验成都独有夜生活!紧挨地铁口,出行方便,3分钟到地铁东门大桥站,5分钟到地铁春熙路站</p> -->
            </div>
            <div class="order-container">
                <div class="lessor-box">
                    <img :src="defaultData.headico" class="head-img">
                    <span class="name">房东：{{defaultData.nickname}}</span>
                    &nbsp;&nbsp;&nbsp;
                    <span class="phone">
                        <a href="">联系房东 &nbsp;{{defaultData.phone}}</a>
                    </span>
                    <br>
                    <br>
                    <span class="comment">
                        共收到{{defaultData.comment_count }}条评价 · 已验证
                    </span>
                </div>
                <button class="order" @click.prevent="order()">
                    <a href="javascript:;">马上预定</a>
                </button>
            </div>
            <div class="comment-box clearfix">
                <div class="line">
                    <h2>评价</h2>
                    <span>
                        <i class="el-icon-star-on"></i>
                        <i class="el-icon-star-on"></i>
                        <i class="el-icon-star-on"></i>
                        <i class="el-icon-star-on"></i>
                        <i class="el-icon-star-on"></i>
                        <span class="remark">{{defaultData.comment_count }}条评价</span>
                    </span>
                </div>
                <div class="comment-line line" v-for="(comment, index) in commentList" :key="index">
                    <img :src="comment.headico" class="head-img">
                    <span class="name">{{comment.nickname}}</span>
                    &nbsp;&nbsp;&nbsp;
                    <br>
                    <br>
                    <span>{{comment.date}}</span>
                    <br>
                    <br>
                    <p>{{comment.content}}</p>
                </div>
                <!-- <div class="comment-line line">
                    <img src="../assets/20.jpg" class="head-img">
                    <span class="name">阿萨</span>
                    &nbsp;&nbsp;&nbsp;
                    <br>
                    <br>
                    <span>2018年6月</span>
                    <br>
                    <br>
                    <p>整个房屋的设计非常用心，小姐姐是个非常有品位的人，房源离地铁站大概500米，很近，步行至春熙路太古里5到10分钟。总之体验挺好的。</p>
                </div>
                <div class="comment-line line">
                    <img src="../assets/21.jpg" class="head-img">
                    <span class="name">阿罗</span>
                    &nbsp;&nbsp;&nbsp;
                    <br>
                    <br>
                    <span>2018年6月</span>
                    <br>
                    <br>
                    <p>确实很好很好很好 装修风格很适合女孩子入住 性价比非常高 稍有欠缺的就是房间是合住的 可能会有人不习惯 其他真的非常完美 地理位置也好 附近吃的也好 房东也会积极帮助解决你遇到的各种问题 总而言之很nice的一次体验 下次希望带上小伙伴一起来</p>
                </div> -->
                <div class="load" @click="getCommentList()" v-show="!isEnd">
                    加载更多
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
import { mapGetters } from "vuex";
import LoginBox from "../components/LoginBox";
import RegistBox from "../components/RegistBox";

const HouseDetailPage = {
    data: function() {
        return {
            isRegistShow: false,
            isLoginShow: false,

            defaultData: {},
            start: 0,
            isEnd: false,
            commentList: []
        };
    },
    components: {
        LoginBox: LoginBox,
        RegistBox: RegistBox
    },
    computed: {
        ...mapGetters(["userId", "roleId"])
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

        order: function() {
            if (!this.userId) {
                this.$message.error("请先登录账号！");
            } else if (this.roleId != 4) {
                this.$message.error("该账号没有租房权限！");
            } else {
                this.$router.push(
                    "/PersonalCenterPage/ReleaseOrderPage/" +
                        this.$route.params.buildingId
                );
            }
        },

        getBuildingInformation: function() {
            const self = this;

            var postData = {
                acc_id: this.$route.params.buildingId
            };

            this.$axios
                .post("/c2c/accommodation/show", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.defaultData = data;
                    }
                });
        },

        getCommentList: function() {
            const self = this;

            var postData = {
                index: this.start,
                count: 5,
                acc_id: this.$route.params.buildingId
            };

            this.$axios
                .post("/c2c/comment/list", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.commentList = self.commentList.concat(
                            data.comments
                        );
                        self.start += 5;

                        if (data.empty) {
                            self.isEnd = true;
                        }
                    }
                });
        }
    },
    created() {
        this.getBuildingInformation();
        this.getCommentList();
    }
};

export default HouseDetailPage;
</script>



<style lang="scss" scoped>
#house-detail-page {
    width: 100%;
    padding-bottom: 50px;

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

    .img-show {
        margin: 0 auto;
        margin-top: 15px;
        width: 1300px;

        img {
            width: 1300px;
            height: 500px;
        }
    }

    .content {
        margin: 0 auto;
        width: 1300px;
        text-align: left;
        margin-top: 10px;

        .line {
            border-bottom: 1px solid #bbb;

            h1 {
                margin: 20px 0;
                margin-top: 10px;
            }

            .remark {
                font-size: 14px;
            }
        }

        .order-container {
            position: relative;
            margin-left: 80px;
            margin-top: 20px;

            .head-img {
                position: absolute;
                margin-left: -80px;
                margin-top: -5px;
                border-radius: 35px;
                width: 70px;
                height: 70px;
            }

            .name {
                font-weight: bold;
            }

            .phone {
                font-weight: bold;

                a {
                    color: #008489;
                }
            }

            .comment {
                font-size: 13px;
            }

            .order {
                position: absolute;
                top: 15px;
                right: 0;
                border: none;
                border-radius: 5px;
                width: 200px;
                height: 50px;
                background: #ff5a5f;
                color: #fff;

                a {
                    color: #fff;
                }
            }
        }

        .comment-box {
            margin-top: 70px;

            .el-icon-star-on {
                color: #00847f;
            }

            .comment-line {
                min-height: 100px;
                margin-top: 40px;
                padding-left: 70px;

                .head-img {
                    position: absolute;
                    margin-left: -80px;
                    margin-top: -5px;
                    border-radius: 35px;
                    width: 70px;
                    height: 70px;
                }

                .name {
                    font-weight: bold;
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
}
</style>

