/*
 * @Author: zhouyou@werun 
 * @Descriptions: 查看预定订单页面 
 * @Date: 2018-07-06 11:00:27 
 * @Last Modified by: zhouyou@werun
 * @Last Modified time: 2018-07-12 11:00:03
 */

<template>
    <div id="view-reserve-order-page">
        <div class="line">
            <h2>查看预定订单</h2>
        </div>
        <!-- <div class="line order">
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
        </div> -->

        <div class="line order" v-for="(order, index) in orderList" :key="index">
            <div class="left-bar">
                <img :src="order.image" class="head-img">
                <br> &nbsp;&nbsp;&nbsp;
                <span class="first">出租者姓名：{{order.tenant_name}}</span>
                <span>出租者联系方式：{{order.tenant_phone}}</span>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span class="first">租户姓名：{{order.lessor_name}}</span>
                <span>租户联系方式：{{order.lessor_phone}}</span>
                <br>
                <br>&nbsp;&nbsp;&nbsp;
                <span class="first">出租金额：{{order.price}}</span>
                <span>出租时间：{{order.date}}</span>
                <span :class="{notAccept: order.state_id ==1 ,accept: order.state_id ==2,complete: order.state_id == 3,}">订单状态：{{order.state_name}}</span>
                <el-button class="delete" type="text" @click="deleteOrder(order.reservation_id, index)">
                    <i class="el-icon-circle-close"></i>&nbsp;删除订单</el-button>
            </div>
        </div>
        <div class="load" @click="getOrderList" v-show="!isEnd">
            加载更多
        </div>
    </div>
</template>


<script>
const ViewReserveOrderPage = {
    data: function() {
        return {
            orderList: [],
            start: 0,
            isEnd: false
        };
    },
    methods: {
        getOrderList: function() {
            const self = this;

            var postData = {
                index: this.start,
                count: 5
            };

            this.$axios
                .post("/c2c/reservation/list", postData)
                .then(function(response) {
                    var data = response.data;

                    if (data.success) {
                        self.orderList = self.orderList.concat(
                            data.reservations
                        );
                        self.start += 5;

                        if (data.empty) {
                            self.isEnd = true;
                        }
                    }
                });
        },

        deleteOrder: function(resId, index) {
            const self = this;

            this.$confirm("确认删除此订单吗?", "提示", {
                confirmButtonText: "确定",
                cancelButtonText: "取消",
                type: "warning"
            })
                .then(() => {
                    var postData = {
                        res_id: resId
                    };

                    this.$axios
                        .post("/c2c/reservation/delete", postData)
                        .then(function(response) {
                            var data = response.data;
                            if (data.success) {
                                self.orderList.splice(index, 1);
                                self.start = self.start - 1;
                                self.$message({
                                    message: "删除成功！",
                                    type: "success"
                                });
                            } else {
                                self.$message.error("删除失败！");
                            }
                        });
                })
                .catch(() => {
                    this.$message({
                        type: "info",
                        message: "已取消删除"
                    });
                });
        }
    },
    created() {
        this.getOrderList();
    }
};

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
                margin-left: 60px;
                margin-top: -20px;
                color: #e51c23;

                a {
                    color: #e51c23;
                }
            }

            .notAccept {
                position: absolute;
                margin-left: 60px;
                margin-top: -60px;
                color: #ff6107;

                a {
                    color: #ff6107;
                }
            }

            .accept {
                position: absolute;
                margin-left: 60px;
                margin-top: -45px;
                color: #3498db;

                a {
                    color: #3498db;
                }
            }

            .complete {
                position: absolute;
                margin-left: 60px;
                margin-top: -45px;
                color: #8bc34a;

                a {
                    color: #8bc34a;
                }
            }
        }
    }

    .first {
        display: inline-block;
        width: 150px;
    }

    .load {
        text-align: center;
        font-style: italic;
        font-size: 20.9984px;
        color: #c5c5c5;
        cursor: pointer;
    }
}
</style>
