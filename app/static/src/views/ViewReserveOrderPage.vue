/*
 * @Author: zhouyou@werun 
 * @Descriptions: 查看预定订单页面 
 * @Date: 2018-07-06 11:00:27 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-06 11:28:56
 */

<template>
    <div id="view-reserve-order-page">
        <div class="line">
            <h2>查看预定订单</h2>
        </div>
        <div class="line order">
            <div class="left-bar">
                <img src="../assets/1.png" class="head-img">
                <br> &nbsp;&nbsp;&nbsp;
                <span>房屋信息：</span>&nbsp;&nbsp;
                <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>最多住2人</span>
                <br>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span>租户姓名：大雄</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>租户电话：15550671537</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>出租金额：1000</span>
                <span class="delete">
                    <i class="el-icon-circle-close"></i>
                    <a href="">取消订单</a>
                </span>
            </div>
        </div>
        <div class="line order">
            <div class="left-bar">
                <img src="../assets/2.png" class="head-img">
                <br> &nbsp;&nbsp;&nbsp;
                <span>房屋信息：</span>&nbsp;&nbsp;
                <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>最多住2人</span>
                <br>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span>租户姓名：大雄</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>租户电话：15550671537</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>出租金额：1000</span>
                <span class="delete">
                    <i class="el-icon-circle-close"></i>
                    <a href="">取消订单</a>
                </span>
            </div>
        </div>
        <div class="line order">
            <div class="left-bar">
                <img src="../assets/3.png" class="head-img">
                <br> &nbsp;&nbsp;&nbsp;
                <span>房屋信息：</span>&nbsp;&nbsp;
                <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>最多住2人</span>
                <br>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span>租户姓名：大雄</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>租户电话：15550671537</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>出租金额：1000</span>
                <span class="delete">
                    <i class="el-icon-circle-close"></i>
                    <a href="">取消订单</a>
                </span>
            </div>
        </div>
        <div class="line order">
            <div class="left-bar">
                <img src="../assets/13.png" class="head-img">
                <br> &nbsp;&nbsp;&nbsp;
                <span>房屋信息：</span>&nbsp;&nbsp;
                <span>1间卧室</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1张床</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>1个公共卫生间</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>最多住2人</span>
                <br>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span>租户姓名：大雄</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>租户电话：15550671537</span>&nbsp;&nbsp;&nbsp;&nbsp;
                <span>出租金额：1000</span>
                <span class="delete">
                    <i class="el-icon-circle-close"></i>
                    <a href="">取消订单</a>
                </span>
            </div>
        </div>
    </div>
</template>


<script>
const ViewReserveOrderPage = {};

export default ViewReserveOrderPage;
</script>


<style lang="scss" scoped>
#view-reserve-order-page {
    padding: 30px;
    text-align: left;

    .line {
        border-bottom: 1px solid #bbb;
    }

    .order {
        min-height: 100px;
        padding: 20px 0 20px;
        font-size: 14px;

        .left-bar {
            padding-left: 160px;

            .head-img {
                position: absolute;
                margin-left: -160px;
                width: 150px;
                height: 100px;
            }

            .delete {
                position: absolute;
                margin-left: 80px;
                margin-top: -30px;
                color: #e51c23;

                a {
                    color: #e51c23;
                }
            }
        }
    }
}
</style>
