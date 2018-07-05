/*
 * @Author: zhouyou@werun 
 * @Descriptions: 主页
 * @Date: 2018-07-05 20:33:56 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-05 21:56:30
 */

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
          <router-link to="./HouseList"><img src="../assets/10.jpg" alt="重庆">
            <span class="title">重庆</span>
          </router-link>

        </div>
      </div>
      <transition name="fade">
        <div class="bounce-box" v-show="isRegistShow">
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
              <el-checkbox v-model="checked" class="check-box">我已经阅读并同意
                <a href="" @click.prevent="disclaimerToggle()">《寻房网服务协议》</a>
              </el-checkbox>
            </div>

            <button @click="registToggle()">同意条款并注册</button>
          </div>
        </div>
      </transition>
      <transition name="fade">
        <div class="bounce-box" v-show="isLoginShow">
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
      <transition name="fade">
        <div class="disclaimer-box bounce-box" v-show="isDisclaimerShow">
          <h3>免责声明</h3>
          <div class="content">
            <p> 寻房短租网由易云游网络技术（北京）有限公司运营的，属于提供技术支持的平台公司，涉及具体产品服务的，将由有资质的服务商或代理商提供。如果您在本网站、寻房短租关联公司网站或其他寻房短租提供的移动应用或软件上（以下简称“寻房短租网”），访问、预定或使用寻房短租的产品或服务（以上统称为“服务”），便视为用户接受了以下免责说明，请您仔细阅读以下内容，尤其是以下加粗及下划线字体。如果您不同意以下任何内容，请立刻停止访问/使用本网站或其他任何移动应用或软件所提供的相关服务。
            </p>
            <p>
              您完全同意及认可，寻房短租网是提供平台技术服务的合法公司，将具有相应资质或合法权益的酒店、旅馆、公寓、民宿、保洁信息、特色体验信息、旅行咨询或服务信息汇集于寻房短租网供用户查阅，同时帮助用户通过寻房短租网与上述服务提供商联系并预订相关服务项目。除明确交易一方主体为寻房短租外，交易的实质主体为上述服务提供商，寻房短租网并非交易的一方，对交易过程中产生的纠纷，并不承担相关责任，但寻房短租网会尽力协助用户与相关服务提供商行协商。
            </p>
            <p>
              您完全理解并同意，鉴于寻房短租以非人工检索方式、根据您键入的关键字或点击特定的产品或服务关键字自动生成的网页链接或相关的产品信息描述，例如价格、库存等，上述非人工检索方式，因缓存时间间隔或检索方式非完全智能等原因，有可能造成信息更新不及时或产品服务信息聚合、抽取不精准等瑕疵，您完全理解并豁免上述产品或服务瑕疵给您造成的不便，寻房短租不承担任何责任。
            </p>
            <p> 为方便您的使用，寻房短租可能会对产品的可信赖程度而进行的评级、推荐或风险提示仅供您参考，寻房短租不担保该等评级、推荐或风险提示的准确性和完整性，对推荐的网站的内容及服务亦不承担任何责任。</p>
            <p>
              您完全理解并同意，您通过寻房短租购买的产品或服务或此后新的产品和服务，应按照相关网页中展示的说明、规定或政策等履行相关义务，享有相关权利，该等说明、规定或政策等与本说明共同构成您和寻房短租的整体协议，您必须严格遵守。
            </p>
            <p>
              您了解并理解，任何经由寻房短租网提供服务而发布的图形、图片或个人言论等，均表示了内容提供者、服务使用者个人的观点、观念和思想，并不代表寻房短租的观点或主张，对于在享受网络服务的过程中可能会接触到令人不快、不适当等内容的，由您个人自行加以判断并承担所有风险，寻房短租不承担任何责任。
            </p>
            <p>
              寻房短租为所有出行服务提供方、第三方代理商（包括但不限于住宿、旅游产品、景点门票等）提供一个在线平台，供其宣传自己可供预订的产品及服务。例如，寻房短租平台上的临时住宿产品及服务信息（包括但不限于住宿方名称、联系人及联络信息、住宿场所的描述和说明、相关图片、视频等）均由住宿方自行提供并上传，由住宿提供方对其提供并上传的所有信息承担相应法律责任。各住宿提供方均能通过后台自行更新其房价、可预订客房数量以及显示在寻房短租平台上的其它信息。
            </p>
            <p>
              您完全理解并同意，通过寻房短租购买的产品或服务或此后新的产品和服务时，您在预订产品或服务后应当及时付款；您在预订产品或服务后未全额支付前，您尚未完成购买上述产品或服务。因上述产品或服务的价格、舱位、数量或库存等实时更新或变化而造成您的额外费用、损失或无库存等，由您自行承担，寻房短租不承担任何责任。您完全理解并同意，您在支付过程中，因网络中断、银行反馈信息错误等非寻房短租的原因造成的付款失败，由您自行承担，寻房短租不承担任何责任。
            </p>
            <p>
              请您及时保存或备份您的文字、图片等其他信息，您完全理解并同意，由于寻房短租储存设备有限、设备故障、设备更新或设备受到攻击等设备原因或人为原因，您使用网路服务储存的信息或数据等全部或部分发生删除、毁损、灭失或无法恢复的风险，均由您自行承担，寻房短租不承担任何责任。
            </p>
            <p>
              若有任何服务条款与法律相抵触，那这些条款将按尽可能接近的方法重新解析，而其它条款则保持对用户产生法律效力和影响。因解释本免责声明以及用户通过寻房短租网预订任何产品而导致的争议，将同意接受网站注册地北京市顺义区人民法院的管辖。
            </p>
          </div>
          <button @click="disclaimerToggle()">同意条款</button>
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
            isRegistShow: false,
            isLoginShow: false,
            isLogined: false,
            isDisclaimerShow: false
        };
    },
    methods: {
        registToggle: function() {
            this.isMaskLayerShow = !this.isMaskLayerShow;
            this.isRegistShow = !this.isRegistShow;
        },
        loginToggle: function() {
            this.isMaskLayerShow = !this.isMaskLayerShow;
            this.isLoginShow = !this.isLoginShow;
        },
        login: function() {
            this.isMaskLayerShow = !this.isMaskLayerShow;
            this.isLoginShow = !this.isLoginShow;
            this.isLogined = true;
        },
        disclaimerToggle() {
            this.isDisclaimerShow = !this.isDisclaimerShow;
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
        border-radius: 20px;
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

    .disclaimer-box {
        width: 900px;
        padding: 20px 30px 30px;
        margin-bottom: 100px;

        h3 {
            font-size: 30px;
            margin-bottom: 0;
        }

        button {
            border: none;
            border-radius: 5px;
            width: 200px;
            height: 40px;
            background: #3498db;
            color: #fff;
        }
    }
}
</style>

