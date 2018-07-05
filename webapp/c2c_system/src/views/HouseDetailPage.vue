/*
 * @Author: zhouyou@werun 
 * @Descriptions: 房屋详情页面 
 * @Date: 2018-07-05 21:58:39 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-05 22:51:35
 */


<template>
    <div id="house-detail-page">
        <div class="header">
            <div class="container clearfix">
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
        <div class="img-show">
            <img src="../assets/13.png" alt="">
        </div>
        <div class="content">
            <div class="line">
                <span class="remark">&nbsp;&nbsp;&nbsp;&nbsp;成都市 · 整套独户房里的独立房间</span>
                <h1>【DUDUSA·画】春熙路/太古里/兰桂坊 双地铁口 阁楼 超大露台画室艺术风</h1>
            </div>
            <div class="line">
                <h3>关于此房源</h3>
                <p>欢迎来到DUDUSA</p>
                <p>1. 这里有个小型画室,可以和我们一起画油画,画盘子,画包包等很多好玩的东西(画画是收费项目,住宿客人有折扣) </p>
                <p>2. 这是一个二楼的阁楼间,虽然空高不高,但是应有尽有,配有小米4k电视机,您可以在线看电视电影甚至可以打王者荣耀等手机游戏!您也可以玩任天堂红白游戏机、桌游等,我们配了一个超大龙猫床垫,可爱温馨,阁楼是开放式的,有帘子,女生可以放心。</p>
                <p>3. 卫生间在楼下,是和雨房间共用,24小时热水,厨房有各种生活必需品满足您自己做饭洗衣的需求,提供免费Wi-Fi,一次性牙膏牙刷,床上用品和毛巾都是一客一换,干净卫生。</p>
                <p>4. 枕芯全部采用希尔顿酒店专供枕芯,舒适安稳!</p>
                <p>5. 房屋有一个超大露台,远眺成都电视塔,闹市区有一方天地,闹中取静,沏一壶茶悠然自得,让您的劳累一闪而过</p>
                <p>6. 房屋位置绝佳,位于成都市中心,楼下便是太古里入口,成都时尚汇聚之地,走路5分钟就到IFS,有各大景区直通车,再往前走5分钟就到春熙路,各种小吃琳琅满目!走路10分钟到兰桂坊酒吧一条街,体验成都独有夜生活!紧挨地铁口,出行方便,3分钟到地铁东门大桥站,5分钟到地铁春熙路站</p>
            </div>
            <div class="line">
                <h3>房源细节</h3>
                <p>88元/晚的价格是一个人入住的价格，如果您是两人入住，需要加40元/天，相当于两人入住价格是128元/晚，谢谢理解哟</p>
            </div>
            <div class="order-container">
                <div class="lessor-box">
                    <img src="../assets/19.jpg" class="head-img">
                    <span class="name">房东：Linda</span>
                    &nbsp;&nbsp;&nbsp;
                    <span class="phone">
                        <a href="">联系房东</a>
                    </span>
                    <br>
                    <br>
                    <span class="comment">
                        共收到203条评价 · 已验证
                    </span>
                </div>
                <button class="order">马上预定</button>
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
                        <span class="remark">148条评价</span>
                    </span>
                </div>
                <div class="comment-line line">
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
                    <img src="../assets/20.jpg" class="head-img">
                    <span class="name">阿罗</span>
                    &nbsp;&nbsp;&nbsp;
                    <br>
                    <br>
                    <span>2018年6月</span>
                    <br>
                    <br>
                    <p>确实很好很好很好 装修风格很适合女孩子入住 性价比非常高 稍有欠缺的就是房间是合住的 可能会有人不习惯 其他真的非常完美 地理位置也好 附近吃的也好 房东也会积极帮助解决你遇到的各种问题 总而言之很nice的一次体验 下次希望带上小伙伴一起来</p>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
const HouseDetailPage = {};

export default HouseDetailPage;
</script>



<style lang="scss" scoped>
#house-detail-page {
    width: 100%;
    padding-bottom: 200px;

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
        margin-top: 15px;
        img {
            width: 1300px;
            height: 400px;
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
        }
    }
}
</style>

