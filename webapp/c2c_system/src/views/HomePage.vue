<template>
  <div id="home-page">
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
          <a href=""><img src="../assets/10.jpg" alt="重庆">
            <span class="title">重庆</span>
          </a>
        </div>
      </div>
      <transition name="el-fade-in">
        <div class="bounce-box" v-show="isRegist">
          <div class="content">
            <a href="" @click.prevent="registToggle()">
              <i class="el-icon-close"></i>
            </a>
            <h3>用户注册</h3>
            <div class="line">
              <el-input placeholder="请输入用户名" prefix-icon="el-icon-edit-outline"></el-input>
            </div>
            <div class="line">
              <el-input type="password" placeholder="请输入密码" prefix-icon="el-icon-view"></el-input>
            </div>
            <div class="line">
              <el-input placeholder="请输入联系方式" prefix-icon="el-icon-mobile-phone"></el-input>
            </div>
            <div class="line">
              <el-input placeholder="请输入注册邮箱" prefix-icon="el-icon-message"></el-input>
            </div>
            <div class="line">
              <el-input placeholder="请输入姓名" prefix-icon="el-icon-edit-outline"></el-input>
            </div>
            <div class="line">
              <el-input placeholder="请输入身份证号码" prefix-icon="el-icon-tickets"></el-input>
            </div>
            <div class="line">
              <el-select v-model="role" placeholder="请选择角色" class="select-box">
                <el-option v-for="item in roles" :key="item.value" :label="item.label" :value="item.value">
                </el-option>
              </el-select>
            </div>
            <div class="line clearfix">
              <el-checkbox v-model="checked" class="check-box">我已经阅读并同意《寻房网服务协议》</el-checkbox>
            </div>
            <button @click="registToggle()">同意条款并注册</button>
          </div>
        </div>
      </transition>
      <transition name="el-fade-in">
        <div class="bounce-box" v-show="isLogin">
          <div class="content">
            <a href="" @click.prevent="loginToggle()">
              <i class="el-icon-close"></i>
            </a>
            <h3>用户登录</h3>
            <div class="line">
              <el-input placeholder="请输入用户名" prefix-icon="el-icon-edit-outline"></el-input>
            </div>
            <div class="line">
              <el-input type="password" placeholder="请输入密码" prefix-icon="el-icon-view"></el-input>
            </div>
            <button @click="login()">登录</button>
          </div>
        </div>
      </transition>
    </div>
    <div class="mask-layer" v-show="isMaskLayerShow"> </div>
  </div>

</template>


<script>
const url1 = require("../assets/4.jpg");
const url2 = require("../assets/5.jpg");
const url3 = require("../assets/6.jpg");
const url4 = require("../assets/7.jpg");

const HomePage = {
    data: function() {
        return {
            photos: [url1, url2, url3, url4],
            roles: [
                {
                    value: "0",
                    label: "租房用户"
                },
                {
                    value: "1",
                    label: "出租用户"
                }
            ],

            role: "",

            isMaskLayerShow: false,
            isRegist: false,
            isLogin: false,
            isLogined: false
        };
    },
    methods: {
        registToggle: function() {
            this.isMaskLayerShow = !this.isMaskLayerShow;
            this.isRegist = !this.isRegist;
        },
        loginToggle: function() {
            this.isMaskLayerShow = !this.isMaskLayerShow;
            this.isLogin = !this.isLogin;
        },
        login: function() {
            this.isMaskLayerShow = !this.isMaskLayerShow;
            this.isLogin = !this.isLogin;
            this.isLogined = true;
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

    .bounce-box {
        position: absolute;
        z-index: 12;
        top: 100px;
        left: 0;
        right: 0;
        margin: 0 auto;
        width: 450px;
        background: #fff;

        .content {
            position: relative;
            padding: 20px 30px 30px;

            a:hover {
                color: #ff5a5f;
            }

            .el-icon-close {
                position: absolute;
                top: 10px;
                right: 10px;
                font-size: 30px;
            }

            h3 {
                font-size: 24px;
            }

            .line {
                margin-bottom: 20px;

                .select-box {
                    width: 390px;
                }

                .check-box {
                    float: left;
                }

                ::-webkit-input-placeholder {
                    /* WebKit browsers */
                    color: #999;
                }
                :-moz-placeholder {
                    /* Mozilla Firefox 4 to 18 */
                    color: #999;
                }
                ::-moz-placeholder {
                    /* Mozilla Firefox 19+ */
                    color: #999;
                }
                :-ms-input-placeholder {
                    /* Internet Explorer 10+ */
                    color: #999;
                }
            }
            button {
                border: none;
                border-radius: 5px;
                width: 390px;
                height: 40px;
                background: #ff5a5f;
                color: #fff;
            }
        }
    }

    .login-box {
    }
}
</style>

